class Matrix:
    def __init__(self, matrix_string):
        matrix_string = matrix_string.split('\n')
        self.matrix = []

        for line in matrix_string:
            line_matrix = []
            for item in line.split(' '):
                line_matrix.append(int(item))
            
            self.matrix.append(line_matrix)


    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        column_matrix = []

        for line in self.matrix:
            column_matrix.append(line[index - 1])
        
        return column_matrix
