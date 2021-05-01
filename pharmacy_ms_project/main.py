from pharmacy_ms.app import *
import json


def print_menu():
    print("""
    ######################################
    ###########1. Add Employee############
    ###########2. Show Employee###########
    ###########2. Add Customer############
    ###########3. Add Medicine############
    ###########4. Show Employee Data######
    ######################################
               """)


if __name__ == "__main__":
    print_menu()
    employee_object_list = []
    customer_data = {}
    salesManagement_data = {}

    menu_choice = 0
    while menu_choice != 5:
        try:
            menu_choice = int(input("Enter your choice: "))
        except ValueError as e:
            print('Please Try again..')

        if menu_choice == 1:
            employee_id = int(input("Enter employee id: "))
            employee_name = input("Enter employee name: ")
            address = input("Enter Employee address: ")
            phone_number = input("Enter employee phone number: ")
            salary = float(input("Enter employee salary: "))
            payment = float(input("Enter employee payment: "))
            employee = Employee(
                id=employee_id,
                name=employee_name,
                address=address,
                phone_number=phone_number,
                salary=salary,
                payment=payment,
            )

            employee_data = {
                'employee_id': employee.id,
                'employee_name': employee.name,
                'address': employee.address,
                'phone_number': employee.phone_number,
                'salary': employee.salary,
                'payment': employee.payment,
                'salary_due': employee.salary_due()
            }
            employee_object_list.append(employee_data)
            with open('employee.json', 'w') as f:
                json.dump(employee_object_list, f, ensure_ascii=False, indent=4)
            print("Successfully saved")

        elif menu_choice == 2:
            try:
                with open('employee.json','r') as f:
                    employee_object_list = json.load(f)
                print("Employee Object list", employee_object_list)
            except NameError as e:
                print('Your phone book is totally emty')

        elif menu_choice >= 5:
            break
            print_menu()
