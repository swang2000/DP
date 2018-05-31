'''
Find the longest path in a matrix with given constraints
3.4
Given a n*n matrix where all numbers are distinct, find the maximum length path (starting from any cell) such that all
cells along the path are in increasing order with a difference of 1.

We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1)
with the condition that the adjacent cells have a difference of 1.

Example:

Input:  mat[][] = {{1, 2, 9}
                   {5, 3, 8}
                   {4, 6, 7}}
Output: 4
The longest path is 6-7-8-9.
'''

import numpy as np


def longpath(i, j, mat, dp):
    n = len(mat)
    if i < 0 or j < 0 or i >= n or j >= n:
        return 0
    if dp[i, j] != -1:
        return dp[i, j]
    if j < n - 1 and ((mat[i][j] + 1) == mat[i][j + 1]):
        dp[i][j] = 1 + longpath(i, j + 1, mat, dp)

    if j > 0 & (mat[i][j] + 1 == mat[i][j - 1]):
        dp[i][j] = 1 + longpath(i, j - 1, mat, dp)

    if i > 0 & (mat[i][j] + 1 == mat[i - 1][j]):
        dp[i][j] = 1 + longpath(i - 1, j, mat, dp)

    if i < n - 1 and (mat[i][j] + 1 == mat[i + 1][j]):
        dp[i][j] = 1 + longpath(i + 1, j, mat, dp)

        # If none of the adjacent fours is one greater
    dp[i][j] = max(1, dp[i, j])
    return dp[i, j]


def findLongpath(mat):
    result = 1   #Initialize result
    n = len(mat)
    # Create a lookup table and fill all entries in it as -1
    dp = np.zeros((n,n)) -1

    # Compute longest path beginning from all cells
    for i in range(n):
        for j in range(n):
            if dp[i][j] == -1:
                longpath(i, j, mat, dp)
                result = max(result, dp[i][j])
    return result


mat = [[1,2,9],
       [5,3,8],
       [4,6,7]]

findLongpath(mat)
