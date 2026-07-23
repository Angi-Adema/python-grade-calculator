#Variables to store user input for name, three assignment names, and corresponding grades
user_name = ""

assignment_name_1 = ""
assignment_name_2 = ""
assignment_name_3 = ""

assignment_grade_1 = 0.0
assignment_grade_2 = 0.0
assignment_grade_3 = 0.0

#

#Prompt user for to input name, three assignment names, and corresponding grades
user_name = input("Please enter your first and last name: ")

assignment_name_1 = input("Enter the name of assignment 1: ")
assignment_grade_1 = float(input("Enter the grade for assignment 1: "))
assignment_name_2 = input("Enter the name of assignment 2: ")
assignment_grade_2 = float(input("Enter the grade for assignment 2: "))
assignment_name_3 = input("Enter the name of assignment 3: ")
assignment_grade_3 = float(input("Enter the grade for assignment 3: "))

#Display welcome message
print("Welcome to your grade calculator!")

