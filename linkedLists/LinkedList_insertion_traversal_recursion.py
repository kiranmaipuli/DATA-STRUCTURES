""" inserting and traversing a linked list using recursion """

a = [1,2,3,4,5,6,7]

#linked list structure
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

head = Node(a[0])
count = 1
length = len(a)
q = head

#creating linked list using recursion   
def createLinkedList(count,q):
    if count < len(a):
        p = Node(a[count])
        q.next = p
        q = p
        count += 1
        createLinkedList(count,q)
createLinkedList(count,q)


p = head

#traversing the linked list
def traversingLinkedList(p):
    if p != None:
        print(p.value)
        traversingLinkedList(p.next)    

traversingLinkedList(p)

