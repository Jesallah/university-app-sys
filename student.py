from datetime import date, datetime
from pprint import pprint

class Student:
    def __init__(self, stud_id):
        self.id = stud_id
        self.firstname = ""
        self.surname = ""
        self. other_names = ""
        self.dob = ""
        self.school = ""
        self.phone_number = ""
        self.course = ""
        self.elective_option = ""
        self.results = {}

    def record_student_details(self):
        print("-"*5 + "Personal Details" + "-"*5)
        firstname = input("Enter your first name: ")
        surname = input("Enter your surname: ")
        other_names = input("Enter your other names in the correct order (leave this blank if you have none): ")
        dob = input("Enter your date of birth(dd/mm/yy): ")
        phone_number = input("Enter your phone number: ")
        print("-"*5 + "School Details" + "-"*5)
        school = input("Enter the name if the school you attended: ")
        # storing user data
        self.firstname = firstname
        self.surname = surname
        self. other_names = other_names
        self.dob = dob.split('/')
        # dob format = [dd,mm,yy]
        self.school = school
        self.phone_number = phone_number

    def get_age(self):
        today = date.today()
        # Assuming self.dob is in format "dd/mm/yy"
        birth_year = int(self.dob[-1])
        full_birth_year = 2000 + birth_year if birth_year <= (today.year % 100) else 1900 + birth_year
        return today.year - full_birth_year
    
    def fix_dob(self):
        today = date.today()
        birth_year = int(self.dob[-1])
        full_birth_year = 2000 + birth_year if birth_year <= (today.year % 100) else 1900 + birth_year
        self.fixed_dob = datetime(int(full_birth_year), int(self.dob[1]), int(self.dob[0]))
        return self.fixed_dob.strftime("%d-%m-%Y")

    def get_fullname(self):
        return f"{self.firstname} {self.other_names} {self.surname}"
    
    def print_student_details(self):
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
        while True:
            print("What course did you study in school?")
            print("1. Science\n2. General Art\n3. Visual Art\n4. Business\n5. Agriculture")
            course = int(input("Select an option: "))
            if (course > 0) and (course < 6):
                break
        
        if course == 1:
            self.course = "Science"
        elif course == 2:
            self.course = "General Art"
        elif course == 3:
            self.course = "Visual Art"
        elif course == 4:
            self.course = "Business"
        else:
            self.course = "Agric"
        
        option = 0
        if course == 1:
            while True:
                print("Science with which course?\n"
                    "1. Biology\n2. Elective ICT\n3. Geography")
                option = int(input("Select an option: "))
                if 0 < option < 4:
                    break

            if option == 1:
                self.elective_option = "bio"
            elif option == 2:
                self.elective_option = "eict"
            else:
                self.elective_option = "geo"

        elif course == 2:
            while True:
                print("What combination of General Arts?\n"
                      "1. Econs/ Geography/ Elective Maths/ Government\n" \
                      "2. Econs/ Geography/ Elective Maths/ Elective ICT\n" \
                      "3. Econs/ Government/ Literature/ CRS")
                option = int(input("Select an option: "))
                if 0 < option < 4:
                    break

            if option == 1:
                self.elective_option = "op1"
            elif option == 2:
                self.elective_option = "op2"
            else:
                self.elective_option = "op3"

        elif course == 3:
            while True:
                print("What combination of Visual Art?\n"
                    "1. GKA/ Graphic Design/ Picture Making/ Sculpture\n2. GKA/ Ceramics/ Leatherwork/ Textiles")
                option = int(input("Select an option: "))
                if 0 < option < 3:
                    break

            if option == 1:
                self.elective_option = "op1"
            else:
                self.elective_option = "op2"
   
        elif course == 4:
            while True:
                print("Business with which course?\n"
                    "1. Elective Maths\n2. Cost Accounting")
                option = int(input("Select an option: "))
                if 0 < option < 3:
                    break

            if option == 1:
                self.elective_option = "emaths"
            else:
                self.elective_option = "c_a"
        
        else:
            while True:
                print("Agric with which course?\n"
                    "1. Physics\n2. Animal Husbandry")
                option = int(input("Select an option: "))
                if 0 < option < 3:
                    break

            if option == 1:
                self.elective_option = "phy"
            else:
                self.elective_option = "anim"

        Student.record_user_results(self)

    def record_user_results(self):
        print("Enter your results:")
        print("-"*3 + "Core Subjects" + "-"*3)
        result_core_math = input("Core mathematics: ")
        self.results["Core Math"] = result_core_math
        result_english = input("English Language: ")
        self.results["English"] = result_english
        result_social = input("Social Studies: ")
        self.results["Social Studies"] = result_social
        result_intsci = input("Integrated Science: ")
        self.results["Integrated Science"] = result_intsci

        #taking the electives the student studied
        def science_student():
            print("\n"+"-"*3 + "Elective Subjects" + "-"*3)
            result_physics = input("Physics: ")
            self.results["Physics"] = result_physics
            result_chemistry = input("Chemistry: ")
            self.results["Chemistry"] = result_chemistry
            result_emath = input("Elective Math: ")
            self.results["Elective Math"] = result_emath

            if self.elective_option.lower() == "bio":
                result_bio = input("Biology: ")
                self.results["Biology"] = result_bio
            elif self.elective_option.lower() == "eict":
                result_ict = input("Elective Ict: ")
                self.results["Elective ICT"] = result_ict
            elif self.elective_option.lower() == "geo":
                result_geo = input("Geography: ")
                self.results["Geography"] = result_geo
            else:
                print("Invalid input")
                science_student()

        def general_art_student():
            # collecting general art student results
            print("\n"+"-"*3 + "Elective Subjects" + "-"*3)
            if self.elective_option.lower() == "op1":
                result_econs = input("Economics: ")
                self.results["Economics"] = result_econs
                result_geo = input("Geography: ")
                self.results["Geography"] = result_geo
                result_emath = input("Elective Math: ")
                self.results["Elective Math"] = result_emath
                result_gov = input("Government: ")
                self.results["Government"] = result_gov
            elif self.elective_option.lower() == "op2":
                result_econs = input("Economics: ")
                self.results["Economics"] = result_econs
                result_geo = input("Geography: ")
                self.results["Geography"] = result_geo
                result_emath = input("Elective Math: ")
                self.results["Elective Math"] = result_emath
                result_ict = input("Elective Ict: ")
                self.results["Elective ICT"] = result_ict
            elif self.elective_option.lower() == "op3":
                result_econs = input("Economics: ")
                self.results["Economics"] = result_econs
                result_gov = input("Government: ")
                self.results["Government"] = result_gov
                result_lit = input("Literature: ")
                self.results["Literature"] = result_lit
                result_crs = input("Christian Religious Studies(CRS): ")
                self.results["CRS"] = result_crs
            else:
                print("Invalid Input")
                general_art_student()

        def visual_art_student():
            print("\n"+"-"*3 + "Elective Subjects" + "-"*3)
            if self.elective_option.lower() == "op1":
                result_gka = input("General Knowledge in Art(GKA): ")
                self.results["Economics"] = result_gka
                result_gd = input("Graphic Design: ")
                self.results["Graphic Design"] = result_gd
                result_picmk = input("Picture Making: ")
                self.results["Picture Making"] = result_picmk
                result_sculpt = input("Sculpting: ")
                self.results["Sculpting"] = result_sculpt
            elif self.elective_option.lower() == "op2":
                result_gka = input("General Knowledge in Art(GKA): ")
                self.results["Economics"] = result_gka
                result_cer = input("Ceramics: ")
                self.results["Ceramics"] = result_cer
                result_text = input("Textiles: ")
                self.results["Textiles"] = result_text
                result_leath = input("Leatherwork: ")
                self.results["Leatherwork"] = result_leath
            else:
                print("Invalid Input")
                visual_art_student()

        def business_student():
            print("\n"+"-"*3 + "Elective Subjects" + "-"*3)
            result_econs = input("Economics: ")
            self.results["Economics"] = result_econs
            result_bm = input("Business Management: ")
            self.results["Business Management"] = result_bm
            result_fa = input("Financial Accounting: ")
            self.results["Financial Accounting"] = result_fa

            if self.elective_option.lower() == "emaths":
                result_emath = input("Elective Math: ")
                self.results["Elective Math"] = result_emath
            elif self.elective_option.lower() == "c_a":
                result_ca = input("Cost Accounting: ")
                self.results["Cost Accounting"] = result_ca
            else:
                print("Invalid input")
                business_student()

        def agric_student():
            print("\n"+"-"*3 + "Elective Subjects" + "-"*3)
            result_genagr = input("General Agric: ")
            self.results["General Agric"] = result_genagr
            result_chemistry = input("Chemistry: ")
            self.results["Chemistry"] = result_chemistry
            result_emath = input("Elective Math: ")
            self.results["Elective Math"] = result_emath

            if self.elective_option.lower() == "phy":
                result_phy = input("Physics: ")
                self.results["Physics"] = result_phy
            elif self.elective_option.lower() == "anim":
                result_anim = input("Animal Husbandry: ")
                self.results["Animal Husbandry"] = result_anim
            else:
                print("Invalid input")
                agric_student()

        if self.course.lower() == "science":
            science_student()
        elif self.course.lower() == "general art":
            general_art_student()
        elif self.course.lower() == "visual art":
            visual_art_student()
        elif self.course.lower() == "business":
            business_student()
        else:
            agric_student()
    
    def get_user_results(self):
        print(f"Student ID: {self.id}\nStudent name: {Student.get_fullname(self)}")
        for key, value in self.results.items():
                print(f"{key}: {value}")