'''
Given a binary string, count number of substrings that start and end with 1. For example, if the input string is
“00100101”, then there are three substrings “1001”, “100101” and “101”.

Input:
The first line contains T denoting the number of testcases. Then follows description of testcases.
Each case contains a string containing 0's and 1's.


Output:
For each test case, output a single line denoting number of substrings possible.

Constraints:
1<=T<=100
1<=Lenght of String<=100


Example:
Input:
1
10101

Output:

'''

def countofsubstr(str):
    index =[]
    l1 = list(str)
    for i in range(len(l1)):
        if l1[i] == '1':
            index.append(i)
    finalset = set()
    for j in range(0, len(index)-1):
        for k in range((j+1),len(index)):
            s1 = '1'+'0'*(index[k]-index[j]-1)+'1'
            finalset.add(s1)
    return len(finalset)



str1 = '00100101'
countofsubstr(str1)

