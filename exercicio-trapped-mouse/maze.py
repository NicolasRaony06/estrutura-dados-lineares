import os
import subprocess
import time

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
                line = f"1{line.replace('\n', '').strip()}1"
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

    def __add_neighbours_mazeStack(self, neighbours):
        if neighbours:
            for cell in neighbours:
                self.mazeStack.push(cell)

    def start(self, maze_file: str):
        """Receives a txt file containing the maze structure and mounts the internal maze structure."""
        self.__mountMaze(maze_file)
        self.__set_entry_exit_cells()

    def exit(self, animated: bool = False):
        '''Returns the exit cell if it exists and is possible in the maze. Receives a boolean value for an animated representation of the exit finding process.'''
        clear_command = 'cls' if os.name == 'nt' else 'clear'
        while self.currentCell != self.exitCell:
            self.__set_currentCell_as_visited()
            neighbours = self.__check_neighbours(self.__get_neighbours())
            self.__add_neighbours_mazeStack(neighbours)

            if self.mazeStack.top() is not None:
                self.currentCell = self.mazeStack.pop()
                if animated:
                    print(self.__str__())
                    time.sleep(0.4)
                    subprocess.run(clear_command, shell=True)
            else:
                return None

        #self.__set_currentCell_as_visited()
        return self.currentCell

    def __str__(self):
        formated_maze = '\n'.join(self.maze)
        return formated_maze
        
# if __name__ == "__main__":
#     maze = Maze()
#     maze.start("arquivos/labirinto1.txt")