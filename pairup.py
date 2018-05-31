'''
Friends Pairing Problem
3.2
Given n friends, each one can remain single or can be paired up with some other friend. Each friend can be paired only once. Find out the total number of ways in which friends can remain single or can be paired up.

Examples:

Input  : n = 3
Output : 4
Explanation
{1}, {2}, {3} : all single
{1}, {2,3} : 2 and 3 paired but 1 is single.
{1,2}, {3} : 1 and 2 are paired but 3 is single.
{1,3}, {2} : 1 and 3 are paired but 2 is single.
Note that {1,2} and {2,1} are considered same.
'''

def pairup1(n):
    if n == 0 or n==1 or n==2:
        return n
    return pairup1(n-1) + (n-1)*pairup1(n-2)



def pairup2(n):
    a = list(range(n+1))
    if n >=3:
        for i in range(3,n+1):
            a[i] = a[i-1] + (i-1)*a[i-2]
    return a[n]



pairup1(3)
pairup2(4)