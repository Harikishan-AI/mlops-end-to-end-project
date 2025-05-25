import os
import yaml
from src.mlops_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a Config_box object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        Config_box: Content of the YAML file as a Config_box object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file read successfully from {path_to_yaml}")
            return ConfigBox(content)
    execpt BoxValueError as e:
        logger.error(f"Error parsing YAML file at {path_to_yaml}: {e}")
        raise ValueError(f"Invalid YAML format in {path_to_yaml}") from e
    except Exception as e:
        logger.error(f"Error reading YAML file at {path_to_yaml}: {e}")
        raise e

@ensure_annotations
def create_directories(paths: list):
    """
    Creates directories if they do not exist.
    
    Args:
        paths (list): List of directory paths to create.
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory created: {path}")

@ensure_annotations
def save_json(path: Path, data: Any):
    """
    Saves data to a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        data (Any): Data to be saved in JSON format.
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"Data saved to JSON file at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads data from a JSON file.
    
    Args:
        path (Path): Path to the JSON file.
        
    Returns:
        Any: Data loaded from the JSON file.
    """
    with open (path, 'r') as json_file:
        data = json.load(json_file)
        logger.info(f"Data loaded from JSON file at {path}")
        return ConfigBox(data)

@ensure_annotations
def save_bin(path: Path, data: Any):
    """
    Saves data to a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
        data (Any): Data to be saved in binary format.
    """
    joblib.dump(data, path)
    logger.info(f"Data saved to binary file at {path}")

@ensure_annotations
def job_lib_load(path: Path) -> Any:
    """
    Loads data from a binary file using joblib.
    
    Args:
        path (Path): Path to the binary file.
        
    Returns:
        Any: Data loaded from the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Data loaded from binary file at {path}")
    return data