""" find the middle element in the linked list """

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
a = [1,2,3,4,5,6,7]

# creating linked list 
head = Node(a[0])
q = head
for i in range(1,len(a)):
    p = Node(a[i])
    q.next = p
    q = p
    p = p.next


# getting the mid point of the linked list using dictionaries
p = head
linkedDict = {}
count = 1
while p:
    linkedDict[count] = p
    count += 1
    p = p.next
    
""" 
time complexity = O(n) 
space complexity = O(n)
"""


import math
size = len(linkedDict) % 2
if size == 0:
    middleElement = len(linkedDict) / 2    
else:
    middleElement = math.ceil(len(linkedDict) / 2)
print(linkedDict[middleElement].value)

""" overall complexity 
time complexity = O(n) 
space complexity = O(n)
"""


######################################################
#using two pointer method
slowPointer = head 
fastPointer = head 

while fastPointer:
    if fastPointer.next != None:        
        fastPointer = fastPointer.next.next
    else:
        break
    if fastPointer != None:
        slowPointer = slowPointer.next
print(slowPointer.value)

""" overall complexity 
time complexity = O(n/2) ~ O(n)
space complexity = O(1)
"""


















