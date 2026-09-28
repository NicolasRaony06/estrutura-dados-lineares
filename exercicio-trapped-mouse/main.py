from maze import Maze

maze = Maze()

maze.start(maze_file="arquivos/labirinto1.txt")

result = maze.exit()
if result:
    print(f"Exit sucessfully finded, Cell: {result}")
    print(maze)
else: 
    print("There is no possible exit in the maze")
    print(maze)