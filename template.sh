# creating folders
mkdir -p agent   # for entire agentic workflow
mkdir -p config
mkdir -p prompt_library
mkdir -p tools  # all the tools to connects agents to do all task
mkdir -p utils  # for any utility for any model or cloud
mkdir -p notebook

# Creating files
touch agent/__init__.py  # constructor. to make this folder a package
touch agent/agentic_workflow.py
touch config/__init__.py
touch config/config.yaml
touch prompt_library/__init__.py
touch prompt_library/prompt.py

touch tools/__init__.py
touch tools/currency_conversion_tool.py
touch tools/place_search.py
touch tools/weather_info_tool.py
touch tools/arthimatic_operation_tool.py
touch tools/calculator_tool.py

touch utils/__init__.py
touch utils/models_loaders.py
touch utils/config_loaders.py
touch utils/currency_converter.py
touch utils/calculator.py
touch utils/place_info_search.py
touch utils/save_to_document.py

touch .env
touch app.py # for front end like streamlit UI
touch main.py # to create end point with fast API
touch notebook/experiment.ipynb