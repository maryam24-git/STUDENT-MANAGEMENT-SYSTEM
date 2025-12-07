students=[]  
def add_student():
    name=input("Enter student name: ")
    age=int(input("Enter age: "))
    if age<=0:
        print("Age cannot be zero or negative")
        return
    marks=float(input("Enter marks: "))
    if marks<0:
        print("Marks cannot negative")
        return
    student={"name": name, 
            "age": age, 
            "marks": marks}
    students.append(student)
    print("Student added.")
    
def view_students():
    if students==[]:   
        print("No students found.")
        return

    for s in students:
        print("Name:",s["name"])
        print("Age:",s["age"])
        print("Marks:",s["marks"])

def search_student():
    name=input("Enter name to search: ")
    for s in students:
        if s["name"]==name:
            print("Student Found!")
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Marks:", s["marks"])
            return 

    print("Student not found.")

def update_marks():
    name=input("Enter student name: ")
    for s in students:
        if s["name"].lower()==name.lower():
            new_marks=float(input("Enter new marks: "))
            s["marks"]=new_marks
            print("Marks updated!")
            return

    print("Student not found.")
while True:
    print("  STUDENT MANAGEMENT SYSTEM  ")
    print("(A) Add Student")
    print("(B) View Students")
    print("(C) Search Student")
    print("(D) Update Marks")
    print("(E) Exit")
    choice=input("Enter choice: ").upper()
    if choice=="A":
        add_student()
    elif choice=="B":
        view_students()
    elif choice=="C":
        search_student()
    elif choice=="D":
        update_marks()
    elif choice=="E":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")