import os
from dotenv import load_dotenv, find_dotenv
load_dotenv (find_dotenv())
print(os.getenv('POSTGRESQL_HOST'))
print(os.getenv('POSTGRESQL_PORT'))
print(os.getenv('POSTGRESQL_USER'))
print(os.getenv('POSTGRESQL_PASSWORD'))