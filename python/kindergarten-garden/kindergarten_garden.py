"""
Grass
Clover
Radishes
Violets

- Alice, Bob, Charlie, David,
- Eve, Fred, Ginny, Harriet,
- Ileana, Joseph, Kincaid, and Larry.
"""


class Garden:
    def __init__(self, diagram, students=None):
        self.dict_plants = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets"
        }

        self.array_student = [
            'Alice', 'Bob', 'Charlie', 'David',
            'Eve', 'Fred', 'Ginny', 'Harriet',
            'Ileana', 'Joseph', 'Kincaid', 'Larry'
        ]

        self.diagram = diagram.split('\n')
        # self.students = sorted(students) if students != None else self.array_student

        if students != None:
            self.students = sorted(students)
        else:
            self.students = self.array_student

    def plants(self, student):
        student_position = self.students.index(student)
        diagram = self.order_plants()

        return diagram[student_position]

    def order_plants(self):
        last_index = 0
        plants = []

        for item in range(0, len(self.diagram[0]) + 1, 2):

            first_line = self.diagram[0][last_index:item]
            second_line = self.diagram[1][last_index:item]

            if not first_line and not second_line:
                continue

            plants.append(
                [
                    self.dict_plants[first_line[0]],
                    self.dict_plants[first_line[1]],
                    self.dict_plants[second_line[0]],
                    self.dict_plants[second_line[1]]
                ])

            last_index = item

        return plants
