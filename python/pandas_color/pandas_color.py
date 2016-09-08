#!/usr/bin/env python
"""
Example code for how to colorize Pandas HTML table output.

Newer versions of Pandas (0.17.1 or newer) have a better way of doing this with Style.

But this is an example of how to do it using older verisons of Pandas.
"""
import numpy as np
import pandas as pd
import re
from IPython.display import HTML


def HTML_with_style(df, style=None, random_id=None):
    """ Apply HTML style to Pandas DataFrame.

    @param df : pd.DataFrame - DataFrame to apply HTML styling to
    @param style : str - HTML style to apply (if None, use blue)
    @param random_id : str - random id to use
    @return HTML object -
    """
    from IPython.display import HTML
    import numpy as np
    import re

    df_html = df.to_html()

    if random_id is None:
        random_id = 'id%d' % np.random.choice(np.arange(1000000))

    if style is None:
        style = """
        <style>
            table#{random_id} {{color: blue}}
        </style>
        """.format(random_id=random_id)
    else:
        new_style = []
        s = re.sub(r'</?style>', '', style).strip()
        for line in s.split('\n'):
                line = line.strip()
                if not re.match(r'^table', line):
                    line = re.sub(r'^', 'table ', line)
                new_style.append(line)
        new_style = ['<style>'] + new_style + ['</style>']

        style = re.sub(r'table(#\S+)?', 'table#%s' % random_id, '\n'.join(new_style))

    df_html = re.sub(r'<table', r'<table id=%s ' % random_id, df_html)

    return HTML(style + df_html)


if __name__ == '__main__':
    # Generate an example DataFrame
    arrays = [['Midland','Midland','Hereford','Hereford','Hobbs','Hobbs','Childress','Childress','Reese','Reese',
               'San Angelo','San Angelo'],['WRF','MOS','WRF','MOS','WRF','MOS','WRF','MOS','WRF','MOS','WRF','MOS']]
    tuples = list(zip(*arrays))
    index = pd.MultiIndex.from_tuples(tuples)
    df = pd.DataFrame(np.random.randn(12,4),index=arrays,columns=['00 UTC','06 UTC','12 UTC','18 UTC'])
    print(df)

    # Render the DataFrame as an HTML table
    df_html = df.to_html()

    # Generate a random identifier for the html table and style we are going to create.
    random_id = 'id%d' % np.random.choice(np.arange(1000000))

    # W need to be careful to specify that this style will only be for our table.
    df_html = re.sub(r'<table', r'<table id=%s ' % random_id, df_html)

    # And create a style tag. This is really up to you. I just added some hover effect.
    style = """
    <style>
        table#{random_id} tr:hover {{background-color: #f5f5f5}}
    </style>
    """.format(random_id=random_id)

    # Finally, display it
    HTML(style + df_html)
