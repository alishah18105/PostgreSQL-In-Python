# Create Student Management System Using PostgreSql In Python
import psycopg2
import functions as f

print("\n===========================================")
print("Welcome To DCS Student Management System")
print("===========================================\n")

mode = input("Are you a student or administor?\n(Enter 's' for student or 'a' for adminstrator ): ")

if mode.lower() == 'a':
    print("\n************************")
    print("Adminstrator Dashboard:")
    print("**************************")


    choice = int(input('''
Press 1: To Add Student Record:
Press 2: To Add Course Record:
Press 3: To Add Student Information Record: ''')) 
    
    if choice == 1:
        f.insert_Student_Record()

    elif choice == 2:
        f.insert_Course_Record()
        
    elif choice == 3:
        f.insert_Student_Info()
    else:
        print("Invalid input entered")


else:
    print("\n********************")
    print("Student Dashboard")
    print("********************")

    choice = int(input('''
Press 1: To View Semester Result:
Press 2: To View Any Course Record:
Press 3: To View All Courses Details: ''')) 
    
    if choice == 1:
        seat_number = input("Enter your seat number: ")
        semester = input("Enter the semester: ")
        student_detail = f.get_Specific_Student_Details(seat_number)
        records = f.get_Specific_Student_Record(seat_number,semester)
        
        print("\n==================================================================")
        print(f"\nName: {student_detail[1]}\t Father Name: {student_detail[2]}")
        print(f"Seat No: {student_detail[3]}\t Program: {student_detail[4]}")
        print(f"Semester: {semester}")

        print("\n{:^13} | {:^15} | {:^13} |{:^14} |{:^14} |".format("Course No", "Credit Hours", "Obtained Marks", "Grade","GP"))
        print("-"*85)
        for record in records:
            grade,gp = f.calculate_grading_point(record[2])
            print("{:^13} | {:^15} | {:^14} | {:^13} | {:^13} |".format(record[0], record[1], record[2],grade,round((gp*int(record[1])),1)))
        print("-"*85)



    elif choice == 2:
        course_no = input("\nEnter the course no: ")
        course_record = f.get_Specific_Course_Details(course_no)
        print("\n{:<12} | {:<60} | {:<13} |".format("Course No", "Course Title", "Credit Hours"))
        print("-" * 90)  
        print("{:<12} | {:<60} | {:^13} |".format(course_record[1], course_record[2], course_record[3]))
    elif choice == 3:
        course_records = f.get_All_Course_Details()

        print("\n{:<12} | {:<60} | {:<13} |".format("Course No", "Course Title", "Credit Hours"))
        print("-" * 93)  
        for course_record in course_records:
            print("{:<12} | {:<60} | {:^13} |".format(course_record[1], course_record[2], course_record[3]))
        
    else:
        print("Invalid input entered")

    

