#Insert Data In Table From User Input In Python
import psycopg2

def insert_student():
    print("Insert Student Record\n")
    name = input("Enter Student Name: ")
    seat_number = input("Enter Seat Number: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender (M/F):")



    cur.execute(''' INSERT INTO students (name, seat_number, age, gender)
            VALUES (%s, %s, %s, %s) 
            ''' , (name, seat_number, age, gender))
    conn.commit()


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
insert_student()
get_all_students()
cur.close()
conn.close()

