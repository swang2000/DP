# Palindrome: Implement a function to check if a linked list is a palindrome.
import CdataS.Linkedlist.Linkedlist as Llist

def check_palindrone(l):
    n = l.size
    res = ispalindrone(l.root, n)
    return res[1]





def ispalindrone(node, n):
    if (n==0) or (node is None):
        return [node, True]
    if n == 1:
        return [node.next_node, True]
    res = ispalindrone(node.next_node, n-2)
    pa = node.data == res[0].data
    if res[1] & pa:
        return [res[0].next_node, True]
    else:
        return res


l = Llist.LinkedList()
l.append(0)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(3)
l.append(2)
l.append(1)
l.append(0)
l.printL()

check_palindrone(l)


