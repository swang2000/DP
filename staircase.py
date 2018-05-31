
# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.


def staircase(n):
    memo = [-1] * (n+1)
    ways = recurSC(n, memo)
    return ways


def recurSC(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if memo[n] > -1:
        return memo[n]

    else:
        memo[n] = recurSC(n - 1, memo) + recurSC(n - 2, memo) + recurSC(n - 3, memo)
    return memo[n]


staircase(3)