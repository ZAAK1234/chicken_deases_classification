import os
import sys

sys.path.append('F:\FAHIM\Data Science\y_ml_project\p2')
from src.chicken_deases_classification.exception import CustomException
from box.exceptions import BoxValueError
import yaml
from src.chicken_deases_classification import logger
import json
import joblib
import ensure
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

from src.chicken_deases_classification.exception import error_message_detail


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)  # Make sure to return the ConfigBox object
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
        :param path_to_directories:
        :param verbose:
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path_to_json: Path, data: dict):
    """
    save json data
    Args:
        path_to_json (Path):path line input
        data (dict): data to save
    """
    with open(path_to_json, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f'json file saved: {path_to_json}')


@ensure_annotations
def load_bin(path_to_bin: Path) -> Any:
    """
    load binary data
    Args:
         path_to_bin (Path):path line input
    Returns:
        Any: object stored in file
    """
    data = joblib.load(path_to_bin)
    logger.info(f'loaded binary data: {path_to_bin}')
    return data


@ensure_annotations
def get_size(path_to_file: Path) -> str:
    """
    get size of file in kb
    Args:
        path_to_file (Path):path line input
    Returns:
         str: size of file in kb

    """
    size_in_kb = round(os.path.getsize(path_to_file) / 1024, 2)
    return f"{size_in_kb} kb"


def decodeImage(imagestring, filename):
    imgdata = base64.b64decode(imagestring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(cropped_image_path):
    with open(cropped_image_path, 'rb') as f:
        return base64.b64encode(f.read())
