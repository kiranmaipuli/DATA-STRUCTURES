""" converting sorted linked list to binary search tree """

a = [1,2,3,4,5,6,7]

class Node:
    
    # node structure of the linked list
    def __init__(self,value):
        self.value = value
        self.next = None
        
head = p = Node(a[0])

# creating a linked list
for i in range(1,len(a)):
    q = Node(a[i])        
    p.next = q
    p = p.next
    
p = head

queue = []

def extractingValues1(head):
    fastPointer = head
    slowPointer = None
    breakPoint = None
    counter = 0

    while fastPointer != None:
        if fastPointer.next != None:
            fastPointer = fastPointer.next.next
        else:
            fastPointer = fastPointer.next

        if counter == 0:
            slowPointer = head
            counter = 1
        else:
            if slowPointer != None and slowPointer.next != None:
                breakPoint = slowPointer
            slowPointer = slowPointer.next
    
    queue.append(slowPointer.value)
    

    if breakPoint != None:
        breakPoint.next = None
        extractingValues1(head)
    if slowPointer != None and slowPointer.next != None:
            extractingValues1(slowPointer.next)

extractingValues1(head)
print(queue)
