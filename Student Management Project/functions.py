import psycopg2

conn = psycopg2.connect(
    dbname="Student_Management",
    user="postgres",
    password="ali",
    host="localhost",
    port="5432"
)

cur = conn.cursor()


def create_Student_Table():
    cur.execute(""" CREATE TABLE IF NOT EXISTS student (
            student_id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            father_name VARCHAR(50) NOT NULL,
            seat_number VARCHAR(50) UNIQUE NOT NULL,
            program VARCHAR(50) NOT NULL,
            gender CHAR(1) 
            );
            """)

    conn.commit()
    print("Student Table Created Successfully")

#--------------------------------------------------------------------------------------------------------

def create_Course_Table():
    cur.execute(""" CREATE TABLE IF NOT EXISTS course (
            course_id SERIAL PRIMARY KEY,
            course_no  VARCHAR(20) UNIQUE NOT NULL,
            course_name VARCHAR(100) NOT NULL,
            credit_hours INT NOT NULL
            );
            """)
    conn.commit()
    print("Course Table Created Successfully")

#--------------------------------------------------------------------------------------------------------


def create_Student_Info_Table():
    cur.execute(""" CREATE TABLE IF NOT EXISTS student_info (
            info_id SERIAL PRIMARY KEY,
            seat_number VARCHAR(50) REFERENCES student(seat_number),
            semester INT NOT NULL,
            course_no VARCHAR(20) REFERENCES course(course_no),
            marks INT NOT NULL
            );
            """)
    conn.commit()
    print("Student Info Table Created Successfully")


#--------------------------------------------------------------------------------------------------------

def insert_Student_Record():
    name = input("\nEnter student name: ")
    father_name = input("Enter student's father name: ")
    seat_number = input("Enter student's seat number: ")
    program = input("Enter student's degree program (BSCS/BSSE): ")
    gender = input("Enter students's gender (M/F): ")


    cur.execute(''' INSERT INTO student(name, father_name, seat_number,program,gender)
                VALUES
                (%s,%s,%s,%s,%s)
                ''',
                (name, father_name, seat_number,program,gender)
    )
    conn.commit()
    print("Student Information Has Been Added Successfully")
                
#--------------------------------------------------------------------------------------------------------

def insert_Course_Record():
    course_no = input("Enter the course number (eg. SE-451): ")
    course_name = input("Enter the course title: ")
    credit_hours = int(input("Enter the course's credit hours: "))

    cur.execute(''' INSERT INTO course (course_no,course_name, credit_hours)
                VALUES 
                (%s,%s,%s)
                '''
                , (course_no, course_name, credit_hours)
                )
    conn.commit()
    print("Course Information Inserted Successfully")

#--------------------------------------------------------------------------------------------------------
    
def insert_Student_Info():
    seat_number = input("\nEnter the student's seat number: ")
    semester = int(input("Enter the student's semester(eg: 1): "))
    records = get_Specific_Student_Record(seat_number,semester)

    if not records:
        for i in range(0,6):
            course_no = input("Enter the course_no you want to enter the marks of: ")
            marks = int(input(f"Enter the obtained marks of course {course_no}: "))
            cur.execute(''' INSERT INTO student_info(seat_number,semester,course_no,marks)
                VALUES
                (%s,%s,%s,%s)
                ''',(seat_number,semester,course_no,marks)
                )
            conn.commit()
    
    else:
        course_no = input("Enter the course_no you want to enter the marks of: ")
        existing_course = [record[0] for record in records]
        if course_no in existing_course:
            print("Record Already Exist...")
            choice = input("Do you want to update existing record? (Y/N): ")
            if choice.lower() == 'y':
                marks = int(input(f"Enter the obtained marks of course {course_no}: "))
                update_Student_Info(marks, seat_number,semester,course_no)
            else:
                return
        else:
            marks = int(input(f"Enter the obtained marks of course {course_no}: "))
        cur.execute(''' INSERT INTO student_info(seat_number,semester,course_no,marks)
            VALUES
            (%s,%s,%s,%s)
            ''',(seat_number,semester,course_no,marks)
            )
        conn.commit()

    print("Course Information Inserted Successfully")

#---------------------------------------------------------------------------------------------------------

def get_Specific_Student_Record(seat_num, sem):
    cur.execute(''' SELECT course_no, marks FROM student_info
                WHERE seat_number = %s AND semester = %s  
                ORDER BY course_no
            ''', (seat_num,sem)
            )
    rows = cur.fetchall() 
    return rows

#----------------------------------------------------------------------------------------------------------

def update_Student_Info(marks, seat_number, semester, course_no):
    cur.execute(''' UPDATE student_info 
                SET marks = %s
                WHERE seat_number = %s AND semester = %s AND course_no = %s
                 ''', (marks, seat_number, semester, course_no))
    conn.commit()
    
#-------------------------------------------------------------------------------------------------------------
def close_connection():
    cur.close()
    conn.close()
    print("Database connection closed.")

