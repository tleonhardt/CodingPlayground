#!/usr/bin/env python
"""
In this example, we will explore using the Reddit API to look at trending posts and comments.

If you're unfamiliar with Reddit, it's a community driven link-sharing site. Users submit articles
and links, and other users upvote the submissions, indicating they like them, or downvote them,
indicating they dislike them. Users can comment on submissions, and the comments can be upvoted or
downvoted as well. Reddit is composed of many smaller communities, or subreddits, where niche articles
can be discussed by a more focused community. Some examples are /r/python, a python-focused community,
and /r/sanfrancisco, a subreddit for discussing issues pertaining to the city of San Francisco, CA.

This exmaple demonstrates how to do the following:
    * Getting a list of trending articles in a subreddit.
    * Exploring the comments of a single article.
    * Posting our own comment on the article.

The Reddit API requires authentication. In this example, we will use OAuth. OAuth can be fairly
complex. You'll be using an authentication token to authenticate in much the same way that we did earlier,
except the header will look like this:
    {"Authorization": "bearer <token>"}

You'll also need to add a User-Agent header, which will tell Reddit that Dataquest is accessing the API:
    {"Authorization": "bearer <token>", "User-Agent": "<user>"}
"""
import requests
import requests.auth

# TODO: Replace these constants with those for your own reddit app
# NOTE: To create a reddit app, go to your login , click "preferences", then click on the "apps" tab
# Constants
app_client_id = 'ReplaceMe'
app_client_secret = 'ReplaceMe'
user_name = 'ReplaceMe'
password = 'ReplaceMe'
client_name = 'My Learning Script/0.1 by {}'.format(user_name)
subreddit = 'python'

# STEP 1:  Request an OAuth Token
client_auth = requests.auth.HTTPBasicAuth(app_client_id, app_client_secret)
post_data = {"grant_type": "password", "username": user_name, "password": password}
headers = {"User-Agent": client_name}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
oauth_data = response.json()

# STEP 2: Extract OAuth Token details from response
oauth_token = oauth_data['access_token']


# STEP 3: Use the token
headers = {"Authorization": "bearer {}".format(oauth_token),
          "User-Agent": "{}".format(client_name)}

##  Retrieve the top articles from the past day in the /r/python subreddit
params = {'t': 'day'}

# Make a GET request to https:oauth.reddit.com/r/python/top
response = requests.get("https://oauth.reddit.com/r/{}/top".format(subreddit), headers=headers, params=params)
status_code = response.status_code
# Successful GET requests typically return status code 200
if 200 != status_code:
    print("GET Error: status code = {}\tdetails: {}".format(status_code, response.json()['message']))
    sys.exit(0)
python_top = response.json()

## Getting the most upvoted article
# The variable python_top is a dictionary that contains information about all of the individual
# articles submitted in the past day. However, the list containing all of the articles is buried
# inside a dictionary key, and you'll need to explore the dictionary to retrieve the list.

# Extract the list containing all of the articles
python_top_articles = python_top['data']['children']

most_upvoted = ""
most_upvoted_title = ""
most_upvotes = 0
for article in python_top_articles:
    ar = article["data"]
    if ar["ups"] >= most_upvotes:
        most_upvoted = ar["id"]
        most_upvoted_title = ar["title"]
        most_upvotes = ar["ups"]
print("The most upvoted article from the past day on the /r/{} subreddit is '{}', with {} upvotes".format(subreddit,
                                                                                                          most_upvoted_title,
                                                                                                          most_upvotes))
## Getting Article comments
# Now that you have the id of the most upvoted article, you can retrieve the comments on it using
# the /r/{subreddit}/comments/{article} endpoint. You'll need to fill in the bracketed items with
# the appropriate value: {subreddit} -- should be the name of the subreddit the article is in (omit
# the leading /r, because it already exists). An example is python. {article} -- the id of the article
# to retrieve comments for. An example is 4b7w9u.
url = "https://oauth.reddit.com/r/{}/comments/{}".format(subreddit, most_upvoted)
response = requests.get(url, headers=headers)
if 200 != response.status_code:
    print("Error getting response: {}".format(response))
comments = response.json()


## Getting the most upvoted comments
# Querying the comments endpoint at /r/{subreddit}/comments/{article} returns a list. The first item
# in the list is information about the article, and the second item is information about the comments.
#
# The comments on Reddit can be nested, that is, comments can have their own comments. Here's an example.
#
# What this means is that the comments are represented very similarly to articles, but they have an
# additional key, replies, that contains other comments.

# Find the most upvoted top-level comment in commnts (ignoring replies)
comments_list = comments[1]['data']['children']
most_upvoted_comment = ""
most_commment_upvotes = 0
for comment in comments_list:
    com = comment["data"]
    if com["ups"] >= most_commment_upvotes:
        most_upvoted_comment = com["id"]
        most_commment_upvotes = com["ups"]
print("The most upvoted comment from the past day on the /r/{} subreddit had id '{}', with {} upvotes".format(subreddit,
                                                                                                              most_upvoted_comment,
                                                                                                              most_commment_upvotes))
## Upvoting a comment
# You can upvote a comment with the /api/vote endpoint. You'll need to pass in the following parameters:
#     dir -- vote direction, 1, 0, or -1. 1 is an upvote, and -1 is a downvote.
#      id -- the id of the article or comment to upvote.

# Make a POST request to the /api/vote endpoint to upvote the most upvoted comment
payload = {'dir': 1, 'id': most_upvoted_comment}
url = "https://oauth.reddit.com/api/vote"
response = requests.post(url, json=payload, headers=headers)
status = response.status_code
