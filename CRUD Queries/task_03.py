#PostgreSQL connection using psycopg2 in Python
#QUERY to Read all records from the students table & filer recordes based on gender

import psycopg2

conn = psycopg2.connect(
    dbname="PostgreSQL_In_Python",  
    user="postgres",
    password="ali",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

#QUERY to Read all records from the students table
cur.execute("SELECT * FROM students;")

rows = cur.fetchall()
print("List of students:")
print("student_id | name | seat_number | age | gender ")
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]}| {row[3]}  | {row[4]} ")

cur.execute(""" SELECT * FROM students WHERE gender = 'M';""")
rows = cur.fetchall()
print("\nList Of Students with gender \'M\':")
print("student_id | name | seat_number, age, gender")
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]}| {row[3]}  | {row[4]} ")

conn.commit()
cur.close()
conn.close()