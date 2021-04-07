class Matrix:
    def __init__(self, lines):
        self.lines = lines
        lines = [[]]

    def __getitem__(self, index):
        return self.lines[index]

    def __add__(self, other):
        for i in range(len(self.lines)):
            for j in range(len(self.lines[0])):
                return self.lines[i][j] + other.lines[i][j]

    def __str__(self):
        for i in range((self.lines)):
            for j in range(len(self.lines[0])):
                print (self.lines[i][j], end = ' ')

first_m = Matrix([[1, 2, 3, 4], [17, 18, 19, 20]])
second_m = Matrix([[21, 22, 23, 24], [37, 38, 39, 40]])
print(str(first_m + second_m))
