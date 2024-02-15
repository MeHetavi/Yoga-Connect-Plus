import psycopg2

conn=psycopg2.connect(database="YogaConnect+",host="localhost",user="postgres",password="tirth",port="5432")
cur=conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS LOGIN (username VARCHAR(400) UNIQUE,email VARCHAR(400) PRIMARY KEY,password VARCHAR(11),gender VARCHAR(10),age INT,type VARCHAR(40))''')


conn.commit()
cur.close()
conn.close()