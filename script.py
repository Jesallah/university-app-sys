from student_edited import Student
import json

# A list to hold all student objects
all_students = []

def add_student(stud_id):
    """Creates a new student, records their details and course information, 
    and adds them to the list of all students."""
    new_student = Student(stud_id)
    new_student.record_student_details()
    new_student.record_user_course()
    all_students.append(new_student)

# On script startup, load existing student data from the students.json file
with open('students.json', 'r', encoding='utf-8') as f:
    student_data = json.load(f)
    # For each student record in the JSON file, create a Student object
    for record in student_data:
        student = Student(record['id'])
        student.firstname = record['firstname']
        student.surname = record['surname']
        student.other_names = record['other_names']
        student.dob = record['dob']
        student.school = record['school']
        student.phone_number = record['phone_number']
        student.course = record['course']
        student.elective_option = record['elective_option']
        student.results = record['results']
        all_students.append(student)

def admin():
    """Displays the main administrative menu for managing student data.
    This function acts as the main loop of the application."""
    print("ADMIN\nWhat do you want to do:")
    print("1. Add a new student\n" \
          "2. Print a student's details\n" \
          "3. Print a student's results\n" \
          "4. Get a student's age\n" \
          "5. Get a student's date of birth in a different format\n" \
          "0. Exit")

    num = int(input("option: "))

    # Add a new student
    if num == 1:
        stud_id = input("Student ID: ")
        add_student(stud_id)
        admin()
    # Print a student's details
    elif num == 2:
        stud_id = input("Student ID: ")
        for st in all_students:
            if st.id == stud_id:
                st.print_student_details()
        print("no such student")
        admin()
    # Print a student's results
    elif num == 3:
        stud_id = input("Student ID: ")
        for st in all_students:
            if st.id == stud_id:
                st.get_user_results()
        print("no such student")
        admin()
    # Get a student's age
    elif num == 4:
        stud_id = input("Student ID: ")
        for st in all_students:
            if st.id == stud_id:
                print(f"{st.get_fullname()}\nAge: {st.get_age()}")
        admin()
    # Get a student's date of birth in a different format
    elif num == 5:
        stud_id = input("Student ID: ")
        for st in all_students:
            if st.id == stud_id:
                print(st.fix_dob())
        admin() # Go back to admin menu
    elif num == 6:
        stud_id = input("Student ID: ")
        for st in all_students:
            if st.id == stud_id:
                print(f"Aggregate: {st.calc_student_aggr()}")
        admin() # Go back to admin menu
    # Exit the application
    elif num == 0:
        print("Exiting...")
        # # Save all student data to the JSON file before exiting
        # student_data = []
        # for st in all_students:
        #     student_data.append({
        #         "id": st.id,
        #         "firstname": st.firstname,
        #         "surname": st.surname,
        #         "other_names": st.other_names,
        #         "dob": st.dob,
        #         "school": st.school,
        #         "phone_number": st.phone_number,
        #         "course": st.course,
        #         "elective_option": st.elective_option,
        #         "results": st.results
        #     })
        # with open('students.json', 'w', encoding='utf-8') as f:
        #     json.dump(student_data, f, indent=4)
        # return  # Exit the admin function and end the application
    # Handle invalid input
    else:
        print("invalid")
        admin()

# Start the administrative interface
admin()
