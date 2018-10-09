import os

def hello(event, context):
    return os.environ["SAMPLE_ENV_VAR"]
