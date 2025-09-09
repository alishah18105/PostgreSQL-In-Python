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
    cur.execute(''' INSERT INTO student(name, father_name, seat_number,program,gender)
                VALUES
                ('Syed Ali Sultan','Syed Sultan Mehmood','B23110106065','BSSE','M'),
                ('Neha Rehan','Syed Muhammad Rehan Ahmed','B23110006131','BSCS','F'),
                ('Farheen Arshad','Arshad Ali','B23110106017','BSSE','F')
                '''
    )
    conn.commit()
    print("Student Information Has Been Added Successfully")
                
#--------------------------------------------------------------------------------------------------------

def insert_Course_Record():
    cur.execute(''' INSERT INTO course (course_no,course_name, credit_hours)
                VALUES 
                ('SE-351','Programming Fundamentals', 4),
                ('SE-353', 'Introduction To Information & Communication Technologies', 3),
                ('SE-355', 'Calculus and Analytical Geometry', 3),
                ('SE-357','Discrete Structure', 3),
                ('SE-359','Functional English', 3),
                ('SE-361','Ideology and Constitution of Pakistan', 2)
                '''
                )
    conn.commit()
    print("Course Information Inserted Successfully")

#--------------------------------------------------------------------------------------------------------
    
def insert_Student_Info():
    cur.execute(''' INSERT INTO student_info(seat_number,semester,course_no,marks)
                VALUES
                ('B23110106065',1,'SE-351',80),
                ('B23110106065',1,'SE-353',87),
                ('B23110106065',1,'SE-355',80),
                ('B23110106065',1,'SE-357',80),
                ('B23110106065',1,'SE-359',86),
                ('B23110106065',1,'SE-361',80)
                '''
                )
    conn.commit()
    print("Course Information Inserted Successfully")

def get_Specific_Student_Record():
    pass

def close_connection():
    cur.close()
    conn.close()
    print("Database connection closed.")

