import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "Sign Language Detection"

list_of_files = [

    "data/.gitkeep"
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_pusher.py",
    f"src/{project_name}/configurations/__init__.py",
    f"src/{project_name}/configurations/s3_operation.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/main_utils.py"
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/artifacts_entity.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/training_pipeline/__init__.py",
    f"src/{project_name}/constants/application.py",
    f"src/{project_name}/exceptions/__init__.py",
    f"src/{project_name}/logger/__init__.py",


    "template/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir!= "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file ; {filepath}")
    
    else:
        logging.info(f"{filename} already exist")
