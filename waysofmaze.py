'''
Count number of ways to reach destination in a Maze
Given a maze with obstacles, count number of paths to reach rightmost-bottommost cell from topmost-leftmost cell. A
cell in given maze has value -1 if it is a blockage or dead end, else 0.

From a given cell, we are allowed to move to cells (i+1, j) and (i, j+1) only.

Examples:

Input: maze[R][C] =  {{0,  0, 0, 0},
                      {0, -1, 0, 0},
                      {-1, 0, 0, 0},
                      {0,  0, 0, 0}};
Output: 4
There are four possible paths as shown in
below diagram.
'''

import numpy as np
def waysofmaze(maze):
    m, n = maze.shape
    ways = np.ones((m,n))
    for i in range(n):
        if maze[0, i] == 0:
            ways[0, i] = 1
        elif maze[0, i] == -1:
            ways[0, i:] = 0
            break
    for j in range(m):
        if maze[j,0] == 0:
            ways[j,0] = 1
        elif maze[j,0] == -1:
            ways[j:,] = 0
            break
    for i in range(1, m):
        for j in range(1,n):
            if maze[i, j] == -1:
                ways[i, j] =0
            else:
                ways[i, j] = ways[i-1,j]+ ways[i, j-1]
    return ways


a= np.array([[0, 0, 0, 0],
    [0, -1, 0, 0],
    [-1, 0, 0, 0],
    [0, 0, 0, 0]])

waysofmaze(a)



