"""
Student Grade Calculator 

Program prompting the user to enter the student name,
three assignment names, and their associated grades for the purpose of 
calculating the total score as well as the average score. We then display 
the results in a professional report.

"""

# Display a welcome message
print("Welcome to the grade calculator!")

# Prompt user to enter their name
user_name = input("\nEnter the student's first and last name: ")

# Prompt user to enter first assignment name and grade
assignment_name_1 = input("\nEnter the name of assignment 1: ")
assignment_grade_1 = float(input("Enter the grade for assignment 1: "))

# Prompt user to enter second assignment name and grade
assignment_name_2 = input("\nEnter the name of assignment 2: ")
assignment_grade_2 = float(input("Enter the grade for assignment 2: "))

# Prompt user to enter third assignment name and grade
assignment_name_3 = input("\nEnter the name of assignment 3: ")
assignment_grade_3 = float(input("Enter the grade for assignment 3: "))

# Calculate the total grade score
total_score = assignment_grade_1 + assignment_grade_2 + assignment_grade_3

# Calculate the average score
average_score = total_score / 3

# Display the grade report
print("\nGrade Report For:", user_name)
print("------------------------------------")
print(f"{assignment_name_1:<20}: {assignment_grade_1:>6.2f}")
print(f"{assignment_name_2:<20}: {assignment_grade_2:>6.2f}")
print(f"{assignment_name_3:<20}: {assignment_grade_3:>6.2f}")
print("------------------------------------")
print(f"{'Total Score':<20}: {total_score:>6.2f}")
print(f"{'Average Score':<20}: {average_score:>6.2f}")


# REFERENCES
# 1. GeeksforGeeks. (2025, August 14). "Multiline Comments in Python" 
# https://www.geeksforgeeks.org/python/multiline-comments-in-python/
#
# 2. GeeksforGeeks. (2025, April 28). "Python Escape Characters" 
# https://www.geeksforgeeks.org/python/python-escape-characters/
#
# 3. GeeksforGeeks. (2026, March 18). "String Formatting in Python" 
# https://www.geeksforgeeks.org/python/string-formatting-in-python/
#
# 4. GeeksforGeeks. (2025, July 15). "String Alignment in Python f-string" 
# https://www.geeksforgeeks.org/python/string-alignment-in-python-f-string/
#
# 5. Miller, B. (n.d.). "Programming in Python 3" zyBooks, a Wiley brand. 
# Canvas https://www.zybooks.com/


