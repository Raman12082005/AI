# -----------------------------
# Parent Class
# -----------------------------
class Person:

    company = "ABC Technologies"      # Class Variable

    def __init__(self, name, age):
        self.name = name
        self.age = age


# -----------------------------
# Child Class
# -----------------------------
class Employee(Person):

    total_employees = 0       # Class Variable

    def __init__(self, emp_id, name, age, salary):

        super().__init__(name, age)

        self.emp_id = emp_id
        self._salary = salary          # Protected Variable
        self.__bonus = 5000            # Private Variable

        Employee.total_employees += 1

    def display(self):

        print("\n-----------------------")
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Salary      :", self._salary)
        print("Company     :", Person.company)

    def total_salary(self):
        print("Total Salary :", self._salary + self.__bonus)

    # Class Method
    @classmethod
    def show_total_employees(cls):
        print("Total Employees:", cls.total_employees)

    # Static Method
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0


# -----------------------------
# Main Program
# -----------------------------
employees = []

while True:

    print("\n===== Employee Management =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Show Total Employees")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        emp_id = int(input("Employee ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        salary = float(input("Salary: "))

        if Employee.is_valid_salary(salary):

            emp = Employee(emp_id, name, age, salary)
            employees.append(emp)

            print("Employee Added Successfully!")

        else:
            print("Invalid Salary")

    elif choice == "2":

        if len(employees) == 0:
            print("No Employees Found")

        else:
            for emp in employees:
                emp.display()
                emp.total_salary()

    elif choice == "3":

        Employee.show_total_employees()

    elif choice == "4":
        break

    else:
        print("Invalid Choice")