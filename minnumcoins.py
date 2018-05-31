'''
Find minimum number of coins that make a given value
3.2
Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change?

Examples:

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents
Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
This problem is a variation of the problem discussed Coin Change Problem. Here instead of finding total number of possible solutions, we need to find the solution with minimum number of coins.

The minimum number of coins for a value V can be computed using below recursive formula.

If V == 0, then 0 coins required.
If V > 0
   minCoin(coins[0..m-1], V) = min {1 + minCoins(V-coin[i])}
                               where i varies from 0 to m-1
                               and coin[i] <= V
Below is recursive solution based on above recursive formula.
'''


def mincoins(v, m, c):
    if v == 0:
        return 0
    res = 3000
    for i in range(m):
        if v >= c[i]:
            res_sub = mincoins(v - c[i], m, c)
            if res_sub != 3000 and ((res_sub + 1) < res):
                res = res_sub + 1
    return res



v = 33
c  = [25, 11, 5, 1]
v1 = 11
c1 = [9,6,5,1]
b = mincoins(v,len(c),c)
b1 = mincoins(v1,len(c1),c1)

