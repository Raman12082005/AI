import json
def save_data():
    data = []
    for student in students:
        data.append(student.to_dict())
    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)
def load_data():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)

            for item in data:
                students.append(Student(item["name"], item["roll_no"], item["marks"]))
    except (FileNotFoundError, json.JSONDecodeError):
        pass
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print(f"Name : {self.name}")
        print(f"Roll no. : {self.roll_no}")
        print(f"Marks : {self.marks}")
    def to_dict(self):
        return{
            "name": self.name,
            "roll_no": self.roll_no,
            "marks": self.marks
        }
    

students = []
load_data()
while True:
    print("1. Add student")
    print("2. Show Students")
    print("3. Search a Student")
    print("4. Delete a Student")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll_no = int(input("Enter Roll no. of the student: "))
        marks = int(input("Enter marks: "))
        students.append(Student(name, roll_no, marks))
        save_data()

    elif choice == "2":
        if(len(students) == 0):
            print("No Student found")
        else:
            print("**________Data of Students_________**")
            for student in students:
                student.display()
                print("-------------------")

    elif choice == "3":
        if(len(students) == 0):
            print("No Student found")
        else:
            roll = int(input("Enter a Roll no. to search: "))
            found = False
            for student in students:
                if(student.roll_no == roll):
                    print("**______Student found______**")
                    student.display()
                    found = True
                    break
            if not found:
                print("Student not found");

    elif choice =="4":
        if(len(students) == 0):
            print("No Student found")
        else:
            roll = int(input("Enter the Roll no. : "))
            found = False
            for student in students:
                if student.roll_no == roll:
                    students.remove(student)
                    save_data()
                    found = True
                    print("Student deleted successfully")
                    break
            if not found:
                print("No student found")


    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again")


