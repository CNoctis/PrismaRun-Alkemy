import os
from dotenv import load_dotenv, find_dotenv

load_dotenv (find_dotenv())

print('Host: {HOST} - User: {USER} - Password:{PASSWORD} - Db: {DATABASE_NAME}'.format(HOST=os.getenv('DATABASE_HOST'), USER=os.getenv('USERNAME'), PASSWORD=os.getenv('PASSWORD'), DATABASE_NAME= os.getenv('DATABASE_NAME')))