""" Split a Circular Linked List into two equal parts. If the number of nodes in the
list are odd then make first list one node extra than second list. """

a = [1,2,3,4,5,6]

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# creating linked lists        
head = Node(a[0])
q = head
for i in range(1,len(a)):
    p = Node(a[i])
    q.next = p
    q = p
    p = p.next
    if i == len(a) - 1:
        q.next = head

# printing linked lists        
def printingLinkedLists(linkedList):
    end = linkedList
    print("printing the linked list")
    while linkedList:
        print(linkedList.value)
        linkedList = linkedList.next
        if linkedList == end:
            print(linkedList.value)
            break
            
slowPointer = head
fastPointer = head

# getting the middle element
while fastPointer:
    if (fastPointer.next == head) or (fastPointer.next.next == head):
        break
    fastPointer = fastPointer.next.next
    slowPointer = slowPointer.next

middleElement = slowPointer

"""
time complexity = O(n/2) ~ O(n)
space complexity = O(1)
"""

head1 = head
head2 = middleElement.next
p = head1
q = head2

# creating the first linked list
while p:
    if p == middleElement:
        p.next = head1
        break
    p = p.next

# creating the second linked list    
while q:
    if q == head:
        z.next = head2
        break
    z = q
    q = q.next    

    
printingLinkedLists(head1)
printingLinkedLists(head2)    



















