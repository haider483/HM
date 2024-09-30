import os #This module helps interact with your operating system (OS), such as working with files and directories.
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')
# logging.basicConfig: This line configures the logging system to display messages of INFO level or higher (more serious) in a specific format.
# level=logging.INFO: Sets the logging level to INFO. Any messages logged as INFO, WARNING, ERROR, or CRITICAL will be shown.
# format='[%(asctime)s]:%(message)s': Sets the format of the message. It will include a timestamp (asctime) and the actual log message.
list_of_files = [
    "src\\__init__.py",
    "src\\helper.py",
    "src\\prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research\\trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
# for filepath in list_of_files:: This loop goes through each item in list_of_files one by one.
# filepath = Path(filepath): Converts the string path ("src\\helper.py") into a Path object. This makes it easier to manipulate paths and check if directories or files exist
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            logging.info(f"Creating empty file: {filepath}")  # Corrected here
    else:
        logging.info(f"{filename} already exists")
