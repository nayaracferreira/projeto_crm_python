import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "02211906",
    dbname = "postgres"    
)

cursor = connection.cursor()


