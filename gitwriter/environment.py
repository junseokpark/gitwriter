import os
import sys
import configparser
from openai import OpenAI, APIConnectionError, AuthenticationError

CONFIG_PATH = os.path.expanduser('~/.gitwriter/environment.ini')
MODELS_PATH = os.path.expanduser('~/.gitwriter/models.ini')


def ensure_environment():
    if not os.path.exists(CONFIG_PATH):
        print("Environment not set up. Please run 'gitwriter setup'.")
        sys.exit(1)


def load_models():
    if not os.path.exists(MODELS_PATH):
        print("Models configuration file not found. Please create 'models.ini' in ~/.gitwriter/")
        sys.exit(1)

    models_config = configparser.ConfigParser()
    models_config.read(MODELS_PATH)
    return models_config


def setup_environment():
    config = configparser.ConfigParser()
    models_config = load_models()

    print("Step 1: Choose API Type")
    api_type = input("Select API type (External API / Local API): ").strip()

    if api_type.lower() in models_config:
        models = models_config[api_type.lower()].get('models', '').split(',')
    else:
        print("Invalid API type.")
        sys.exit(1)

    print(f"Step 2: Choose Model: {', '.join(models)}")
    model = input("Select model: ").strip()
    if model not in models:
        print("Invalid model selection.")
        sys.exit(1)

    print("Step 3: Provide API Key or Local Address")
    if api_type.lower() == "external api":
        api_key = input("Enter API key: ").strip()
        config['API'] = {'TYPE': api_type, 'MODEL': model, 'API_KEY': api_key}
    else:
        api_address = input("Enter API address (format: address:port): ").strip()
        config['API'] = {'TYPE': api_type, 'MODEL': model, 'API_ADDRESS': api_address}

    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, 'w') as configfile:
        config.write(configfile)

    print("Environment setup complete.")


def load_environment():
    ensure_environment()
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    return config['API']

def test_environment():
    env = load_environment()
    if env['TYPE'].lower() == "external api":
        try:
            client = OpenAI(api_key=env['API_KEY'])
            response = client.models.list()
            print("External API connection successful.")
        except (AuthenticationError, APIConnectionError) as e:
            print(f"API connection failed: {e}")
    else:
        print(f"Testing local API at {env['API_ADDRESS']} - (Implement your local test logic)")
