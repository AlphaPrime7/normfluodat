'''
    Lists DAT files in the provided directory.
        
    Parameters
    ----------
    dir: str
        The directory pointing to dat files.
        
    Returns
    -------
    list
        Actually returns a list or tuple of with the names of dat files.
    
    Notes
    -----
    This function simply lists dat files within the supplied directory.
    
    Examples
    --------
    ``` {python}
    find_dats("C:/Users/Username/Documents") #replace Username with the user-specific name.
    find_dats("C:/Users/GrandProf/Documents") 
    ```
'''
import os
from pathlib import Path
from typing import Optional

def find_dats(dir: Optional[str] = None):

    if dir is None:
        dir = os.path.dirname(__file__)
    else:
        dir = dir
    
    ext_paths = Path(dir).glob('**/*.dat',)

    for path in ext_paths:
        print(path) 
