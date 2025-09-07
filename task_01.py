#PostgreSQL connection using psycopg2 in Python
#QUERY to create a table named students
import psycopg2

conn = psycopg2.connect(
    dbname="PostgreSQL_In_Python",
    user="postgres",
    password="ali",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            seat_number VARCHAR(50),
            age INT,
           gender CHAR(1)
            );
            """)

conn.commit()
cur.close()
conn.close()