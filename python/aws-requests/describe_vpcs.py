#!/usr/bin/env python
# coding=utf-8
"""Directly call the DescribeVpcs EC2 API using the aws-requests-auth module.

This is intended to be an example which can be easily modified to call other APIs and/or services and is effectively
a command-line programmatic replacement for using a graphical tool like Postman (https://www.getpostman.com).

The following Python modules are required and can be installed via pip:
- requests
    * Requests allows you to send HTTP/1.1 requests. There’s no need to manually add query strings to your URLs.
    * http://docs.python-requests.org
- aws-requests-auth
    * AWS signature version 4 signing process for the requests module
    * https://github.com/DavidMuller/aws-requests-auth
- botocore
    * A low-level interface to a growing number of Amazon Web Services (used here to automatically gather AWS creds)
    * https://github.com/boto/botocore
- lxml
    * XML toolkit for Python
    * https://github.com/lxml/lxml
- pygments
    * Pygments is a generic syntax highlighter that supports 300 languages including JSON, XML, HTML, YAML, Java, etc.
    * http://pygments.org
"""
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import TerminalFormatter
import requests
# This line will fail if you do not have both aws-requests-auth and botocore installed
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth


if __name__ == '__main__':
    # Configure AWS basics
    aws_region = 'us-east-1'
    aws_service = 'ec2'
    aws_endpoint = '{}.{}.amazonaws.com'.format(aws_service, aws_region)

    # Use Boto to automatically gather AWS credentials from environment variables, AWS config files, or IAM Role
    auth = BotoAWSRequestsAuth(aws_host=aws_endpoint,
                               aws_region=aws_region,
                               aws_service=aws_service)

    # Configure details of the API call
    api = 'DescribeVpcs'
    api_version = '2015-10-01'
    params = {'Action': api, 'Version': api_version}
    url = 'https://{}'.format(aws_endpoint)

    # Send a GET request
    response = requests.get(url=url, params=params, auth=auth)

    # Print response details
    print('Response code: {}'.format(response.status_code))
    print('Headers: {}'.format(response.headers))

    # Convert the response content from an encoded byte string to a Unicode string
    response_bytes = response.content
    response_str = response_bytes.decode()

    # If the respose is XML, ensure that it is nicely formatted with good indenting and newlines
    if response_str.startswith('<?xml'):
        import lxml.etree as etree

        response_bytes = etree.tostring(etree.fromstring(response.content), pretty_print=True)

    # Pretty-print the content of the response with syntax highlighting for readability
    highlighted_text = highlight(response_bytes, guess_lexer(response_str), TerminalFormatter())
    print(highlighted_text)
