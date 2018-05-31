'''
How to print maximum number of A’s using given four keys
4.4
This is a famous interview question asked in Google, Paytm and many other company interviews.

Below is the problem statement.

Imagine you have a special keyboard with the following keys:
Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it
                 after what has already been printed.

If you can only press the keyboard for N times (with the above four
keys), write a program to produce maximum numbers of A's. That is to
say, the input parameter is N (No. of keys that you can press), the
output is M (No. of As that you can produce).
Examples:

Input:  N = 3
Output: 3
We can at most get 3 A's on screen by pressing
following key sequence.
A, A, A

Input:  N = 7
Output: 9
We can at most get 9 A's on screen by pressing
following key sequence.
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

Input:  N = 11
Output: 27
We can at most get 27 A's on screen by pressing
following key sequence.
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V, Ctrl A,
Ctrl C, Ctrl V, Ctrl V
'''

# // A recursive function that returns the optimal length string
# // for N keystrokes
def findoptimal(N):

    # // The optimal string length is N when N is smaller than 7
    if (N <= 6):
        return N

    # // Initialize result
    max = 0

    # // TRY ALL POSSIBLE BREAK-POINTS
    # // For any keystroke N, we need to loop from N-3 keystrokes
    # // back to 1 keystroke to find a breakpoint 'b' after which we
    # // will have Ctrl-A, Ctrl-C and then only Ctrl-V all the way.
    # #int b;
    for b in range(N-3, 0, -1):
        #
        # // If the breakpoint is s at b'th keystroke then
        # // the optimal string would have length
        # // (n-b-1)*screen[b-1];
        curr = (N-b-1)*findoptimal(b)
        if (curr > max):
            max = curr
    return max

findoptimal(8)
findoptimal(12)