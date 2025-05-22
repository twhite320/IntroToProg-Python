# -----------------------------------------------------------------------------#
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception
# handling
# Change Log: (Who, When, What)
# Tellrell White,05/19/2025,Created Script
# ------------------------------------------------------------------------------#

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''# Holds the first name of a student entered by the user.
student_last_name: str = '' # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if not file.closed:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        #Check to make sure first and last name are alphabet characters
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                 raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                 raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name, "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            #verify this works. Check syntax. Review lab code
            print(f"You have registered Student {student_data ["FirstName"]} "
                  f"{student_data ["LastName"]} for Course {student_data ["CourseName"]}.")

        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')

    # Present the current data stored in list
    elif menu_choice == "2":
        for row in students:
            print(row)

    #Writing data out to a JSON file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if not file.closed:
                file.close()

        print("The following data was saved to file!")
        for row in students:
            print(row)

    #Breaks out of loop to end program
    elif menu_choice == "4":
        break

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")


#Functionality for printing row of values
'''
       for student in students:
           print(f"{student["FirstName"]}, {student["LastName"]},"
                 f" {student["CourseName"]}")

                 '''