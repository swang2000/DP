
def findpath(maze):
    if (maze ==  None) or (maze.ndim == 0):
        return None
    path = []
    failedpoint = []
    if getpath(maze, maze.shape[0]-1, maze.shape[1]-1, path, failedpoint):
        return path



def getpath(maze, row, col, path, failedpoint):
    if (row < 0) or (col < 0) or (maze[row, col] is False):
        return False
    p = [row, col]
    if (p in failedpoint):
        return False
    isAtOrigin = (row == 0) & (col == 0)
    if (isAtOrigin or getpath(maze, row, col - 1, path, failedpoint) or
            getpath(maze, row - 1, col, path, failedpoint)):
        path.append(p)
        return True
    failedpoint.append(p)
    return False


import numpy as np
def countpaths2(maze):
    if maze[0,0] == -1:
        return 0
    m, n = maze.shape
    for i in range(m):
        if maze[i, 0] ==0:
            maze[i, 0] =1
        else:
            break
    for j in range(n):
        if maze[0, j] >=0:
            maze[0, j] =1
        else:
            break

    for i in range(1, m):
        for j in range(1,n):
            if maze[i, j] != -1:
                if maze[i-1, j] >0:
                    maze[i, j] = maze[i, j] + maze[i-1, j]
                if maze[i, j-1] > 0:
                    maze[i, j] = maze[i, j] + maze[i, j-1]
    return maze

maze = np.array([[0,  0, 0, 0],
              [0, -1, 0, 0],
              [-1, 0, 0, 0],
              [0,  0, 0, 0]])
countpaths2(maze)





