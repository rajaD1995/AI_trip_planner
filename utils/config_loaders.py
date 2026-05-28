import yaml
import os

# Loading the yaml file in configer.yaml
def load_config(config_path: str ="config/configer.yaml")->dict:
    with open(config_path,"r") as f:
        config = yaml.safe_load(f)
    
    return config