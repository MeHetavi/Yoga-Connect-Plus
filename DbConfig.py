
import psycopg2

# Establish connection parameters
host = 'localhost'
database = 'YogaConnect+'
user = 'postgres'
password = 'hetu'

# Establish connection
try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )    
    
except psycopg2.Error as e:
    ...