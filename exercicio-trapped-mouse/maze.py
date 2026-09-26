from stack import Stack
from cell import Cell

class Maze:
    def __init__(self):
        self.currentCell = None
        self.entryCell = None
        self.exitCell = None
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

    def start(self, maze_file: str):
        self.__mountMaze(maze_file)
        self.__set_entry_exit_cells()

        print(self.maze)

if __name__ == "__main__":
    maze = Maze()
    maze.start("arquivos/labirinto1.txt")