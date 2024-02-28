"""This python function implements the env variables for API coniguration"""
from dotenv import dotenv_values
# .env file contains the necessary key values that need to be loaded for using models
config = dotenv_values('.env')