'''
    List all files in directory
        
    Parameters
    ----------
    dir: str
        
    Returns
    -------
    tuple or list

    Examples
    --------
    ``` {python}
    list_all_files('C:/...')
    ```
'''
import pathlib
from typing import Optional

def list_all_files(dir: Optional[str] = None):
    
    desktop = pathlib.Path(dir)
    desktop.iterdir()
    
    for item in desktop.iterdir():
        print(f"{item} - {'dir' if item.is_dir() else 'file'}")

if __name__ == '__main__':
    list_all_files