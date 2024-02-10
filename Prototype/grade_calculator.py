grade = int(input("Enter your grade score: "))

def grade_calculator():
    if grade >= 80 <=100:
        print("เกรด A")
    elif grade >=70 <=79:
        print("เกรด B")
    elif grade >= 60 <= 69:
        print("เกรด C")
    elif grade >= 50 <= 59:
        print("เกรด D")
    elif grade < 50:
        print("เกรด F")

grade_calculator()
            