students = {} # Empty Dictionary.
def students_dict(name, grade): # Adding student Function.
    students[name] = grade # Adding student name and grade in empty dictionary.
    print('Successfully Added New Student.') # After adding printing this message.
    return f'Name: {name}\nGrade: {students[name]}%' # Returning name and grade so that user can know what they have added.

def grade(name): # Getting grade Function.
    print('Result of Student -') # Printing message for user to know what they are going to see.
    if name in students: # If this condition is true.
        return f'Name: {name}\nGrade: {students[name]}%' # Returning Name and Grade of students
    else:
        # If student does not found in dictionary then print this message. 
        return 'Student does not Exists. \nTo Add New Student Enter 1 in Menu.' # Return this message

while True: # Forever Loop
    try: # try-except to catch ValueError.
        menu = int(input('[1] - Add student | [2] - Get Grade | [3] - Exit\n')) # Menu for user to ask what they want to do.
        if menu == 1: # If this condition is true then 
            ask_student_name = input('Enter Name of Student - ') # Ask Student Name
            try: # try-except to catch ValueError 
                ask_student_grade = int(input('Enter Grade of Student - ')) # Ask student Grade
            except ValueError: # If error occured 
                print('Enter only Numbers.') # print this message
                continue
            result1 = students_dict(ask_student_name, ask_student_grade) # Assign name and grade from student_dict function those parameters.
            print(result1) # print result from students_dict.
        elif menu == 2: # if this condition is true
            print('Enter name of Student to Get Grade.') # Print  this message so that user know what they are doing.
            get_grade = input('Enter Name - ') # Ask Student Name.
            result2 = grade(get_grade) # Give get_grate to name from grade function.
            print(result2) # print result from grade function.
        else:
            print('Thankyou.') # Print this message when done.
            break # If everything done end

    except ValueError: # If error found
        print('Enter numbers between (1 - 3).') # Print this message
