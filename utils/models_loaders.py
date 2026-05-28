from pydantic import BaseModel
import os
from utils.config_loaders import load_config


# to load the yaml file from the config_loader.py
class configloader:
    def __init__(self):
        self.config = load_config()  # As a dict the yaml file will be loaded here

class modelloader:
    def __init__(self):
        pass 
