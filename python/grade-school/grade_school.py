class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students.setdefault(grade, []).append(name)

    def roster(self):
        all_students = []

        keys = sorted(self.students.keys())

        for key in keys:
            all_students.extend(sorted(self.students[key]))

        return all_students

    def grade(self, grade_number):
        return sorted(self.students.get(grade_number, []))