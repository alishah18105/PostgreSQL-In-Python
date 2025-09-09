# Create Student Management System Using PostgreSql In Python
import psycopg2
import functions as f

print("\nWelcome To DCS Student Management System")
print("========================================\n")

mode = input("Are you a student or administor?\n(Enter 's' for student or 'a' for adminstrator ): ")

if mode.lower() == 'a':
    print("\nAdminstrator Dashboard:")
    choice = int(input('''
Press 1: To Add Student Record:
Press 2: To Add Course Record:
Press 3: To Add Student Information Record: ''')) 


else:
    print("\nStudent Dashboard\n")


# f.insert_Course_Record()
#f.insert_Student_Record()
#f.insert_Student_Info()
