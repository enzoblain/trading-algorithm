import os

from dotenv import load_dotenv

def get_from_env(var):
    load_dotenv()

    value = os.getenv(var)

    if not value:
        raise ValueError(f"{var} not found. Please set it in the .env file.")

    return value

def transform_dataframe_to_dict(dataframe):
    return dataframe.to_dict(orient='records')