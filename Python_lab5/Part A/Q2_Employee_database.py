employees = {
    "E1": {"name": "Kiran", "dept": "IT", "salary": 60000},
    "E2": {"name": "Sara", "dept": "HR", "salary": 45000},
    "E3": {"name": "Dev", "dept": "IT", "salary": 75000},
    "E4": {"name": "Nina", "dept": "Finance", "salary": 52000},
    "E5": {"name": "Omar", "dept": "HR", "salary": 48000}
}


def get_salary():
    while True:
        try:
            salary = float(input("Enter salary: "))
            if salary >= 0:
                return salary
            print("Salary cannot be negative.")
        except ValueError:
            print("Enter a valid salary.")


def add_employee():

    emp_id = input("Enter employee ID: ").strip()

    if not emp_id:
        print("Employee ID cannot be empty.")
        return

    if emp_id in employees:
        print("Employee ID already exists.")
        return

    name = input("Enter employee name: ").strip()
    dept = input("Enter department: ").strip()

    if not name or not dept:
        print("Name and department cannot be empty.")
        return

    salary = get_salary()

    employees[emp_id] = {
        "name": name,
        "dept": dept,
        "salary": salary
    }

    print("Employee added successfully.")


def update_salary():

    emp_id = input("Enter employee ID: ").strip()

    if emp_id not in employees:
        print("Employee not found.")
        return

    employees[emp_id]["salary"] = get_salary()

    print("Salary updated successfully.")


def delete_employee():

    emp_id = input("Enter employee ID: ").strip()

    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")


def search_employee():

    emp_id = input("Enter employee ID: ").strip()

    if emp_id in employees:

        emp = employees[emp_id]

        print("\nEmployee ID:", emp_id)
        print("Name:", emp["name"])
        print("Department:", emp["dept"])
        print("Salary:", emp["salary"])

    else:
        print("Employee not found.")


def reports():

    # Department-wise payroll and headcount
    departments = {}

    for emp in employees.values():

        dept = emp["dept"]

        if dept not in departments:
            departments[dept] = {
                "payroll": 0,
                "headcount": 0
            }

        departments[dept]["payroll"] += emp["salary"]
        departments[dept]["headcount"] += 1

    print("\n1. Department-wise Payroll and Headcount")

    for dept, data in departments.items():
        print(dept,
              "Payroll:", data["payroll"],
              "Headcount:", data["headcount"])

    # Highest-paid employee in each department
    highest_paid = {}

    for emp_id, emp in employees.items():

        dept = emp["dept"]

        if (dept not in highest_paid or
                emp["salary"] > highest_paid[dept]["salary"]):

            highest_paid[dept] = {
                "name": emp["name"],
                "salary": emp["salary"]
            }

    print("\n2. Highest-paid Employee in Each Department")

    for dept, emp in highest_paid.items():
        print(dept, ":", emp["name"], "-", emp["salary"])

    # Sort employees by salary
    sorted_employees = sorted(
        employees.items(),
        key=lambda item: item[1]["salary"],
        reverse=True
    )

    print("\n3. Employees Sorted by Salary")

    for emp_id, emp in sorted_employees:
        print(emp_id, emp["name"], emp["salary"])

    # Create a new dictionary with a 10% raise
    raised_employees = {
        emp_id: {
            **emp,
            "salary": emp["salary"] * 1.10
        }
        for emp_id, emp in employees.items()
        if emp["salary"] < 50000
    }

    print("\n4. Employees After 10% Raise")

    for emp_id, emp in raised_employees.items():
        print(emp_id, emp["name"], emp["salary"])

    print("\nOriginal Employee Salaries")

    for emp_id, emp in employees.items():
        print(emp_id, emp["name"], emp["salary"])

    # Department with highest average salary
    averages = {
        dept: data["payroll"] / data["headcount"]
        for dept, data in departments.items()
    }

    print("\n5. Department with Highest Average Salary")

    if averages:
        best_dept = max(averages, key=averages.get)
        print(best_dept, ":", averages[best_dept])
    else:
        print("No employee records available.")


while True:

    print("\n===== EMPLOYEE DATABASE =====")
    print("1. Add Employee")
    print("2. Update Salary")
    print("3. Delete Employee")
    print("4. Search Employee")
    print("5. Reports")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        update_salary()

    elif choice == "3":
        delete_employee()

    elif choice == "4":
        search_employee()

    elif choice == "5":
        reports()

    elif choice == "6":
        print("Exiting Employee Database.")
        break

    else:
        print("Invalid choice. Try again.")