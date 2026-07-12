# -----------------------------
# Parent Class
# -----------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# -----------------------------
# Child Class
# -----------------------------
class Student(Person):

    def __init__(self, roll_no, name, age, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):

        if self.marks >= 90:
            return "A"

        elif self.marks >= 75:
            return "B"

        elif self.marks >= 60:
            return "C"

        elif self.marks >= 40:
            return "D"

        else:
            return "Fail"

    # Method Overriding
    def display(self):

        print("\n-----------------------")
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Marks   :", self.marks)
        print("Grade   :", self.calculate_grade())
        print("-----------------------")


# -----------------------------
# Student Management System
# -----------------------------
students = []

while True:

    print("\n===== Student Management =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        roll = int(input("Roll No: "))
        name = input("Name: ")
        age = int(input("Age: "))
        marks = float(input("Marks: "))

        student = Student(roll, name, age, marks)
        students.append(student)

        print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No students found.")

        else:
            for student in students:
                student.display()

    elif choice == "3":

        roll = int(input("Enter Roll No: "))

        found = False

        for student in students:

            if student.roll_no == roll:
                student.display()
                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")