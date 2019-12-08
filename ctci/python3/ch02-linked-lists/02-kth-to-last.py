'''Implement an algorithm to find the kth to last element
'''

from random import randint

from LinkedList import LinkedList

def kth_to_last(head, k):
    if head is None or k <= 0:
        return None

    length = 0
    current = head
    while current:
        current = current.next
        length += 1

    if k > length:
        return None

    current = head
    for _ in range(length-k):
        current = current.next

    return current.value

ll = LinkedList.generate(10, 0, 9)
print('List: ' + str(ll))
k = randint(0, 11)
print(str(k) + ' to Last: ' + str(kth_to_last(ll.head, k)))
