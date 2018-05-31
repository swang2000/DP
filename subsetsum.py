'''
Dynamic Programming | Set 25 (Subset Sum Problem)
3.4
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal
to given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
'''

def subetsum(a, s):
    if len(a)== 0 and s==0:
        return True
    if len(a)== 0 and s!=0:
        return False
    if a[0] ==s:
        return True
    else:
        return subetsum(a[1:], s-a[0]) or subetsum(a[1:], s)


def findsubsetsum(b, s):
    a = [x for x in b if x <=s]
    return subetsum(a,s)


b = [3,4,34,12,5,2]
findsubsetsum(b, 35)


