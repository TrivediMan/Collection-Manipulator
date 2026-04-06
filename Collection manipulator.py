print("Jay Shree Krishna")
students = {}
while True:
    print("\nWelcome to the Student Data Organizer!")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")
        students[sid] = {
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": subjects
        }
        print("\nStudent added successfully!")
    elif choice == "2":
        if not students:
            print("\nNo students found.")
        else:
            print("\n--- Display All Students ---")
            for sid, info in students.items():
                print(f"Student ID: {sid} | Name: {info['name']} | Age: {info['age']} | "
                      f"Grade: {info['grade']} | Subjects: {info['subjects']}")
    elif choice == "3":
        print("Exiting program...Goodbye!")
        print("Thank you for using this program!......👍😊")
        break
    else:
        print("Invalid choice. Please try again.")