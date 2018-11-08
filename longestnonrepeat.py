'''
Length of the longest substring without repeating characters
Given a string, find the length of the longest substring without repeating characters. For example, the longest
substrings without repeating characters for “ABDEFGABEF” are “BDEFGA” and “DEFGAB”, with length 6. For “BBBB” the
longest substring is “B”, with length 1. For “GEEKSFORGEEKS”, there are two longest substrings shown in the below
diagrams, with length 7.
'''

def longestnonrepeat(a):
    maxl = 0
    suml = 0
    aset = set()
    for i in a:
        if i not in aset:
            suml += 1
            aset.add(i)
        else:
            if suml > maxl:
                maxl = suml
            aset.clear()
            suml =0
    return maxl


a = 'GEEKSFORGEEKS'
longestnonrepeat(a)



