import os
import json

def load_validation_input_config():
    with open('validation_input_config.json', 'r') as file:
        validation_input_config = json.load(file)
    return validation_input_config
