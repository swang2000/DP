'''
Count number of ways to cover a distance
1.9
Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.

Examples:

Input:  n = 3
Output: 4
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input:  n = 4
Output: 7
'''

def waystodistance(n):
    a = [0]*n
    a[0] = 1
    a[1] = 2
    a[2] = 4
    for i in range(3, n):
        a[i] = a[i-3] + a[i-2] + a[i-1]
    return a[n-1]

n =4
waystodistance(n)

