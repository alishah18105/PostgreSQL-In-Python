#PostgreSQL Using psycopg2 in Python
#QUERY to insert multiple records into the students table

import psycopg2

conn = psycopg2.connect(
    dbname = "PostgreSQL_In_Python",
    user = "postgres",
    password = "ali",
    host = "localhost",
)

cur = conn.cursor()
cur.execute(""" INSERT INTO students (name, seat_number, age, gender)
            VALUES
            ('Ali Sultan', 'B23110106065', 20, 'M'), 
            ('Neha Rehan', 'B23110006131',20,'F'),
            ('Mustafa Akhlaq','B23110106050', 22, 'M'),
            ('Abdullah Imran','B23110106029', 20, 'M'),
            ('Ayesha Ehtisham','B23110106014',19,'F'),
            ('Farheen Arshad','B23110106017', 21, 'F')
            """)
conn.commit()
cur.close()
conn.close()