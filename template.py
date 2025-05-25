import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("template_manager.log"),
        logging.StreamHandler()
    ]
)

project_name = "mlops_project"

list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipliene/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constant/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "README.md",
    "app.py",
    "research/research.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    filepath = Path(file_path)
    filedir,filename = os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")
    
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath} and is not empty.")