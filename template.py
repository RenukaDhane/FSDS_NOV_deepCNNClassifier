from fileinput import filename
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s: ')

# print(Path("x/y/z.txt")) Path allows to gets OS specific paths irrespective of the path passed to it

package_name="deepClassifier"

list_of_files=[
    ".github/workflows/.gitkeep",    # empty folders do not go to repository ,so to avoid that we use gitkeep as placeholder to keep the folder structure in repo
    #F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.
    #The __init__.py files are required to make Python treat directories containing the file as python packages.
    # directories and packages become identifiable
    #mywords - initialize package or define it as package
    f"src/{package_name}/__init__.py", 
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "configs/config.yaml",
    #DVC introduces a mechanism to capture data pipelines — series of data processes that produce a final result.
    "dvc.yaml",
    #below contains training parameters
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    #Modern Python packages can contain a pyproject.toml file, first introduced in PEP 518 and later expanded in PEP 517, PEP 621 and PEP 660. 
    # This file contains build system requirements and information, which are used by pip to build the package.
    "pyproject.toml",
    #tox is a generic virtualenv management and test command line tool you can use for:
    # • checking that your package installs correctly with different Python versions and interpreters
    # • running your tests in each of the environments, configuring your test tool of choice
    # • acting as a frontend to Continuous Integration servers, greatly reducing boilerplate and merging CI and shellbased testing.
    # used for testing project locally
    "tox.ini",
    "research/trials.ipynb"
   
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    # if directory name is blank that means no need of creating that directory,create dir when dir name not blank
    if filedir!='':   
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for file :{filename}")
    
    #create empty file when path does not exist or file size is zero
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):   
        with open(filepath,"w") as f:
            pass# create an empty file
            logging.info(f"Creating empty file :{filepath}")

    else:
        logging.info(f"{filename} already exists")

    