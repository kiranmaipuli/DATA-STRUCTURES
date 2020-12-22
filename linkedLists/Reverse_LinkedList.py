""" Reverse a single linked list """
a = [1,2,3,4,5,6,7]
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

head = Node(a[0])
for i in range(1,len(a)):
    p = Node(a[i])
    if i == 1:
        head.next = p
    else:
        q.next = p
    q = p


temp = nextNode = None
p = head

# storing the reverse order of the linked list in another linked list
while p:
    nextNode = p.next
    p.next = temp
    temp = p
    p = nextNode
    
# printing the linked list in the reverse order    
q = temp
while temp:
    print(temp.value)    
    temp = temp.next
    
    
    
    
    
    
    
    
    
    
    
    
    
    