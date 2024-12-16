class Student:
    def __init__(self, student_id, enrollment_number, name, email, phone, address, program, stream):
        self.student_id = student_id
        self.enrollment_number = enrollment_number
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.program = program
        self.stream = stream

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.programs = ['B.Tech', 'BBA', 'MCA']
        self.streams = ['CSE', 'ECE', 'EEE', 'IT']

    def display_menu(self):
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Display Student by ID")
        print("6. Exit")

    def validate_input(self, field_name):
        while True:
            value = input(f"Enter {field_name}: ").strip()
            if value:
                return value
            print(f"{field_name} is required.")

    def add_student(self):
        student_id = len(self.students) + 1
        enrollment_number = student_id + 1000

        name = self.validate_input("Name")
        email = self.validate_input("Email")
        phone = self.validate_input("Phone")
        address = self.validate_input("Address")

        print("Choose Program:")
        for idx, program in enumerate(self.programs, 1):
            print(f"{idx}. {program}")
        program_choice = int(input("Select Program (1-3): "))

        print("Choose Stream:")
        for idx, stream in enumerate(self.streams, 1):
            print(f"{idx}. {stream}")
        stream_choice = int(input("Select Stream (1-4): "))

        student = Student(
            student_id, enrollment_number, name, email, phone, address, 
            self.programs[program_choice - 1], self.streams[stream_choice - 1]
        )
        self.students.append(student)
        print("Student Added Successfully!\n")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def update_student(self):
        student_id = int(input("Enter Student ID to Update: ").strip())
        student = self.find_student_by_id(student_id)
        if student:
            student.name = self.validate_input("New Name")
            student.email = self.validate_input("New Email")
            student.phone = self.validate_input("New Phone")
            print("Student Updated Successfully!\n")
        else:
            print("Student Not Found!\n")

    def delete_student(self):
        student_id = int(input("Enter Student ID to Delete: ").strip())
        student = self.find_student_by_id(student_id)
        if student:
            self.students.remove(student)
            print("Student Deleted Successfully!\n")
        else:
            print("Student Not Found!\n")

    def display_all_students(self):
        if not self.students:
            print("No Students Available!\n")
            return

        print("\n{:<5} {:<12} {:<10} {:<20} {:<12} {:<10} {:<10}".format("ID", "Enrollment", "Name", "Email", "Phone", "Program", "Stream"))
        print("-" * 80)
        for student in self.students:
            print("{:<5} {:<12} {:<10} {:<20} {:<12} {:<10} {:<10}".format(
                student.student_id, student.enrollment_number, student.name, student.email, 
                student.phone, student.program, student.stream))

    def display_student_by_id(self):
        student_id = int(input("Enter Student ID: ").strip())
        student = self.find_student_by_id(student_id)
        if student:
            print("\nStudent Details:")
            print(f"ID: {student.student_id}\nEnrollment: {student.enrollment_number}\nName: {student.name}\nEmail: {student.email}\nPhone: {student.phone}\nAddress: {student.address}\nProgram: {student.program}\nStream: {student.stream}\n")
        else:
            print("Student Not Found!\n")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Choose an option (1-6): ").strip()
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.update_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.display_all_students()
            elif choice == '5':
                self.display_student_by_id()
            elif choice == '6':
                print("Exiting Program. Goodbye!")
                break
            else:
                print("Invalid Choice. Try Again!\n")

if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run()
