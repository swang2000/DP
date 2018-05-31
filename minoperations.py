'''
Minimum Operations
Show Topic Tags
Given a number N the task is to find an optimal solution to reach N from 0 using 2 operations ie
1. Double the number
2. Add one to the number

Example

Input  : N = 8
Output : 4
0 + 1 = 1, 1 + 1 = 2, 2 * 2 = 4, 4 * 2 = 8

Input  : N = 7
Output : 5
0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 3 * 2 = 6, 6 + 1 = 7

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N.

Output:
For each test case in a new line print an integer denoting the min no of operation to be performed to reach N from 0.

Constraints:
1<=T<=100
1<=N<=10000

Example:
Input:
2
8
7
Input:
4
5

** For More Input/Output Examples Use 'Expected Output' option **
'''

def minoperation(n):
    mo = [0, 1]
    for i in range(2, n+1):
        if i%2 == 0:
            mo.append(min(mo[int(i/2)]+1, mo[i-1]+1))
        else:
            mo.append(min(mo[i//2]+2, mo[i-1]+1))
    return mo[n]



minoperation(8)
minoperation(7)
minoperation(23)
