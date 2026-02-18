import json
from student_edited import Student
from programme import Programme

# A list to hold all student objects
all_students = []

# A list to hold all programme objects
all_programmes = []

def get_predefined_programmes():
    """Returns a list of predefined programmes with default cut-off points.
    
    Returns:
        list: A list of Programme objects with common university programmes.
    """
    return [
        Programme("Computer Science", 6),
        Programme("Medicine", 8),
        Programme("Engineering", 7),
        Programme("Business Administration", 10),
        Programme("Law", 9),
        Programme("Nursing", 12),
        Programme("Pharmacy", 7),
        Programme("Accounting", 11),
        Programme("Economics", 10),
        Programme("Mathematics", 8),
        Programme("Physics", 9),
        Programme("Chemistry", 8),
        Programme("Biology", 9),
        Programme("Psychology", 11),
        Programme("Sociology", 12),
        Programme("Political Science", 10),
        Programme("Journalism", 11),
        Programme("Education", 12),
        Programme("Agriculture", 13),
        Programme("Architecture", 7)
    ]

def load_programmes():
    """Loads programmes from programmes.json file. If file doesn't exist, 
    initializes with predefined programmes and creates the file.
    
    Returns:
        list: A list of Programme objects.
    """
    try:
        with open('programmes.json', 'r', encoding='utf-8') as f:
            programme_data = json.load(f)
            programmes = [Programme.from_dict(prog) for prog in programme_data]
            return programmes
    except FileNotFoundError:
        # Initialize with predefined programmes if file doesn't exist
        predefined = get_predefined_programmes()
        save_programmes(predefined)
        return predefined
    except json.JSONDecodeError:
        # If JSON is corrupted, use predefined programmes
        predefined = get_predefined_programmes()
        save_programmes(predefined)
        return predefined

def save_programmes(programmes):
    """Saves a list of programmes to programmes.json file.
    
    Args:
        programmes (list): A list of Programme objects to save.
    """
    programme_data = [prog.to_dict() for prog in programmes]
    with open('programmes.json', 'w', encoding='utf-8') as f:
        json.dump(programme_data, f, indent=4)

def add_programme():
    """Prompts the user to add a new programme with its cut-off point."""
    name = input("Enter programme name: ").strip()
    if not name:
        print("Programme name cannot be empty.")
        return
    
    # Check if programme already exists
    for prog in all_programmes:
        if prog.name.lower() == name.lower():
            print(f"Programme '{name}' already exists.")
            return
    
    while True:
        try:
            cutoff = float(input("Enter cut-off point: "))
            if cutoff < 0:
                print("Cut-off point cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    new_programme = Programme(name, cutoff)
    all_programmes.append(new_programme)
    save_programmes(all_programmes)
    print(f"Programme '{name}' with cut-off point {cutoff} added successfully.")

def list_programmes():
    """Displays all available programmes with their cut-off points."""
    if not all_programmes:
        print("No programmes available.")
        return
    
    print("\n" + "="*50)
    print("AVAILABLE PROGRAMMES")
    print("="*50)
    for i, prog in enumerate(all_programmes, 1):
        print(f"{i}. {prog.name} - Cut-off: {prog.cutoff_point}")
    print("="*50 + "\n")

def get_programme_by_name(name):
    """Finds a programme by its name (case-insensitive).
    
    Args:
        name (str): The name of the programme to find.
        
    Returns:
        Programme or None: The Programme object if found, None otherwise.
    """
    for prog in all_programmes:
        if prog.name.lower() == name.lower():
            return prog
    return None

def save_students():
    """Saves all student data to the students.json file."""
    student_data = []
    for st in all_students:
        student_data.append({
            "id": st.id,
            "firstname": st.firstname,
            "surname": st.surname,
            "other_names": st.other_names,
            "dob": st.dob,
            "school": st.school,
            "phone_number": st.phone_number,
            "course": st.course,
            "elective_option": st.elective_option,
            "results": st.results,
            "selected_programmes": st.selected_programmes
        })
    with open('students.json', 'w', encoding='utf-8') as f:
        json.dump(student_data, f, indent=4)

def add_student(stud_id):
    """Creates a new student, records their details and course information, 
    and adds them to the list of all students."""
    new_student = Student(stud_id)
    new_student.record_student_details()
    new_student.record_user_course()
    all_students.append(new_student)
    save_students()

# On script startup, load existing programme data
all_programmes = load_programmes()

# On script startup, load existing student data from the students.json file
try:
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
            # Load selected_programmes if it exists (for backward compatibility)
            if 'selected_programmes' in record:
                student.selected_programmes = record['selected_programmes']
            else:
                student.selected_programmes = []
            all_students.append(student)
except FileNotFoundError:
    # If students.json doesn't exist, start with empty list
    pass
except json.JSONDecodeError:
    # If JSON is corrupted, start with empty list
    pass

def admin():
    """Displays the main administrative menu for managing student data.
    This function acts as the main loop of the application."""
    while True:
        print("ADMIN\nWhat do you want to do:")
        print("1. Add a new student\n" \
              "2. Print a student's details\n" \
              "3. Print a student's results\n" \
              "4. Get a student's age\n" \
              "5. Get a student's date of birth in a different format\n" \
              "6. Get a student's aggregate\n" \
              "7. View all programmes\n" \
              "8. Add new programme\n" \
              "9. Student programme selection\n" \
              "0. Exit")

        num = int(input("option: "))

        # Add a new student
        if num == 1:
            stud_id = input("Student ID: ")
            add_student(stud_id)
        # Print a student's details
        elif num == 2:
            stud_id = input("Student ID: ")
            found = False
            for st in all_students:
                if st.id == stud_id:
                    st.print_student_details()
                    found = True
                    break
            if not found:
                print("no such student")
        # Print a student's results
        elif num == 3:
            stud_id = input("Student ID: ")
            found = False
            for st in all_students:
                if st.id == stud_id:
                    st.get_user_results()
                    found = True
                    break
            if not found:
                print("no such student")
        # Get a student's age
        elif num == 4:
            stud_id = input("Student ID: ")
            found = False
            for st in all_students:
                if st.id == stud_id:
                    print(f"{st.get_fullname()}\nAge: {st.get_age()}")
                    found = True
                    break
            if not found:
                print("no such student")
        # Get a student's date of birth in a different format
        elif num == 5:
            stud_id = input("Student ID: ")
            found = False
            for st in all_students:
                if st.id == stud_id:
                    print(st.fix_dob())
                    found = True
                    break
            if not found:
                print("no such student")
        elif num == 6:
            stud_id = input("Student ID: ")
            found = False
            for st in all_students:
                if st.id == stud_id:
                    print(f"Aggregate: {st.calc_student_aggr()}")
                    found = True
                    break
            if not found:
                print("no such student")
        # View all programmes
        elif num == 7:
            list_programmes()
        # Add new programme
        elif num == 8:
            add_programme()
        # Student programme selection
        elif num == 9:
            stud_id = input("Student ID: ")
            found = False
            for st in all_students:
                if st.id == stud_id:
                    st.select_programmes(all_programmes)
                    save_students()
                    found = True
                    break
            if not found:
                print("no such student")
        # Exit the application
        elif num == 0:
            print("Exiting...")
            save_students()  # Save all student data before exiting
            break  # Exit the while loop and end the application
        # Handle invalid input
        else:
            print("invalid")

# Start the administrative interface
admin()
