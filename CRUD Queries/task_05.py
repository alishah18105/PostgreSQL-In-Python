#Update Age Of Student In Table From User Input In Python

import psycopg2

def update_record():
    print("Update Student Age \n")
    seat_number = input("Enter Seat Number: ")
    age = int(input("Enter New Age: "))

    cur.execute(''' UPDATE students
                SET age = %s
                WHERE seat_number = %s
                ''', (age, seat_number))
    conn.commit()
    print("Record Updated Successfully\n")
    
def get_all_students():
    cur.execute(''' SELECT * FROM students;''')
    rows = cur.fetchall()
    print("List of students:")
    print("student_id | name | seat_number | gender")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]}| {row[3]}  | {row[4]} ")

conn = psycopg2.connect(
    dbname = "PostgreSQL_In_Python",
    user = "postgres",
    password = "ali",
    host = "localhost",
    port = "5432"
)

cur = conn.cursor()
update_record()
get_all_students()
cur.close()
conn.close()

