"""
{
    1: [Romulo, Rodrigo, Rogério],
    2: []
}
"""


class School:
    def __init__(self):
        self._students = []
        self._grades = []
        pass

    def add_student(self, name, grade):
        if grade in self._grades:
            self._students[grade].append(name)

        else:
            self._students.insert(grade, [name])

    def roster(self):
        students = []

        for item in self._students:
            students.extend(item)

        return sorted(students)

    def grade(self, grade_number):
        if not self._grades and grade_number not in self._grades:
            return []

        else:
            return self._students[grade_number]
