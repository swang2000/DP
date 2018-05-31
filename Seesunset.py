'''
An array of buildings is facing the sun. The heights of the building is given in an array. You have to tell which all
buildings will see the sunset.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,N is the number of buildings.
The second line of each test case contains N input H[i],height of building.

Output:

Print the total number of buildings which will see the sunset.

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 500
1 ≤ H[i] ≤ 1000

Example:

Input:
2
5
7 4 8 2 9
4
2 3 4 5

Output:
3
4

'''

def seesunset(a):
    highest = a[0]
    nbs = 1
    for i in range(1,len(a)):
        if a[i] > highest:
            nbs +=1
            highest = a[i]
    return nbs

a = [7, 4, 8, 2, 9]
a1 = [2, 3, 4, 5]
print(str(seesunset(a1)))


