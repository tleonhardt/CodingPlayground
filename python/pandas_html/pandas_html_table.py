#!/usr/bin/env python
"""
Example of using custom formaters to format the data when converting a Pandas DataFrame to an
HTML table.
"""
import numpy as np
import pandas as pd

# Construct a Pandas DataFrame
df = pd.DataFrame([np.nan, np.pi, np.e], columns=['Number'], index=['A', 'B', 'C'], dtype=float)

def format_no_nan(val):
    """
    Return val as a formatted string, or an empty string if val is null/NaN.
    
    @param val - value from a Pandas DataFrame
    @return str - empty string if val is null or NaN, string version of val otherwise
    """
    if pd.notnull(val):
        return '{}'.format(val)
    return ''
    

# Convert to html
html_table = df.to_html(formatters={'Number': format_no_nan})

print(html_table)
