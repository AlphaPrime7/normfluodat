'''
    Append unique identifier attribute to a data frame.
        
    Parameters
    ----------
    df: nfd_df
        The directory pointing to dat files.
        
    Returns
    -------
    pd.DataFrame
        Returns a unique id data frame.

    
    Examples
    --------
    ``` {python}
    df = pd.DataFrame({'col1': [1, 2, 3],
                   'col2': ['a', 'b', 'c']})
    test_df = unique_identifier(df)
    print(test_df)
    ```
'''

def format_number(i):
    from decimal import Decimal
    return '%g' % (Decimal(str(i)))


import pandas as pd
from typing import NewType
nfd_df = NewType('nfd_df', pd.DataFrame)

def unique_identifier(df: nfd_df) -> pd.DataFrame:

    x = 0
    for i in range(df.shape[0]):
        x += 1
        df.loc[i, 'Cycle_Number'] = format_number(x)

    first_column = df.pop('Cycle_Number')
    df.insert(0, 'Cycle_Number', first_column)
    return df

if __name__ == '__main__':
    unique_identifier
