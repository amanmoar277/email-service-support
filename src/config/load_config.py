import os
from dotenv import load_dotenv, find_dotenv
import logging

def initiate_env():
    """load environment
    """
    absolete_path = os.path.abspath(__file__)
    file_dir = os.path.dirname(absolete_path)
    env_path = os.path.join(file_dir, '..', '..', 'environment', ".env")
    load_dotenv(verbose=True, dotenv_path=env_path, override=True)

def validate_env():
    env = os.getenv("ENV")
    if not env:
        raise ValueError('ENV_NOT_FOUND')

    valid_env = ['local', 'development', 'production']

    if env in valid_env:
        return env

    raise ValueError(
        f"Invalid ENV, Expected one of {' | '.join(valid_env)}")

def assign_settings(settings: dict, config: dict) -> dict:
    for key in config:
        setting_val = os.getenv(key)
        setting_type = config[key]

        if setting_val is None:
            raise ValueError(f"Environment Setting Missing - {key}")

        if str(setting_val) == '0':
            setting_val = False
        elif str(setting_val) == '1':
            setting_val = True

        if setting_type == int:
            setting_val = int(setting_val)

        if setting_type == os.PathLike:
            setting_val = Path(setting_val)

        if setting_type == list:
            setting_val = setting_val.split(",")

        if not isinstance(setting_val, setting_type):
            raise ValueError(
                f"Type Mismatch for {key}, Expected {setting_type}")

        settings[key] = setting_val

    return settings

def app_settings(settings):
    config = {
        "ENV": str,
        "APP_NAME": str,
        "APP_PORT": int,
        "DEBUG": bool
    }

    return assign_settings(settings, config)

def db_settings(settings):
    config = {
        "MONGODB_URI": str,
        "MONGODB_NAME": str,
        "SECRET_KEY": str,
    }

    return assign_settings(settings, config)

def attach_settings():
    settings = {}

    # attach app related settings
    app_settings(settings)

    # attach DB related settings
    db_settings(settings)

    return settings

def load_settings():
    initiate_env()
    env = validate_env()

    settings = attach_settings()
    logging.info(
        f"-----------------Environment Detected: {env}-----------------------")

    return settings