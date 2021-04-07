class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        if (self.cells - other.cells) < 0:
            print('Разность меньше 0, операция невозможна')
        else:
            return self.cells - other.cells

    def __mul__(self, other):
        return self.cells * other.cells

    def __floordiv__(self, other):
        return self.cells // other.cells

    def __mod__(self, other):
        return self.cells % other.cells

    def make_order(self, num_cells):
        return f'{"*" * num_cells}\n' * (self.cells // num_cells)


cell_1 = Cell(25)
cell_2 = Cell(15)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(str(cell_1.make_order(5)))