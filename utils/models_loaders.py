# utils/model_loader.py - FIXED VERSION
import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loaders import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

load_dotenv()

class ConfigLoader:
    def __init__(self):
        # Load the yaml file from config_loader.py
        print("Loading config.....")
        self.config = load_config()
    
    def __getitem__(self, key):
        # Allows us to use config["key"] instead of config.config["key"]
        # This is syntactic sugar for cleaner code
        return self.config[key]
    
    def get_active_provider(self):
        """Read which provider to use from YAML"""
        return self.config["llm"]["active_model"]  # Reads active_model from YAML!

class ModelLoader(BaseModel):
    # moderl_provider: Literal["groq","openai"] ="groq"
    # Creates a hidden storage space for ConfigLoader that starts empty (None)
    # exclude=True hides this field when printing the object
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    # Automatically runs after __init__ - creates and stores ConfigLoader
    def model_post_init(self, __context: Any) -> None:
        self.config = ConfigLoader()

    # Allows custom data type (ConfigLoader) as a field in Pydantic model
    # 'Config' name is FIXED - Pydantic specifically looks for this inner class
    class Config:
        arbitrary_types_allowed = True
    
    # Main function to call the model
    def load_llm(self, model_provider: str = None):
        """
        Load LLM model.
        If model_provider not passed, read from YAML.
        """
        # If provider not specified, get from YAML
        if model_provider is None:
            model_provider = self.config.get_active_provider()  # Reads from YAML!
        
        print(f"Loading model from provider: {model_provider}")
        
        if model_provider == "groq":
            print("Loading LLM from Groq...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config["llm"]["groq"]["model_name"]  # From yaml file
            return ChatGroq(model=model_name, api_key=groq_api_key)
        
        elif model_provider == "openai":
            print("Loading LLM from OpenAI...")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config["llm"]["openai"]["model_name"]  # From yaml file
            return ChatOpenAI(model=model_name, api_key=openai_api_key)
        
        else:
            raise ValueError(f"Unknown provider: {model_provider}")