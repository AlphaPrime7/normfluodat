'''
    Lists DBF files in the provided directory.
        
    Parameters
    ----------
    dir: str
        The directory pointing to dbf files.
        
    Returns
    -------
    list
        Actually returns a list or tuple of with the names of dbf files.
    
    Notes
    -----
    This function simply lists dbf files within the supplied directory and all subdirectories.
    
    Examples
    --------
    ``` {python}
    find_dbfs("C:/Users/Username/Documents") #replace Username with the user-specific name.
    find_dbfs("C:/Users/GrandProf/Documents") #specific to me
    ```
'''
import os
from pathlib import Path
from typing import Optional

def find_dbfs(dir: Optional[str] = None):

    if dir is None:
        dir = os.path.dirname(__file__)
    else:
        dir = dir
    
    ext_paths = Path(dir).glob('**/*.dbf',)

    for path in ext_paths:
        print(path) 

