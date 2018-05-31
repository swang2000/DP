'''
Dynamic Programming | Set 4 (Longest Common Subsequence)
2.8
We have discussed Overlapping Subproblems and Optimal Substructure properties in Set 1 and Set 2 respectively.
We also discussed one example problem in Set 3. Let us discuss Longest Common Subsequence (LCS) problem as one more
example problem that can be solved using Dynamic Programming.

LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. A
subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, “abc”,
“abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n different possible
subsequences.

It is a classic computer science problem, the basis of diff (a file comparison program that outputs the differences
between two files), and has applications in bioinformatics.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
'''

def findLCS(a, b):
    m = len(a)
    n = len(b)
    if m*n ==0:
        return 0
    if a[m-1] == b[n-1]:
        return 1 + findLCS(a[:m-1], b[:n-1])
    else:
        return max(findLCS(a[:(m-1)], b), findLCS(a, b[:n-1]))


a = 'AGGTAB'
b = 'GXTXAYB'
findLCS(a, b)

