def input_student_data():
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    return name, score


def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"


def display_result(name, score, grade):
    print("\n--- Student Result ---")
    print("Name:", name)
    print("Score:", score)
    print("Grade:", grade)


# Main Program
name, score = input_student_data()
grade = calculate_grade(score)
display_result(name, score, grade)
