'''Implement an algorithm to find the kth to last element
'''

from random import randint

from LinkedList import LinkedList

def delete_middle_node(head):
    if head is None:
        return

    current = head
    count = 0
    while current:
        count += 1
        current = current.next

    current = head
    for i in range(count//2):
        if i + 1 == count // 2:
            current.next = current.next.next
            return
        current = current.next

size = randint(0, 10)
ll = LinkedList.generate(size, 0, 9)
print('Before: ' + str(ll))
delete_middle_node(ll.head)
print('After: ' + str(ll))
