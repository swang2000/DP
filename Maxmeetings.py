'''
There is one meeting room in Flipkart. There are n meetings in the form of (S [ i ], F [ i ]) where S [ i ] is start
time of meeting i and F [ i ] is finish time of meeting i

What is the maximum number of meetings that can be accommodated in the meeting room ?



Input:

The first line of input consists number of the test cases. The description of T test cases is as follows:

The first line consists of the size of the array, second line has the array containing the starting time of all the
meetings each separated by a space, i.e., S [ i ]. And the third line has the array containing the finishing time of
all the meetings each separated by a space, i.e., F [ i ].


Output:

In each separate line print the order in which the meetings take place separated by a space.


Constraints:

1 ≤ T ≤ 70

1 ≤ N ≤ 100

1 ≤ S[ i ], F[ i ] ≤ 100000


Example:

Input:

2
6
1 3 0 5 8 5
2 4 6 7 9 9
8
75250 50074 43659 8931 11273 27545 50879 77924
112960 114515 81825 93424 54316 35533 73383 160252

Output:

1 2 4 5
6 7 1
'''





from bisect import bisect

class Meeting:
    # save about 500 bytes of memory
    #  by not having a __dict__
    __slots__ = ("start", "end")

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

def max_meetings(meetings):
    meetings.sort()    # Meeting.__lt__ provides a natural sort order by meeting.end

    # -1 is just a "lower than any actual time" gatepost value
    lst = [-1]

    for m in meetings:
        # find the longest chain of meetings which this meeting can follow
        i = bisect(lst, m.start)

        if i == len(lst):
            # new most-meetings value
            lst.append(m.end)
        elif m.end < lst[i]:
            # new earliest finish-time for
            lst[i] = m.end

    # what is the most meetings we can attend?
    # print(lst)
    return len(lst) - 1


meetings = [
    Meeting(0, 1),
    Meeting(1, 2),
    Meeting(2, 3),
    Meeting(3, 5),
    Meeting(4, 4.5)
]

print(max_meetings(meetings))   # => 4