#!/usr/bin/env python
# coding=utf-8
"""Directly make HTTP calls to AWS service endpoints using the requsts and aws-requests-auth modules.

This is a generic example which can be easily modified to call AWS APIs and/or services and is effectively
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
    * XML toolkit for Python (used to ensure pretty XML formatting, even for error responses)
    * https://github.com/lxml/lxml
- pygments
    * Pygments is a generic syntax highlighter that supports 300 languages including JSON, XML, HTML, YAML, Java, etc.
    * http://pygments.org
"""
import argparse
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import TerminalFormatter
import requests


def main(argv=None):
    """Run when invoked from the command-line."""
    # Create an arparse argument parser for parsing command-line arguments
    desc = 'A command line HTTP client for AWS services with an intuitive UI, XML support and syntax highlighting.'
    epilog = 'See the AWS Documentation for API references for each service:  https://docs.aws.amazon.com'
    parser = argparse.ArgumentParser(description=desc, epilog=epilog, prog='http_aws')
    parser.add_argument('-r', '--region', help='The region to use. Overrides config/env settings.')
    parser.add_argument('-s', '--service', help='AWS service - e.g. ec2, s3, etc.', default='ec2')
    parser.add_argument('-e', '--endpoint', help="Override command's default URL with the given URL")
    parser.add_argument('-c', '--creds',
                        help="Override AWS Access Key Id and AWS Secret Access Key - i.e. <Access_Key>:<Secret_Key>")
    parser.add_argument('-v', '--version', help='API version to use', default='2015-10-01')
    parser.add_argument('api', help='Name of the API to call - e.g. "DescribeVpcs" (for ec2 service)')
    args = parser.parse_args(argv)

    # --- Configure AWS basics ---

    # Configure AWS region
    aws_region = 'us-east-1'    # Default if not overriden on command-line or specified in config file
    if args.region:
        aws_region = args.region
    else:
        import os
        # Read the region from the ~/.aws/config file if it exists
        try:
            with open(os.path.expanduser('~/.aws/config')) as f:
                data = f.read()
                lines = data.splitlines()
                for line in lines:
                    if line.startswith('region = '):
                        aws_region = line.split('region = ')[1]
        except (FileNotFoundError, PermissionError):
            pass

    # Configure AWS service
    if args.service:
        aws_service = args.service
    else:
        aws_service = 'ec2'  # Default if not overriden on command-line

    # Configure AWS endpoint
    if args.endpoint:
        aws_endpoint = args.endpoint
    else:
        aws_endpoint = '{}.{}.amazonaws.com'.format(aws_service, aws_region)

    if args.creds:
        from aws_requests_auth.aws_auth import AWSRequestsAuth
        # Use the specified AWS access and secret key
        access_key, secret_key = args.creds.split(':')
        auth = AWSRequestsAuth(aws_access_key=access_key,
                               aws_secret_access_key=secret_key,
                               aws_host=aws_endpoint,
                               aws_region=aws_region,
                               aws_service=aws_service)
    else:
        # This line will fail if you do not have both aws-requests-auth and botocore installed
        from aws_requests_auth.boto_utils import BotoAWSRequestsAuth
        # Use Boto to automatically gather AWS credentials from environment variables, AWS config files, or IAM Role
        auth = BotoAWSRequestsAuth(aws_host=aws_endpoint,
                                   aws_region=aws_region,
                                   aws_service=aws_service)

    # Configure details of the API call
    api = args.api
    api_version = args.version
    params = {'Action': api, 'Version': api_version}
    url = 'https://{}'.format(aws_endpoint)

    # Send a GET request
    response = requests.get(url=url, params=params, auth=auth)
    # TODO: Support PUT requests for Mutating API calls

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


if __name__ == '__main__':
    import sys
    sys.exit(main())
