import os 
from pathlib import Path
import logging
#logging configuration with time and date 
logging.basicConfig(level=logging.INFO, format='[%(asctime)s}]: %(message)s:')

list_of_files=[
    "src/_init_.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py", 
    "app.py",
    "research/trials.ipynb",
    "test.py"
]
#creating file directiory in one attempt 
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename= os.path.split(filepath)
    
    if filedir!= "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory; {filedir} for the file :{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath, "w") as f:
            pass
            logging.info(f"creating empty file:{filepath}")
    else:
        logging.info(f"{filename} is already exists")
        
        