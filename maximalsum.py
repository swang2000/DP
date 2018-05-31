'''
Dynamic Programming | Set 31 (Optimal Strategy for a Game)
4.1
Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even. We play a game against an opponent
by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the
row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely
win if we move first.

Note: The opponent is as clever as the user.
Let us understand the problem with few examples:

    1. 5, 3, 7, 10 : The user collects maximum value as 15(10 + 5)

    2. 8, 15, 3, 7 : The user collects maximum value as 22(7 + 15)

Does choosing the best at each move give an optimal solution?

No. In the second example, this is how the game can finish:

1.
…….User chooses 8.
…….Opponent chooses 15.
…….User chooses 7.
…….Opponent chooses 3.
Total value collected by user is 15(8 + 7)

2.
…….User chooses 7.
…….Opponent chooses 8.
…….User chooses 15.
…….Opponent chooses 3.
Total value collected by user is 22(7 + 15)
'''


def maximalsum(a):
    if len(a) ==0:
        return 0
    if len(a) == 2:
        return max(a)
    return max(a[0]+ min(maximalsum(a[2:]), maximalsum(a[1:-1])),
                         a[-1]+min(maximalsum(a[1:-1]), maximalsum(a[:-2])))

a = [5, 3, 7, 10]
b = [8, 15, 3, 7]
maximalsum(a)
maximalsum(b)

