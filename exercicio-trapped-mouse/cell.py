class Cell:
    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __str__(self):
        return f"{self.__x}, {self.__y}"

    def __eq__(self, other_cell):
        if isinstance(other_cell, Cell):
            return (self.__x == other_cell.__x) and (self.__y == other_cell.__y) 
        
        #return self.__str__() == other_cell.__str__()

if __name__ == '__main__':
    #test overload __eq__()
    cell1 = Cell(10, 3)
    cell2 = Cell(10, 3)
    cell3 = Cell(3, 10)

    print(cell1 == cell2)
    print(cell2 == cell3)