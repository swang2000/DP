'''
Maximum size square sub-matrix with all 1s
3.3
Given a binary matrix, find out the maximum size square sub-matrix with all 1s.

For example, consider the below binary matrix.
maximum-size-square-sub-matrix-with-all-1s
'''

import numpy as np
def maxonematrix(a):
    r,c = a.shape
    smatrix = np.zeros((r, c))
    smatrix[0,:] = a[0,:]
    smatrix[:,0] = a[:, 0]
    izero = (a==0)
    smatrix[izero] = 0
    for i in range(1,r):
        for j in range(1, c):
            if a[i,j] == 1:
                smatrix[i,j] = min(smatrix[i-1, j-1],smatrix[i-1, j], smatrix[i, j-1]) + 1

    return smatrix.max()


a = np.array([[0, 1, 1, 0, 1],
              [1, 1, 0, 1, 0],
              [0, 1, 1, 1, 0],
              [1, 1, 1, 1, 0],
              [1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0]])
maxonematrix(a)
