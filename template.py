import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "mlproject"

# Define the list of directories
list_of_dirs = [
    f"src/{project_name}/",
    f"src/{project_name}/components/",
    f"src/{project_name}/utils/",
    f"src/{project_name}/config/",
    f"src/{project_name}/entity/",
    "data/",
]

# List of files to create
list_of_files = [
    "requirements.txt",
    "README.md",
    ".gitignore",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_processing.py",  # Placeholder for data processing
    f"src/{project_name}/components/forecasting.py",     # Placeholder for forecasting
    f"src/{project_name}/components/model_evaluation.py", # Placeholder for model evaluation
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/logging.py",               # Logger setup
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",        # Placeholder for configuration settings
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",        # Placeholder for config entity
    f"src/{project_name}/main.py",                         # Main entry point
    f"src/app.py",                                        # Streamlit app
]

# Create directories
for dir_path in list_of_dirs:
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    logging.info(f"Creating directory: {dir_path}")

# Create files
for file_path in list_of_files:
    file_path = Path(file_path)
    if not file_path.exists():
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{file_path.name} already exists")