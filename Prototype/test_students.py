students = []

with open("students.csv") as file:
    for line in file:
        # Split the line into name and school
        elements = line.rstrip().split(",")
        
        # Check if there are enough elements
        if len(elements) == 2:
            name, school = elements
            student = {"name": name, "school": school}
            students.append(student)
        else:
            print(f"Skipping invalid line: {line}")

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in the {student['school']}")
