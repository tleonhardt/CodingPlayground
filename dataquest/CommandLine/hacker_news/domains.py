#!/usr/bin/env python
"""
Which domains were submitted most often?
"""
from read import load_data

# Read in the Hacker News dataset
hn = load_data()

def remove_subdomain(url):
    url_parts = str(url).split('.')
    if len(url_parts) < 2:
        return url

    # Deal with .uk, .au, etc.
    if len(url_parts[-1]) == 2:
        domain_parts = url_parts[-3:]
    else:
        domain_parts = url_parts[-2:]

    domain = '.'.join(domain_parts)
    return domain


# Make analysis more robust by removing subdomains
hn['domain'] = hn['url'].apply(remove_subdomain)

# Count the number of occurences of each domain
domains = hn['domain'].dropna().value_counts()

# Print the 100 most submitted domains
print(domains.head(100))
