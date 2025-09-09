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
    print("********************\n")

    seat_number = input("Enter your seat number: ")
    semester = input("Enter the semester: ")
    student_detail = f.get_Specific_Student_Details(seat_number)
    records = f.get_Specific_Student_Record(seat_number,semester)
    
    print("\n==================================================================")
    print(f"\nName: {student_detail[1]}\t Father Name: {student_detail[2]}")
    print(f"Seat No: {student_detail[3]}\t Program: {student_detail[4]}")
    print(f"Semester: {semester}")

    print("\n|Course Number \t| Marks |")
    print("----------------------------")
    for record in records:
        print(f"|{record[0]} \t| {record[1]} \t|") 
    print("\n==================================================================")


