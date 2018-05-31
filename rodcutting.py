'''
Dynamic Programming | Set 13 (Cutting a Rod)
3.1
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the rod
is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by cutting
in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
'''

# recursive solution
# def rodcutting(n, p):
#     if n ==1:
#         return p[0]
#     else:
#         maxv = p[n-1]
#         for i in range(1,n//2+1):
#             temp = rodcutting(i, p[:i]) + rodcutting(n-i, p[:n-i])
#             if temp > maxv:
#                 maxv = temp
#     return maxv
#
#
#
# n = 8
# p = [1,   5,   8,   9,  10,  17,  17,  20]
# rodcutting(n, p)

# dynamic programming

def rodcutting2(n, p):
    v = p.copy()
    v[1] = max(2*v[0], p[1])
    for i in range(2,n):
        maxv = p[i]
        for j in range(i//2+1):
            temp = v[j] + v[i-j-1]
            if temp > maxv:
                maxv = temp
        v[i] = maxv
    return v

n = 8
p = [1,   5,   8,   9,  10,  17,  17,  20]
rodcutting2(n, p)



