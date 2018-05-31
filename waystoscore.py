'''
Reach a given score
Show Topic Tags
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of distinct
combinations to reach the given score.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N.

Output:

Print number of ways/combinations to reach the given score.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 1000

Example:

Input
3
8
20
13

Output
1
4
2
Explanation
For 1st example when n = 8
{ 3, 5 } and {5, 3} are the two possible permutations but these represent the same cobmination. Hence output is 1.

** For More Input/Output Examples Use 'Expected Output' option **
'''

# Returns number of ways to reach score n
def count(n):
    # // table[i] will store count of solutions for
    # // value i.
    table = [0]*(n+1)

    #// Base case (If given value is 0)
    table[0] = 1

    # // One by one consider given 3 moves and update the table[]
    # // values after the index greater than or equal to the
    # // value of the picked move
    for i in range(3, n+1):
       table[i] += table[i-3]
    for i in range(5, n+1):
       table[i] += table[i-5]
    for i in range(10, n+1):
       table[i] += table[i-10]

    return table[n]



count(20)