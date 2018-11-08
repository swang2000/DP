'''
Dynamic Programming | Set 6 (Min Cost Path)
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost path
to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse through that cell. Total cost of a
path to reach (m, n) is sum of all the costs on that path (including both source and destination). You can only
traverse down, right and diagonally lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j),
(i, j+1) and (i+1, j+1) can be traversed. You may assume that all costs are positive integers.

'''

import numpy as np
def minCost(m):
    r, c = m.shape
    cost = m.copy()
    cost[0, :] = np.cumsum(cost[0,:])
    cost[:, 0] = np.cumsum(cost[:,0])
    for i in range(1,r):
        for j in range(1, c):
            cost[i, j] = min(cost[i-1, j-1], cost[i-1, j], cost[i, j-1]) + m[i, j]
    return cost


m = np.array([[1, 2, 3],
             [4, 8, 2],
             [1, 5, 3]])

minCost(m)



