import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "admin123",
    dbname = "postgres"    
)

cursor = connection.cursor()


