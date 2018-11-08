'''
Dynamic Programming | Set 12 (Longest Palindromic Subsequence)
Given a sequence, find the length of the longest palindromic subsequence in it.

longest-palindromic-subsequence

As another example, if the given sequence is “BBABCBCAB”, then the output should be 7 as “BABCBAB” is the longest
palindromic subseuqnce in it. “BBBBB” and “BBCBB” are also palindromic subsequences of the given sequence, but not the
longest ones.
'''

import numpy as np
def Longestpalindrome(str):
    n = len(str)
    L = np.zeros((n,n))
    for i in range(n):
        L[i, i] =1

    for subl in range(2, n+1):
        for i in range(n-subl+1):
            j = i+subl-1
            if str[i] == str[j] and subl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j])

    return L


a = 'GEEKSFORGEEKS'
Longestpalindrome(a)




