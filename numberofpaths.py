'''
Paths to reach origin
Show Topic Tags
You are standing on a point (n, m) and you want to go to origin (0, 0) by taking steps either left or down i.e.
from each point you are allowed to move either in (n-1, m) or (n, m-1). Find the number of paths from point to origin.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test
case contains two integers n and m representing the point.

Output:
Print the total number of paths from point to origin.

Constraints:
1<=T<=100
1<=n,m<=100

Example:
Input:
3
3 2
3 6
3 0

Output:
10
84
1
'''

def numberofpaths(m,n):
    if m ==0 and n ==0:
        return 0
    elif m*n == 0:
        return 1
    if m > 0 and n > 0:
        return numberofpaths(m-1, n) + numberofpaths(m ,n-1)


numberofpaths(3,2)
numberofpaths(3,6)
numberofpaths(2,2)