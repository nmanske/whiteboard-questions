'''Implement an algorithm to find the kth to last element
'''

from random import randint

from LinkedList import LinkedList

def delete_middle_node(head):
    if head is None or head.next is None:
        return False

    nextNode = head.next
    head.next = nextNode.next

    return True

size = randint(0, 10)
ll = LinkedList.generate(size, 0, 9)
print('Before: ' + str(ll))
delete_middle_node(ll.head)
print('After: ' + str(ll))
