class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = matrix_string.split("\n")
        self.new_rows = self.make_rows()
        

    def make_rows(self):
        self.new_rows = []
        for row in self.rows:
            new_row = row.split(" ")
            for index, nr in enumerate(new_row):
                new_row[index] = int(nr)
            self.new_rows.append(new_row)
        return self.new_rows

    def row(self, index):
        real_index = index - 1
        return self.new_rows[real_index]

    def column(self, index):
        real_index = index - 1
        columns = []
        for row_var in self.new_rows:
            columns.append(row_var[real_index])
        return columns
