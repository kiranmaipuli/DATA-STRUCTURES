""" Given a linked list with even and odd numbers, create an algorithm for making
changes to the list in such a way that all even numbers appear at the beginning. """

a = [1,2,3,4,5,6,7,8]

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# creating linked list
head = q = Node(a[0])
for i in range(1,len(a)):
    p = Node(a[i])
    q.next = p
    q = p
    p = p.next

even = odd = temp1 = temp2 = None
p = head
counte = counto = 0

# building odd and even linked list
def buildingLinkedLists(linkedList,linkedListObject,temp,count):
    if count == 0:
        linkedList = temp = linkedListObject
        count += 1
    else:
        temp.next = p
        temp = p
    return linkedList,count, temp
    
while p:
    if p.value % 2 == 0:            
        even,counte,temp1 = buildingLinkedLists(even,p,temp1,counte)
    else:
        odd,counto,temp2 = buildingLinkedLists(odd,p,temp2,counto)
    p = p.next

def traversing(p):
    while p:
        print(p.value)
        p = p.next

temp1.next = odd
temp2.next = None
head = even

traversing(head)

""" complexity
time complexity = O(n)
space complexity = O(n)
"""





















