import psycopg2
import psycopg2.extras

connection = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "admin123",
    dbname = "postgres"    
)

cursor = connection.cursor()


