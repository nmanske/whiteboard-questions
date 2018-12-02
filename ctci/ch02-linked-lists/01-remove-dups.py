'''Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?'''

from LinkedList import LinkedList

def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.value])

    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

def remove_dups_nobuffer(ll):
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

# With buffer
ll = LinkedList.generate(100, 0, 9)
print('Before: ' + str(ll))
remove_dups(ll)
print('After: ' + str(ll) + '\n')

# No buffer
ll = LinkedList.generate(100, 0, 9)
print('Before: ' + str(ll))
remove_dups(ll)
print('After: ' + str(ll))
