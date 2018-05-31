'''
Shortest Common Supersequence
3.1
Given two strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences.

Examples:

Input:   str1 = "geek",  str2 = "eke"
Output: "geeke"

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  "AGXGTXAYB"
'''

def findSCS(a, b):
    c = a
    prev = 0
    for i in range(len(b)):
        index = c[prev:].index(b[i]) + prev if b[i] in c[prev+1:] else -1
        if index >= 0:
            prev = index
        else:
            c = c[:prev+1]+b[i]+c[prev+1:]
    return c

a = 'AGGTAB'
b = 'GXTXAYB'
findSCS(a,b)

import numpy as np
def findSCS2(a, b):
    m = len(a)
    n = len(b)
    l = LCS(a,b)
    return m+n-l


def LCS(a, b):
    m = len(a)
    n = len(b)
    mn = np.zeros((m+1, n+1))
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                mn[i, j] = mn[i - 1, j - 1] + 1
            else:
                mn[i, j] = max(mn[i - 1, j], mn[i, j - 1])
    return mn[m,n]


a = 'AGGTAB'
b = 'GXTXAYB'
findSCS2(a, b)