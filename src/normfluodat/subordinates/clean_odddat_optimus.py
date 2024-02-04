'''
    Clean the DAT (converted to .txt file).
        
    Parameters
    ----------
    dir: str
        A data frame derived from the imported .txt file.
        
    Returns
    -------
    Data frame
        Returns a clean data frame.
    
    Notes
    -----
    R to python function conversion achieved by CHATGPT 3.5
    
    Examples
    --------
    ``` {python}

    #RUN CODE
    dat = "C:/Users/GrandProf/Downloads/Repos_4cleanup/Repositories_AP7/Active/normfluodat/data-raw/dat_1.txt"
    df = pd.read_csv(dat, sep='\t', header=None)
    df = clean_odddat_optimus(df)
    df.to_csv('C:/Users/GrandProf/Downloads/Repos_4cleanup/Repositories_AP7/Active/normfluodat/data-raw/data.csv')
    df_head = df.head(20)
    df_tail = df.tail(20)
    print(df_head)
    print(df_tail)

    #TIMEIT
    import timeit
    
    dat = "C:/Users/GrandProf/Downloads/Repos_4cleanup/Repositories_AP7/Active/normfluodat/data-raw/dat_1.txt"
    df = pd.read_csv(dat, sep='\t', header=None)
    loop = 1000
    repeat = 2
    result = timeit.timeit('clean_odddat_optimus(df)', globals=globals(), number=loop)
    print(result/loop) #get single execution time
    
    print(timeit.timeit(lambda: clean_odddat_optimus(df), number = 10))
    print(timeit.repeat(lambda: clean_odddat_optimus(df), repeat=repeat, number=100))

    #TIMEIT IN JUPYTER
    dat = "C:/Users/GrandProf/Downloads/Repos_4cleanup/Repositories_AP7/Active/normfluodat/data-raw/dat_1.txt"
    df = pd.read_csv(dat, sep='\t', header=None)

    %timeit clean_odddat_optimus(df)
    %timeit -r 3 -n 10000 clean_odddat_optimus(df) #just a note %%timeit measures cell exec time
    ```
'''

import pandas as pd
import numpy as np
import timeit
import comma_cleaner as cc

def clean_odddat_optimus(df):
    special_chars = ['-,', '-']

    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            if any(char in str(df.iloc[i, j]) for char in special_chars):
                df.iloc[i, j] = np.nan
    nona_rows_df = df.dropna()

    if df.shape[1] == 1:
        comma_df = nona_rows_df
        comma_df = comma_df[~comma_df.isna().all(axis=1)]
        nocomma_df = pd.to_numeric(comma_df.iloc[:, 0].str.replace(",", ""), errors='coerce')
        num_rows = nocomma_df.shape[0] + 1
        nocomma_df.index = range(1, num_rows)
        return pd.DataFrame(nocomma_df)

    else:
        comma_df = nona_rows_df
        comma_df = comma_df[~comma_df.isna().all(axis=1)]
        nocomma_df = cc.comma_cleaner(comma_df)
        nocomma_df = pd.DataFrame(nocomma_df)
        num_rows = len(nocomma_df.index) + 1
        nocomma_df.index = range(1, num_rows)
        return nocomma_df
    
if __name__ == '__main__':
    clean_odddat_optimus