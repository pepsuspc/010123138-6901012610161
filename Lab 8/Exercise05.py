class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def show(self):
        for row in self.data:
            for value in row:
                print(f"{value:5}",end="")
            print()

    def add(self,other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Cannot add: both matrices must be the same size")
        result = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                new_row.append(self.data[i][j] + other.data[i][j])
            result.append(new_row)
        return Matrix(result)

    def subtract(self,other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Cannot subtract: both matrics must be the same size")
        result = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                new_row.append(self.data[i][j] - other.data[i][j])
            result.append(new_row)
        return Matrix(result)

    def multiplication(self,other):
        if self.cols != other.rows:
            raise ValueError("Cannot multiply: columns of the first must equal rows of the second")
        result = []
        for i in range(self.rows):
            new_row = []
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                new_row.append(total)
            result.append(new_row)
        return Matrix(result)   