""" reverse a linked list in pairs """

a = [1,2,3,4,5,6,7]

class Node:
    def __init__(self,value):
        self.value= value
        self.next = None

# creating the linked lists        
head = Node(a[0])
q = head 
for i in range(1,len(a)):
    p = Node(a[i])
    q.next = p
    q = p
    p = p.next
    
second = head.next
first = head
count = 0

# reversing the linked list in pairs
while second:
    nextLink = second.next
    second.next = first
    if count == 0:
        head = second
        count += 1
    else:
        previousLink.next = second
    previousLink = first
    if nextLink != None:
        second = nextLink.next
        first = nextLink
    else:
        previousLink.next = None
        break

    
if first and (second == None):
    previousLink.next = first
    first = None

p = head

# printing the elements of the reverse pairs linked lists
while p:
    print(p.value)
    p = p.next


