'''
    Mop data frame commas.
        
    Parameters
    ----------
    comma_df: pd.DataFrame
        A comma dirty data frame.
        
    Returns
    -------
    pd.DataFrame
        Returns mopped comma(s) data frame.

    Examples
    --------
    ``` {python}
    comma_df = pd.DataFrame({'col1': ['1,', '2,' , '3,'],
                   'col2': ['4,', '5,', '6,']})
    nocomma_df = comma_cleaner(comma_df)
    print(nocomma_df)
    ```
'''

import pandas as pd

def comma_cleaner(comma_df: pd.DataFrame) -> pd.DataFrame:
    cols_to_becleaned = list(comma_df.columns)
    comma_df[cols_to_becleaned] = comma_df[cols_to_becleaned].apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',', ''), errors='coerce'))

    return pd.DataFrame(comma_df)

#Intra-module comms
if __name__ == "__main__":
    comma_cleaner()