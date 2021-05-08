from app_model import *
import json


def print_menu():
    print("""
    ######################################
    ########### 1. Add Employee ##########
    ########### 2. Show Employee #########
    ########### 3. Delete Employee #######
    ########### 4. Add Customer ##########
    ########### 5. Show Customer #########
    ########### 6. Delete Customer #######
    ######################################
               """)


if __name__ == "__main__":
    print_menu()
    employee_object_list = []
    customer_object_list = []
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
                with open('employee.json', 'r') as f:
                    employee_object_list = json.load(f)
                print("Employee_id  Employee_name  Address  Phone_number  Salary  Payment  Salary_due")
                for employee in employee_object_list:
                    print(
                        f"{employee['employee_id']}      "
                        f"       {employee['employee_name']}         "
                        f" {employee['address']}  "
                        f"  {employee['phone_number']} "
                        f" {employee['salary']}  "
                        f"{employee['payment']} "
                        f" {employee['salary_due']}")
            except NameError as e:
                print('Something Wrong')
        elif menu_choice == 3:
            try:
                with open('employee.json', 'r') as f:
                    employee_object_list = json.load(f)
                print("Employee Object list", employee_object_list)
                id_of_employee = int(input("Delete Employee ID: "))
                delete_employee_list_object = []
                for employee in employee_object_list:
                    if employee['employee_id'] != id_of_employee:
                        delete_employee_list_object.append(employee)

                with open('employee.json', 'w') as f:
                    json.dump(delete_employee_list_object, f, ensure_ascii=False, indent=4)
                print("Successfully Deleted")

            except NameError as e:
                print('Something Wrong')
        elif menu_choice == 4:
            customer_id = int(input("Enter Customer id: "))
            customer_name = input("Enter Customer name: ")
            address = input("Enter customer address: ")
            phone_number = input("Enter customer phone number: ")
            medicine_price = float(input("Enter customer salary: "))
            payment = float(input("Enter customer payment: "))
            customer = Customer(
                id=customer_id,
                name=customer_name,
                address=address,
                phone_number=phone_number,
                medicine_price=medicine_price,
                payment=payment,
            )

            customer_data = {
                'customer_id': customer.id,
                'customer_name': customer.name,
                'address': customer.address,
                'phone_number': customer.phone_number,
                'salary': customer.medicine_price,
                'payment': customer.payment,
                'customer_due': customer.customer_due()
            }
            customer_object_list.append(customer_data)
            with open('customers.json', 'w') as f:
                json.dump(customer_object_list, f, ensure_ascii=False, indent=4)
            print("Successfully saved")

        elif menu_choice == 5:
            try:
                with open('customers.json', 'r') as f:
                    customer_object_list = json.load(f)
                print("Customer_id  Customer_name  Address  Phone_number  Medicine Price  Payment  Customer_due")
                for customer in customer_object_list:
                    print(
                        f"{customer['customer_id']}      "
                        f"       {customer['customer_name']}         "
                        f" {customer['address']}  "
                        f"  {customer['phone_number']} "
                        f" {customer['salary']}  "
                        f"{customer['payment']} "
                        f" {customer['customer_due']}")
            except NameError as e:
                print('Something Wrong')

        elif menu_choice >= 10:
            break
            print_menu()
