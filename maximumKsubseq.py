'''
Maximum Sum Subsequence of length k
Show Topic Tags
Given an array sequence [A1 , A2 ...An], the task is to find the maximum possible sum of increasing subsequence S of
length K such that Si1<=Si2<=Si3.........<=Sin.

INPUT
The first line contains an integer 'T' denoting the number of testcases. Then 'T' test cases follows. Each test case
consists of two line containing two space separated integers 'N' and 'K' denoting the size of the array and length of
the subsequence.

OUTPUT
Print the maximum possible sum. If their is no subsequence of length K print "-1".

CONSTRAINTS
1 <= T <= 100
1 <= N <= 100
1 <= a[i] <= 10^5
1 <= k <=100

Example
Input
1
8 3
8 5 9 10 5 6 19 8

Output
38

Explanation
In sample input Possible Increasing subsequence of Length 3 with maximum possible sum is 9 10 19

** For More Input/Output Examples Use 'Expected Output' option **
'''


def MKSQ(a, k):
    n = len(a)
    ml = [1] *n
    for i in range(1, n):
        for j in range(0,i):
            if (a[j] < a[i]) and (ml[i] < (ml[j] + 1)):
                ml[i] = ml[j] + 1
    # mk = [i for i, item in enumerate(ml) if item>=k]
    # mitem = [item for i, item in enumerate(ml) if item >= k]
    # nmk = len(mk)
    # sumk = [0] *nmk
    # for i in range:
    sumk = []
    i = 0
    for index,item in enumerate(ml):
        if item >= k:
            w = k-1
            sumi = a[index]
            v = item -1
            while w > 0:
                x = [x for (x, y) in zip(a[:index], ml[:index]) if y==v]
                sumi += max(x)
                v -= 1
                w -= 1
                index = a.index(max(x))
            sumk.append(sumi)
    return max(sumk)

a= [8, 5, 9, 10, 5, 6, 19, 8]
k=3
MKSQ(a, k)