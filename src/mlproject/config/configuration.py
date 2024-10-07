import yaml

class Configuration:
    def __init__(self, config_file_path='config/config.yaml'):
        self.config_file_path = config_file_path
        self.config = self.read_yaml(config_file_path)

    def read_yaml(self, config_file_path):
        with open(config_file_path, 'r') as yaml_file:
            return yaml.safe_load(yaml_file)

    def get_config(self):
        return self.config
