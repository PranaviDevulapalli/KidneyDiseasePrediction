# Module is a single python file that contains code for reuse
# Library is the collection of modules at one place
# OS module provides functions to interact with the operating system- it helps you create,delete and modify files or directories
#OS is a part of python Standard library
#Why cant we just use OS module and why do we have to use pathlib?
# In OS- everything is handled in strings. We cannot use /\ for the dealing with the paths. Hence we use PathLib
# Logging- It is a way to track events that happen when some software runs. The events can be tracked in a log file or console. It tells you where the program is going or  what went wrong

import os  # This module 
from pathlib import Path
import logging
# This helps me to print the actions you are doing instead of printing every statement of what you are doing
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')
#basicConfig()- setup the defaultbehaviour of the logging system.
#level- It tells the logging module to handle all the messages at this level and above. There are 5 levels of the logging- DEBUG,INFO,WARNING.ERROR AND CRITICAL. Thos level=logging.INFO gives every other info except the debug thingy.
#format- It tells the logging module how to display the log messages. Here we are displaying the time and the message.
# [%(asctime)s]- the time when the log message was created. [%(message)s]- the actual message that should be displayed.
project_name='cnnClassifier'# You will have to use this name everywhere
list_of_files=[
    ".github/workflows/.gitkeep",# This is to keep the github workflow folder in the repo even if it is empty
    f"src/{project_name}/__init__.py",# This is to make this folder a package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/config.yaml",# This is the config file where you will store all the configurations
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",# This is the config file where you will store all the configurations
    "dvc.yaml",# This is the dvc file which contains all the stages of the pipeline
    "params.yaml",# This is the params file where you will store all the parameters
    "requirements.txt",# This file contains all the dependencies of the project
    "setup.py",# This file is used to install the package
    "research/trials.ipynb",
    # This is the notebook where you will do all your experiments
     "templates/index.html"
    # This is the template file where you will store all the html templates
     


]
for filepath in list_of_files:
    filepath=Path(filepath)# Converting the string path to Path object
    # Usually windows does not understand forward slash in path and hence we use Pathlib to convert it to the correct format
    filedir,filename=os.path.split(filepath)# Splitting the path into directory and filename
# For eg: f"src/{project_name}/utils/__init__.py",it seperates it into f"src/{project_name}/utils/" and "__init__.py"
    if filedir!="":# If the directory is not empty
        os.makedirs(filedir,exist_ok=True)# This will create all the intermediate directories if they do not exist. exist_ok=True means if the directory already exists, do not raise an error
        logging.info(f"Creating directory:{filedir} for the file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):# If the file does not exist or the file is empty
        with open (filepath,'w') as fp:# Creating a new file in write mode
            pass# Just to create an empty file
            logging.info(f"Creating new file:{filepath}")
    else:
        logging.info(f"File already exists:{filepath}")