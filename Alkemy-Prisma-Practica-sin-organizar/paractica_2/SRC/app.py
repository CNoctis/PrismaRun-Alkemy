from decouple import config

print('Host: {HOST} - User: {USER} - Password:{PASSWORD} - Db: {DATABASE_NAME}'.format(HOST=config('DATABASE_HOST'), USER=config('USERNAME'), PASSWORD=config('PASSWORD'), DATABASE_NAME= config('DATABASE_NAME')))

