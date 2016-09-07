#!/usr/bin/env python
"""
Example code for how to use regular expressions to parse lines from a file to see if they match
certain criteria and then to store data from those lines which are in a CSV-like fashion in a Pandas
DataFrame and finally to export that DataFrame as an HTML table.
"""

import re
import pandas as pd
import numpy as np


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


def csv_list_to_pandas_df(csv_lines, delim=',', column_names=None, drop=None, index=None):
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

def csv_row_to_pandas_series(csv_row, delim=',', index_names=None, name=None, drop=None):
    """ Converts a CSV string to a Pandas Series and returns that Series, which
    is suitable for appending to a Pandas DataFrame.

    @param csv_row : str - CSV strings
    @param delim: str - delimitter character
    @param index_names : list[str] - index names
    @param drop : list[str] - indexes to drop
    @param name : str - index to use for overall Series name (automatically dropped)
    @return pd.Series - Pandas Series containing contents of the CSV string
    """
    # Split the CSV strings into a list of strings, split at the delimiter
    csv_data = csv_row.strip().split(delim)

    # Create Pandas Series from the data
    csv_series = pd.Series(csv_data, index=index_names)

    # Drop the name index and set it as the overall series name
    series_name = csv_series[name]
    csv_series.drop(name, inplace=True)
    csv_series.name = series_name

    # Drop any columns we don't care about
    if drop is not None:
        for idx_name in drop:
            csv_series.drop(idx_name, inplace=True)

    # Convert any 'object' types to numberic ones, where possible
    csv_series = csv_series.convert_objects(convert_numeric=True)

    return csv_series


if __name__ == '__main__':
    lines = read_lines('wm.txt')
    matched_lines = []
    for line in lines:
        line_parser(line, MY_REGEX, matched_lines)

    # Strip off the first character and any trailing whitespace
    matches = [match.strip()[1:] for match in matched_lines]

    #----- Add all of the data to a DataFrame at once
    nodes = csv_list_to_pandas_df(matches, delim='/', drop=['DeleteMe'], index='IP',
                                  column_names=['DeleteMe', 'IP', 'Role', 'Subrole', 'Confidence'])

    # Convert the Pandas DataFrame to an HTML Table
    html_table = nodes.to_html()

    # Save off the HTML table to an html file
    with open('mytable.html', 'w') as output_file:
       output_file.writelines(html_table)


    #----- Now do the same thing, but do it 1 line at a time
    # Create an Empty Pandas DataFrame
    more_nodes = pd.DataFrame(columns=['Role', 'Subrole', 'Confidence'])
    more_nodes.index.name = 'IP'

    # Loop through each match, dealing with converting and adding 1 line at a time
    for match in matches:
        # Create a Pandas Series for the match
        series = csv_row_to_pandas_series(match, delim='/', name='IP', drop=['DeleteMe'],
                                          index_names=['DeleteMe', 'IP', 'Role', 'Subrole', 'Confidence'])
        # Set the value for this Series within the existing DataFrame
        more_nodes.loc[series.name] = series

    # Convert integer types so they aren't float
    more_nodes.Role = more_nodes.Role.astype(int)
    more_nodes.Subrole = more_nodes.Subrole.astype(int)

    print(more_nodes)
    print(more_nodes.dtypes)
