# import os
# from pathlib import Path
# import logging

# logging.basicConfig(level = logging.INFO, format ='[%(asctime)]:%(message)s:')

# project_name = "textSummarizer"



# #Below are files that will we will need to create in our project
# list_of_file = [
#     ".github/workflows/.gitkeep", # will write here CICD file , YML file
#     f"src/{project_name}/__init__.py",
#     f"src/{project_name}/components/__init__.py",
#     f"src/{project_name}/utils/__init__.py",
#     f"src/{project_name}/utils/common.py",
#     f"src/{project_name}/logging/__init__.py",
#     f"src/{project_name}/config/__init__.py",
#     f"src/{project_name}/config/configuration.py",
#     f"src/{project_name}/pipeline/__init__.py",
#     f"src/{project_name}/entity/__init__.py",
#     f"src/{project_name}/constant/__init__.py",
#     "config/config.yaml",
#     "params.yaml",
#     "app.py",
#     "main.py",
#     "Dockerfile",
#     "requirements.txt",
#     "setup.py",
#     "research/trials.ipynb"
# ]

# for file in list_of_file:
#     filepath = Path(file)
#     filedir, filename = os.path.split(filepath)
    
#     if filedir != "":
#         os.makedirs(filedir, exist_ok = True) 
#         logging.info(f"creating directory:{filedir} for the file {filename}")   
        
        
    
#     if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):
#         with open(filepath, 'w') as f:
#             pass
#             logging.info(f"creating empty file: {filepath}")
        
#     else:
#         logging.info(f"file: {filename} is already exists")
        
import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "textSummarizer"

# List of necessary files
list_of_files = [
    ".github/workflows/.gitkeep",  # CI/CD files (YML)
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    
]

for file_path in list_of_files:
    filepath = Path(file_path)
    filedir = filepath.parent  # Get the directory name
    
    try:
        # Create directory if it does not exist
        if filedir and not filedir.exists():
            filedir.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {filedir}")
        
        # Create empty file if it does not exist or is empty
        if not filepath.exists() or filepath.stat().st_size == 0:
            filepath.touch()
            logging.info(f"Created empty file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")
    except Exception as e:
        logging.error(f"Error creating {filepath}: {e}")
    