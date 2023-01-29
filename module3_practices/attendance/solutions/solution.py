class AttendanceTracker:
    def __init__(self):
        self.students = {}

    def check_in(self, person: str):
        if person not in self.students.keys():
            raise ValueError("Student Not Found")
        self.students[person] = [person, True]

    def print_attendance(self):
        for i in self.students.keys():
            if self.students[i][1] == False:
                print(f"{self.students.keys[i][0]} : Absent")
            else:
                print(f"{self.students.keys[i][0]}: Present")

    def add_student(self, person: str):
        if person in self.students.keys():
            raise ValueError("Person Already Exists")
        else:
            self.students[person] = [person, False]

    def delete_student(self, person: str):
        if person not in self.students.keys():
            raise ValueError("Person does not exist")
        del self.students[person]
