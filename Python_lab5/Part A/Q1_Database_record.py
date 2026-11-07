students = {
    101: {"name": "Asha", "marks": {
        "Math": 88, "Physics": 76, "Chem": 92
    }},
    102: {"name": "Ravi", "marks": {
        "Math": 35, "Physics": 58, "Chem": 64
    }},
    103: {"name": "Meena", "marks": {
        "Math": 72, "Physics": 81, "Chem": 69
    }}
}


def get_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def add_student():
    try:
        roll = int(input("Enter roll number: "))
    except ValueError:
        print("Invalid roll number.")
        return

    if roll in students:
        print("Roll number already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    marks = {}

    try:
        n = int(input("How many subjects? "))
        if n <= 0:
            print("Enter at least one subject.")
            return
    except ValueError:
        print("Invalid number of subjects.")
        return

    for i in range(n):
        subject = input("Enter subject name: ").strip()

        if not subject:
            print("Subject name cannot be empty.")
            continue

        marks[subject] = get_marks()

    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully.")


def update_marks():
    try:
        roll = int(input("Enter roll number: "))
    except ValueError:
        print("Invalid roll number.")
        return

    if roll not in students:
        print("Student not found.")
        return

    subject = input("Enter subject name: ").strip()

    if not subject:
        print("Subject name cannot be empty.")
        return

    score = get_marks()
    students[roll]["marks"][subject] = score

    print("Marks updated successfully.")


def delete_student():
    try:
        roll = int(input("Enter roll number: "))
    except ValueError:
        print("Invalid roll number.")
        return

    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def show_record():
    try:
        roll = int(input("Enter roll number: "))
    except ValueError:
        print("Invalid roll number.")
        return

    if roll in students:
        print("\nRoll Number:", roll)
        print("Name:", students[roll]["name"])
        print("Marks:", students[roll]["marks"])
    else:
        print("Student not found.")


def reports():

    # Calculate average marks
    averages = {
        roll: round(sum(data["marks"].values()) /
                    len(data["marks"]), 2)
        for roll, data in students.items()
        if data["marks"]
    }

    print("\n1. Average Marks")

    for roll, avg in averages.items():
        print(students[roll]["name"], ":", avg)

    # Find the topper
    print("\n2. Class Topper")

    if averages:
        topper = max(averages, key=averages.get)
        print(students[topper]["name"],
              "with average", averages[topper])
    else:
        print("No student records available.")

    # Highest scorer in each subject
    subject_scores = {}

    for data in students.values():
        for subject, score in data["marks"].items():

            if (subject not in subject_scores or
                    score > subject_scores[subject][1]):

                subject_scores[subject] = (
                    data["name"], score
                )

    print("\n3. Highest Scorer in Each Subject")

    for subject, result in subject_scores.items():
        print(subject, ":", result[0], "-", result[1])

    # Students scoring below 40
    print("\n4. Students Scoring Below 40")

    below_40 = {
        data["name"]: {
            subject: score
            for subject, score in data["marks"].items()
            if score < 40
        }
        for data in students.values()
        if any(score < 40
               for score in data["marks"].values())
    }

    if below_40:
        for name, marks in below_40.items():
            print(name, ":", marks)
    else:
        print("No students found.")

    # Grade-wise grouping
    grades = {"A": [], "B": [], "C": [], "D": [], "F": []}

    for roll, avg in averages.items():

        name = students[roll]["name"]

        if avg >= 90:
            grades["A"].append(name)
        elif avg >= 75:
            grades["B"].append(name)
        elif avg >= 60:
            grades["C"].append(name)
        elif avg >= 40:
            grades["D"].append(name)
        else:
            grades["F"].append(name)

    print("\n5. Grade-wise Grouping")

    for grade, names in grades.items():
        print(grade, ":", names)


while True:

    print("\n===== STUDENT DATABASE =====")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Show Student Record")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_marks()

    elif choice == "3":
        delete_student()

    elif choice == "4":
        show_record()

    elif choice == "5":
        reports()

    elif choice == "6":
        print("Exiting Student Database.")
        break

    else:
        print("Invalid choice. Try again.")