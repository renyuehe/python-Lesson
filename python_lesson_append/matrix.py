class Matrix:

    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        a_row = len(self.data)
        a_col = len(self.data[0])

        b_row = len(other.data)
        b_col = len(other.data[0])

        if a_row != b_row and a_col != b_col:
            return "形状不同，不能相加"

        for row in range(a_row):
            for col in range(a_col):
                self.data[row][col] += other.data[row][col]

        return self

    def __str__(self):
        return str(self.data)


if __name__ == '__main__':
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    print(a + b)
