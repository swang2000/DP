'''
Dynamic Programming | Set 5 (Edit Distance)
3.3
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits
(operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.

Examples:

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations.
Replace 'n' with 'r', insert t, insert a
'''

# recursive solution

def edistance(a, b):
    m = len(a)
    n = len(b)
    if m == 0:
        return n
    if n == 0:
        return m
    if a[0] == b[0]:
        return edistance(a[1:], b[1:])
    else:
        return min(1+ edistance(a[1:], b), 1+ edistance(a, b[1:]), 1+ edistance(a[1:], b[1:]))


# Dp solution
import numpy as np
def edistance2(a, b):
    m = len(a)
    n = len(b)
    dm = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if i == 0:
                dm[i,j] = j
            if j == 0:
                dm[i,j] = i
            if i*j >0:
                if a[i] == b[j]:
                    dm[i, j] = dm[i-1, j-1]
                else:
                    dm[i, j] = 1+min(dm[i-1, j],
                                     dm[i, j-1],
                                     dm[i-1, j-1])
    return dm[m-1, n-1]

str1 = "sunday"
str2 = "saturday"

edistance2(str1, str2)










