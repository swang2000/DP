'''
Given an array of integers, every element appears twice except for one. Find that single one.
Note: There can be an element appearing odd number of times. That element needs to be counted as single number.
In case of odd number of copies, the even ones get cancelled out from each other rendering just one element in the end.
'''


def singlenumber(a):
    for i in range(0, len(a), 2):
        if a[i] != a[i+1]:
            return a[i]



a = [8,8,10,7,7,6,6,15,15]
a.sort()
print(str(singlenumber(a)))


