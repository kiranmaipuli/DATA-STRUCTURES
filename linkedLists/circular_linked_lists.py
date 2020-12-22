""" operations of a singly circular linked lists """

a = [1,2,3,4,5,6]

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

######################################
#creating circular circular linked list        
head = Node(a[0])

for i in range(1,len(a)):
    p = Node(a[i])
    if i == 1:
        head.next = p
    elif i == len(a) - 1:
        q.next = p
        p.next = head
    else:
        q.next = p
    q = p

######################################
#traversing a circular linked list
p = head
while p != None:
    print(p.value)
    p = p.next
    if p == head:
        print(p.value)
        break

######################################
#insert a new element at the beginning
k = Node(0)
p = head
while p != None:
    p = p.next
    if p.next == head:
        p.next = k
        break

k.next = head
head = k
######################################
#insert a new element at the end
lastElement = Node(1000)
p = head
while p != None:
    p = p.next
    if p.next == head:
        p.next = lastElement
        lastElement.next = head
        break

######################################
        









