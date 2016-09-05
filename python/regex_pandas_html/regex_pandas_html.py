#!/usr/bin/env python
"""
Example code for how to use regular expressions to parse lines from a file to see if they match
certain criteria and then to store data from those lines which are in a CSV-like fashion in a Pandas
DataFrame and finally to export that DataFrame as an HTML table.
"""

import re
import pandas as pd


MY_REGEX = r"/Node Roles/\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

def line_parser(text_line, regex, container):
    """ Parse a single line attempting to match a regex.
    If it matches, then add the line to a data structure.

    @param line : str - line to parse
    @param regex : str - regular expression to match to
    @param container : list - container to add matches to
    """
    if re.match(regex, text_line, 0):
        container.append(text_line)


def read_lines(fname):
    """ Read all lines in from a file and call a parser function for each line.

    @param fname : str - filename
    """
    content = None
    with open(fname) as file:
        content = file.readlines()
    return content


def convert_to_pandas_df(csv_lines, delim=',', column_names=None, drop=None, index=None):
    """ Converts a list of CSV strings to a Pandas DataFrame and returns that DataFrame.

    @param data : list[str] - list of CSV strings
    @param delim: str - delimitter character
    @param column_names : list[str] - column names
    @param drop : list[str] - column names to drop
    @param index : str - column name to use as the index for the DataFrame
    @return df : pd.DataFrame
    """
    # Turn the list of CSV strings into a data structure containing a list of lists
    data = [sub.strip().split(delim) for sub in csv_lines]

    # Create Pandas DataFrame from the matches
    df = pd.DataFrame(data, columns=column_names)

    # Drop any columns we don't care about
    if drop is not None:
        for col_name in drop:
            df.drop(col_name, axis=1, inplace=True)

    # Set Index if it was specified
    if index is not None:
        df.set_index('IP', inplace=True)

    # Convert any 'object' types to numberic ones, where possible
    df = df.convert_objects(convert_numeric=True)

    return df


if __name__ == '__main__':
    lines = read_lines('wm.txt')
    matched_lines = []
    for line in lines:
        line_parser(line, MY_REGEX, matched_lines)

    # Strip off the first character and any trailing whitespace
    matches = [match.strip()[1:] for match in matched_lines]

    nodes = convert_to_pandas_df(matches, delim='/',
                                 column_names=['DeleteMe', 'IP', 'Role', 'Subrole', 'Confidence'],
                                 drop=['DeleteMe'], index='IP')

    # Convert the Pandas DataFrame to an HTML Table
    html_table = nodes.to_html()

    # Save off the HTML table to an html file
    with open('mytable.html', 'w') as output_file:
        output_file.writelines(html_table)
