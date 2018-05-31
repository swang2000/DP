'''
Printing Maximum Sum Increasing Subsequence
3.1
The Maximum Sum Increasing Subsequence problem is to find the maximum sum subsequence of a given sequence such that all
elements of the subsequence are sorted in increasing order.

Examples:

Input:  [1, 101, 2, 3, 100, 4, 5]
Output: [1, 2, 3, 100]

Input:  [3, 4, 5, 10]
Output: [3, 4, 5, 10]

Input:  [10, 5, 4, 3]
Output: [10]

Input:  [3, 2, 6, 4, 5, 1]
Output: [3, 4, 5]
Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
In previous post, we have discussed about Maximum Sum Increasing Subsequence problem. However, the post only covered code
 related to finding maximum sum of increasing subsequence, but not to the construction of subsequence. In this post,
 we will discuss how to construct Maximum Sum Increasing Subsequence itself.
'''


def maxsumsubarray(a):
    maxa = a.copy()
    pos = list(range(len(a)))
    for i in range(1,len(a)):
        for j in range(0, i):
            if a[j] < a[i]:
                if maxa[j] + a[i] > maxa[i]:
                    maxa[i] = maxa[j] + a[i]
                    pos[i] = j
    return max(maxa)


a = [1, 101, 2, 3, 100, 4, 5]
b = [3, 2, 6, 4, 5, 1]
maxsumsubarray(a)
maxsumsubarray(b)

