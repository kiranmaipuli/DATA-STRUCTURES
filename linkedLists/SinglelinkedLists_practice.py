a = [1,2,4,1,8,9,10]

#node class
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

##########################################        
#head of the linked list        
head = Node(a[0])        

#inserting the elements in the linked list
for i in range(1,len(a)):
    p = Node(a[i])
    if i == 1:
        head.next = p
    else:
        q.next = p
    q = p
        
k = head
###########################################

#traversing the linked list
while k != None:
    #print(k.value)
    k = k.next
###########################################    
#inserting new element(11) after 8 (at the ith element)
m = Node(11)
k = head

while k != None:
    if k.value == 8:
        temp = k.next
        k.next = m
        m.next = temp
        break
    k = k.next


###########################################    
#deleting 11 from the linked list
k = head
while k != None:
    if k.next.value == 11:
        k.next = k.next.next
        break
    k = k.next

###########################################
#inserting new node at the beginning
p = Node(0)
p.next = head
head = p

###########################################
#inserting new node at the end
ap = Node(100)
while p != None:
    if p.next == None:
        p.next = ap
        break
    p = p.next
    
###########################################
#inserting new node at 3rd position
    
ap1 = Node(101)
count = 0
p = head

while p != None:
    count += 1
    if count == 2:
        temp = p.next
        p.next = ap1
        ap1.next = temp
        break
    p = p.next

###########################################
    


























