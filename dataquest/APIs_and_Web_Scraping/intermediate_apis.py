#!/usr/bin/env python
"""
Most APIs require authentication. Imagine that you're using the Reddit API to pull a list of your
private messages. It would be a huge privacy breach for Reddit to give that information to anyone,
so requiring authentication makes sense.

Authentication is also used by APIs so that they can perform rate limiting. APIs are usually created
to enable users to build interesting applications or services. In order to ensure that the API is
available and responsive for all users, APIs prevent you from making too many requests in too short
of a time. This is known as rate limiting, and ensures that one user cannot overload the API server
by making too many requests too fast.

In this mission, we'll be exploring the Github API and using it to pull some interesting data on
repositories and users. Github is a site for hosting code (if you haven't looked at it, you should --
it's a great place to host a portfolio). Github has user accounts, repositories that contain code,
and organizations that can be created by companies.

You can find documentation on the API here:  https://developer.github.com/v3/
In particular, make sure to pay attention to the authentication section:
    https://developer.github.com/v3/#authentication

In order to authenticate with the Github API, we'll need to use an access token. An access token is
a credential that you can generate here:  https://github.com/settings/tokens
An access token is a string that the API can read and associate with your account.
"""
import requests
import sys

# boolen flags determine what should be done in regards to the new 'learning-about-apis' repo
CREATE_REPO = False
UPDATE_REPO = False
DELETE_REPO = False

# GitHub user
user = 'tleonhardt'

# GitHub Personal Access Token
# TODO: Replace this with your own working GitHub Personal Access Token
# NOTE: This is a fake value and will generate a 401 response due to "bad credentials"
access_token = "replace_me_with_your_own_github_personal_access_token"

# If a command line arguemnt is passed in, use that to override the GitHub access token
if len(sys.argv) > 1:
    access_token = sys.argv[1]

# Create a dictionary of headers, with our Authorization header.
headers = {"Authorization": "token {}".format(access_token)}

# Make a GET request to the Github API get info about a given user
response = requests.get("https://api.github.com/users/{}".format(user), headers=headers)
status_code = response.status_code
# Successful GET requests typically return status code 200
if 200 != status_code:
    print("GET Error: status code = {}\tdetails: {}".format(status_code, response.json()['message']))
    sys.exit(0)
# Assign the json content of the response to a variable
data = response.json()
# Print the content of the response
print('GitHub details for user {}:\n{}\n'.format(user, data))


# Make an authenticated request to retrieve organizations a GitHub user is in
response = requests.get("https://api.github.com/users/{}/orgs".format(user), headers=headers)
orgs = response.json()
print("{} is in the following GitHub organizations: {}\n".format(user, orgs))


# Get info on Linus Torvalds
linus = 'torvalds'
response = requests.get("https://api.github.com/users/{}".format(linus), headers=headers)
torvalds = response.json()
print('GitHub info for Linux Torvalds:\n{}\n'.format(torvalds))


# Get information on the Hello-World repository from octocat
response = requests.get('https://api.github.com/repos/octocat/Hello-World', headers=headers)
hello_world = response.json()
print("Info on octocat's Hello-World repo:\n{}\n".format(hello_world))


# Pagination - limiting the response to a maximum number of entries at a time
params = {"per_page": 50, "page": 1}
response = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params)
page1_repos = response.json()
print("1st page of repos starred by Vik Paruchuri contains {} items\n".format(len(page1_repos)))


# If you don't specify a user, it gives information on the user the token is for
response = requests.get("https://api.github.com/user", headers=headers)
user_info = response.json()
print("Info on the owner of this token: {}\n".format(user_info))


## POST requests
# In the last mission, we mentioned different types of requests. So far, we've been making GET
# requests. GET requests are used to retrieve information from the server (hence the name GET).
#There are a few other types of requests.
#
# One of them is called a POST request. POST requests are used to send information to the server,
# and create objects on the server. In our case, we can use POST requests to create new repositories.

# Create a new repository
new_repo = 'learning-about-apis'
payload = {"name": new_repo}

if CREATE_REPO:
    # We need to pass in our authentication headers!
    response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
    status = response.status_code
    if 201 != status:
        print("Error attempting to create a new repo: {}".format(response.json()))
    else:
        print("Successfully created a new repo named: {}".format(new_repo))


## PUT/PATCH Requests
# Sometimes, we don't want to make a new object, we just want to update an existing one. This is
# where PATCH and PUT requests come into play. We use PATCH requests when we want to change a few
# attributes of an object, and we don't want to send the whole object to the server (maybe we just
#  want to change the name of our repository, for example). We use PUT requests when we want to send
# the whole object to the server, and replace the version on the server with the version we went.
#
# In practice, API developers don't always respect this convention, and sometimes API endpoints that
# accept PUT requests will treat them like PATCH requests, and not require that the whole object be
# sent back.

# Update the description of an existing repository
if UPDATE_REPO:
    payload = {"description": "Learning about requests!", "name": new_repo}
    response = requests.patch("https://api.github.com/repos/{}/{}".format(user, new_repo), json=payload, headers=headers)
    status = response.status_code
    # A PATCH request will usually return a 200 status code if everything goes fine.
    if 200 != status:
        print("Error attempting to update existing repo '{}' for user {}: {}".format(new_repo, user, response.json()))
    else:
        print("Successfully updated description for existing repo '{}' for user {}".format(new_repo, user))


## DELETE Requests
# The final major request type is the DELETE request. The DELETE request removes objects from the
# server. We can use the DELETE request to remove repositories.
if DELETE_REPO:
    response = requests.delete("https://api.github.com/repos/{}/{}".format(user, new_repo), headers=headers)
    status = response.status_code
    # A successful DELETE request will usually return a 204 request, indicating that the object has been deleted.
    if 204 != status:
        print("Error attempting to delete repo '{}' for user {}: {}".format(new_repo, user, response.json()))
    else:
        print("Successfully deleted repo '{}' for user {}".format(new_repo, user))
