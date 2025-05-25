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