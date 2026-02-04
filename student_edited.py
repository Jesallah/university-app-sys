from datetime import date, datetime
from pprint import pprint

class Student:
    """Represents a student in the university application system."""

    def __init__(self, stud_id):
        """Initializes a new Student object.

        Args:
            stud_id (str): The unique ID for the student.
        """
        self.id = stud_id
        self.firstname = ""
        self.surname = ""
        self.other_names = ""
        self.dob = ""
        self.school = ""
        self.phone_number = ""
        self.course = ""
        self.elective_option = ""
        self.results = {}
        self.fixed_dob = None

    def record_student_details(self):
        """Prompts the user to enter their personal and school details."""
        print("-"*5 + "Personal Details" + "-"*5)
        self.firstname = input("Enter your first name: ")
        self.surname = input("Enter your surname: ")
        self.other_names = input("Enter your other names in the correct order (leave this blank if you have none): ")
        self.dob = input("Enter your date of birth(dd/mm/yy): ").split('/')
        self.phone_number = input("Enter your phone number: ")
        print("-"*5 + "School Details" + "-"*5)
        self.school = input("Enter the name of the school you attended: ")

    def get_age(self):
        """Calculates the student's age based on their date of birth.

        Returns:
            int: The student's age.
        """
        today = date.today()
        # Assuming self.dob is in format [dd, mm, yy]
        birth_year = int(self.dob[-1])
        # Convert 2-digit year to 4-digit year
        full_birth_year = 2000 + birth_year if birth_year <= (today.year % 100) else 1900 + birth_year
        return today.year - full_birth_year

    def fix_dob(self):
        """Formats the student's date of birth into a more readable format.

        Returns:
            str: The formatted date of birth (e.g., "DD-MM-YYYY").
        """
        today = date.today()
        birth_year = int(self.dob[-1])
        # Convert 2-digit year to 4-digit year
        full_birth_year = 2000 + birth_year if birth_year <= (today.year % 100) else 1900 + birth_year
        self.fixed_dob = datetime(int(full_birth_year), int(self.dob[1]), int(self.dob[0]))
        return self.fixed_dob.strftime("%d-%m-%Y")

    def get_fullname(self):
        """Constructs the student's full name.

        Returns:
            str: The student's full name.
        """
        return f"{self.firstname} {self.other_names} {self.surname}"

    def print_student_details(self):
        """Prints all the details of the student in a formatted way."""
        print(f"""\nStudent Details:
Student ID: {self.id}
Full name: {self.get_fullname()}
Date of Birth: {self.fix_dob()}
Age: {self.get_age()}
Phone number: {self.phone_number}
School: {self.school}
Course: {self.course}
Results:""")
        pprint(self.results, width=1, sort_dicts=False)

    def record_user_course(self):
        """Guides the user to select their course and elective options."""
        while True:
            print("What course did you study in school?")
            print("1. Science\n2. General Art\n3. Visual Art\n4. Business\n5. Agriculture")
            try:
                course = int(input("Select an option: "))
                if 0 < course < 6:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        course_map = {1: "Science", 2: "General Art", 3: "Visual Art", 4: "Business", 5: "Agric"}
        self.course = course_map.get(course)

        # Record elective options based on the chosen course
        if self.course == "Science":
            while True:
                print("Science with which course?\n" \
                "1. Biology\n2. Elective ICT\n3. Geography")
                try:
                    option = int(input("Select an option: "))
                    if 0 < option < 4:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elective_map = {1: "bio", 2: "eict", 3: "geo"}
            self.elective_option = elective_map.get(option)

        elif self.course == "General Art":
            while True:
                print("What combination of General Arts?\n"
                      "1. Econs/ Geography/ Elective Maths/ Government\n"
                      "2. Econs/ Geography/ Elective Maths/ Elective ICT\n"
                      "3. Econs/ Government/ Literature/ CRS")
                try:
                    option = int(input("Select an option: "))
                    if 0 < option < 4:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elective_map = {1: "op1", 2: "op2", 3: "op3"}
            self.elective_option = elective_map.get(option)

        elif self.course == "Visual Art":
            while True:
                print("What combination of Visual Art?\n"
                    "1. GKA/ Graphic Design/ Picture Making/ Sculpture\n" \
                    "2. GKA/ Ceramics/ Leatherwork/ Textiles")
                try:
                    option = int(input("Select an option: "))
                    if 0 < option < 3:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elective_map = {1: "op1", 2: "op2"}
            self.elective_option = elective_map.get(option)

        elif self.course == "Business":
            while True:
                print("Business with which course?\n"
                    "1. Elective Maths\n2. Cost Accounting")
                try:
                    option = int(input("Select an option: "))
                    if 0 < option < 3:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elective_map = {1: "emaths", 2: "c_a"}
            self.elective_option = elective_map.get(option)

        else:
            while True:
                print("Agric with which course?\n"
                    "1. Physics\n2. Animal Husbandry")
                try:
                    option = int(input("Select an option: "))
                    if 0 < option < 3:
                        break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elective_map = {1: "phy", 2: "anim"}
            self.elective_option = elective_map.get(option)

        # ... (similar logic for other courses)

        self.record_user_results()

    def record_user_results(self):
        """Records the student's results for core and elective subjects."""
        print("Enter your results:")
        print("-"*3 + "Core Subjects" + "-"*3)
        self.results["Core Math"] = input("Core mathematics: ")
        self.results["English"] = input("English Language: ")
        self.results["Social Studies"] = input("Social Studies: ")
        self.results["Integrated Science"] = input("Integrated Science: ")

        # Nested functions to handle results for different courses
        def science_student():
            print("\n" + "-"*3 + "Elective Subjects" + "-"*3)
            self.results["Physics"] = input("Physics: ")
            self.results["Chemistry"] = input("Chemistry: ")
            self.results["Elective Math"] = input("Elective Math: ")
            if self.elective_option == "bio":
                self.results["Biology"] = input("Biology: ")
            elif self.elective_option == "eict":
                self.results["Elective ICT"] = input("Elective ICT: ")
            elif self.elective_option == "geo":
                self.results["Geography"] = input("Geography: ")

        def general_art_student():
            print("\n" + "-"*3 + "Elective Subjects" + "-"*3)
            if self.elective_option == "op1":
                self.results["Economics"] = input("Economics: ")
                self.results["Geography"] = input("Geography: ")
                self.results["Elective Math"] = input("Elective Math: ")
                self.results["Government"] = input("Government: ")
            elif self.elective_option == "op2":
                self.results["Economics"] = input("Economics: ")
                self.results["Geography"] = input("Geography: ")
                self.results["Elective Math"] = input("Elective Math: ")
                self.results["Elective ICT"] = input("Elective ICT: ")
            elif self.elective_option == "op3":
                self.results["Economics"] = input("Economics: ")
                self.results["Government"] = input("Government: ")
                self.results["Literature"] = input("Literature: ")
                self.results["CRS"] = input("Christian Religious Studies(CRS): ")

        def visual_art_student():
            print("\n" + "-"*3 + "Elective Subjects" + "-"*3)
            if self.elective_option == "op1":
                self.results["General Knowledge in Art"] = input("General Knowledge in Art(GKA): ")
                self.results["Graphic Design"] = input("Graphic Design: ")
                self.results["Picture Making"] = input("Picture Making: ")
                self.results["Sculpting"] = input("Sculpting: ")
            elif self.elective_option == "op2":
                self.results["General Knowledge in Art"] = input("General Knowledge in Art(GKA): ")
                self.results["Ceramics"] = input("Ceramics: ")
                self.results["Textiles"] = input("Textiles: ")
                self.results["Leatherwork"] = input("Leatherwork: ")

        def business_student():
            print("\n" + "-"*3 + "Elective Subjects" + "-"*3)
            self.results["Economics"] = input("Economics: ")
            self.results["Business Management"] = input("Business Management: ")
            self.results["Financial Accounting"] = input("Financial Accounting: ")
            if self.elective_option == "emaths":
                self.results["Elective Math"] = input("Elective Math: ")
            elif self.elective_option == "c_a":
                self.results["Cost Accounting"] = input("Cost Accounting: ")

        def agric_student():
            print("\n" + "-"*3 + "Elective Subjects" + "-"*3)
            self.results["General Agric"] = input("General Agric: ")
            self.results["Chemistry"] = input("Chemistry: ")
            self.results["Elective Math"] = input("Elective Math: ")
            if self.elective_option == "phy":
                self.results["Physics"] = input("Physics: ")
            elif self.elective_option == "anim":
                self.results["Animal Husbandry"] = input("Animal Husbandry: ")

        # Call the appropriate nested function based on the student's course
        if self.course == "Science":
            science_student()
        elif self.course == "General Art":
            general_art_student()
        elif self.course == "Visual Art":
            visual_art_student()
        elif self.course == "Business":
            business_student()
        else:
            agric_student()

    def get_user_results(self):
        """Prints the student's ID, name, and their results."""
        print(f"\nStudent ID: {self.id}\nStudent name: {self.get_fullname()}")
        for key, value in self.results.items():
            print(f"{key}: {value}")