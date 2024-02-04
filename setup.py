import os
import click
import pathlib
from setuptools import setup,find_packages, Command
from typing import Any, List
from warnings import warn
from pathlib import Path

#Match the R version number
_VERSION = "1.5.2"

#My guess of minimum dependencies
INSTALL_REQUIRES = [
     "numpy",
     "pandas",
]

#The project root-a nice tool to know
PROJECT_ROOT = os.path.dirname(__file__)

#using that PROJECT_ROOT methodology from earlier
with open(os.path.join(PROJECT_ROOT, "README.md")) as file_:
    read_me = file_.read()

class CustomCommandClass(Command):

    description = "R like commands with python setuptools"

    user_options: List[Any] = [
        ('setwd=', 's', 'set working directory'),
        ('getwd=', 'g', 'get working directory'),
    ]

    def initialize_options(nofun, **kwargs):
        nofun.setwd = None
        nofun.getwd = None
        nofun.target_dir = None
    
    def finalize_options(nofun):
        pass

    def run(nofun):
        
        if nofun.target_dir is None:
            def getwd():
                os.getcwd()
                click.echo(f"The current working directory is , {os.getcwd()}")
            getwd()

        else:
            def setwd(target_dir):
                 dpath = pathlib.PureWindowsPath(target_dir).as_posix()
                 if not Path(dpath).exists(): #pathlib.PureWindowsPath(dpath).as_posix()
                     try:
                         new_path = os.makedirs(dpath, exist_ok= True)
                         new_path
                         click.echo(os.chdir( str(new_path)) )
                     except FileNotFoundError:
                         click.echo(f"Directory: {dpath} does not exist but will be created if possible")
                         raise SystemExit(0)
                     except NotADirectoryError:
                         click.echo(f"{dpath} is not a directory but will be created if possible")
                         raise SystemExit(0)
                     except PermissionError:
                         click.echo(f"You do not have permissions to change to {dpath}")
                         raise SystemExit(0)
                     click.echo()

                 else:
                     try:
                         os.chdir(str(dpath))
                         click.echo(os.chdir(str(dpath)))
                     except FileNotFoundError:
                         click.echo(f"Directory: {dpath} does not exist")
                         raise SystemExit(0)
                     except NotADirectoryError:
                         click.echo(f"{dpath} is not a directory")
                         raise SystemExit(0)
                     except PermissionError:
                         click.echo(f"You do not have permissions to change to {dpath}")
                         raise SystemExit(0)
                     click.echo()
            setwd()

setup(
    name = "normfluodat",
    version = _VERSION,
    author = "Tingwei Adeck",
    maintainer_email="awesome.tingwei@outlook.com",

    url='https://github.com/alphaprime7/normfluodbf',
    project_urls={
        "Bug Tracker": "https://github.com/alphaprime7/normfluodbf/issues",
    },
    keywords=['dat','dbf','liposomes', 'research','bioinformatics', 'science', 'FLUOStar','BMG LABTECH'],
    description="Cleans and Normalizes liposome flux assay DBF and DAT files from the FLUOStar Microplate Reader.",
    long_description=read_me,
    long_description_content_type="text/x-rst",

    license="MIT",

    platforms= ['Windows', 'Linux', 'MacOS'],
    python_requires='>=3.6',

    classifiers=[
        'Development Status :: 3 - Pre-Alpha',
        "Operating System :: OS Independent",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Linux :: Ubuntu",
        "Environment :: Local Environment",
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Topic :: STEM :: Quantitative",
        "Topic :: Bioinformatics",
        'Intended Audience :: Developers',
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
    ],

    cmdclass={
        'getwd': CustomCommandClass,
        'setwd': CustomCommandClass
    },

    install_requires= INSTALL_REQUIRES,
    packages=find_packages(where = "src/"),
    package_dir={'': 'src/'},

    #There will be dat data files
    include_package_data=True,
    package_data={'data-raw': ['dat1.dat']},

    test_suite = "tests",

    zip_safe = False

    
)
