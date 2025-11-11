from employees import employee_ops
from employees import stats

def main():
    ops = employee_ops.EmployeeOps()  

    while True:
        print("\n--- Employee Management System ---")
        print("1. View Employees")
        print("2. Add Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Employee Stats")
        print("6. Exit")

        try:
            user_choice = int(input("Please enter a number (1-6): "))
        except ValueError:
            print("Invalid input — please enter a number.")
            continue  # loop again

        if user_choice == 1:
            ops.view_employees()  

        elif user_choice == 2:
            name = input("Name of Employee: ")
            age = int(input("Age of Employee: "))
            title = input("Employee Title: ")
            employee_id = input("Employee ID: ")

            ops.add_employee(name, age, title, employee_id)
            print(f"{name} added successfully!")

        elif user_choice == 3:
            ID = input("Employee ID to update: ")
            field = input("What field do you want to update? (name, age, title): ").lower()
            new_value = input(f"Enter new {field}: ")

            if field == "age":
                new_value = int(new_value)

            ops.update_employees(ID, **{field: new_value})  #  use kwargs correctly

        elif user_choice == 4:
            ID = input("Enter employee ID to delete: ")
            result = ops.delete_employee(ID)
            print(result)

        elif user_choice == 5:
            data = [emp.to_dict() for emp in ops.employees]
            total = stats.get_total_employees(data)
            avg_age = stats.get_average_age(data)
            print(f"Total Employees: {total}")
            print(f"Average Age: {avg_age:.2f}")

        elif user_choice == 6:
            print("Exiting program... Goodbye!")
            break  #  exit the loop

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
