""" check whether a linked list is cyclic or a linear singly linked list """
a = [1,2,3,4,5,6]

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
#########################
#creating circular linked list
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

p = head

############################
#creating linear linked list

head1 = Node(a[0])
for i in range(1,len(a)):
    p = Node(a[i])
    if i == 1:
        head1.next = p
    else:
        q.next = p
    q = p

############################
p = head1

while p:
    print(p.value)
    if p.next == head:
        print("linked list is a cyclic linked list")
        break
    elif p.next == None:
        print("linked list is a linear linked list")
        break
    p = p.next
    
#################################
#using hash map for solving this
count = 0
p = head
myDict = {}
myList = []
while p:
    myList.append(p)
    if p in myDict:
        count = 1
        print("circular list")
        break
    else:
        myDict[p] = count
    p = p.next
if count == 0:
    print("linear linked list")    
    
################################################################
#slow pointer method - two pointer method - floyd pointer method

slow_pointer = head
fast_pointer = head

while fast_pointer:
    fast_pointer = fast_pointer.next.next
    slow_pointer = slow_pointer.next
    if slow_pointer == fast_pointer:
        print("circular loop")
        break

#################################################################
























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    