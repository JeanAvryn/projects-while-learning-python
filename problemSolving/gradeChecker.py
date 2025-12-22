def grade_checker():
    grade = input("Enter your grade: ")
    try:
        grades = int(grade)
        if grades <= 100 and grades >= 90:
            print("Your grade is A.")
        elif grades <= 89 and grades >= 80:
            print("Your grade is B.")
        elif grades <= 79 and grades >= 70:
            print("Your grade is C.")
        elif grades <= 69 and grades >= 0:
            print("Your grade is F.")
        else:
            print("Invalid grade.")
    except ValueError:
        print("Grade is not a number. Please enter a valid grade: ")
grade_checker()
