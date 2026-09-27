from stack import Stack
from cell import Cell

class Maze:
    def __init__(self):
        self.currentCell: Cell = None
        self.entryCell: Cell = None
        self.exitCell: Cell = None
        self.mazeStack = Stack()
        self.maze: list[str] = []

    def __mountMaze(self, maze_file: str):
        mazeRows = Stack()
        with open(maze_file) as file:
            for line in file.readlines()[::-1]:
                line = f"1{line.replace('\n', '')}1"
                if mazeRows.top() is None:
                    mazeRows.push("1"*len(line))
                mazeRows.push(line)
            mazeRows.push("1"*len(line))

        current_row = mazeRows.pop()
        while current_row is not None:
            self.maze.append(current_row)
            current_row = mazeRows.pop()

    def __set_entry_exit_cells(self):
        for row_counter, current_row in enumerate(self.maze):
            entry = current_row.find('m')
            exit = current_row.find('e')
            if entry >= 0:
                self.entryCell = Cell(row_counter, entry)
                self.currentCell = Cell(row_counter, entry)
            if exit >= 0:
                self.exitCell = Cell(row_counter, exit)

    def __get_neighbours(self):
        current_x = self.currentCell.get_x()
        current_y = self.currentCell.get_y()

        right = Cell(current_x, current_y + 1)
        left = Cell(current_x, current_y - 1)
        down = Cell(current_x + 1, current_y)
        up = Cell(current_x - 1, current_y)

        return up, down, left, right

    def __check_neighbours(self, neighbours: list[Cell]):
        valid = []
        for cell in neighbours:
            value = self.maze[cell.get_x()][cell.get_y()]
            if value not in ['1', '.']:
                valid.append(cell)
        return valid

    def __set_currentCell_as_visited(self):
        if self.currentCell is not None:
            list_str = list(self.maze[self.currentCell.get_x()])
            list_str[self.currentCell.get_y()] = '.'
            self.maze[self.currentCell.get_x()] = ''.join(list_str)

    def start(self, maze_file: str):
        self.__mountMaze(maze_file)
        self.__set_entry_exit_cells()

# if __name__ == "__main__":
#     maze = Maze()
#     maze.start("arquivos/labirinto1.txt")