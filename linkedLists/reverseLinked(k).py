a = [1,2,3,4,5,6,7,8,9,10,11,12]

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# creating the linked list        
head = Node(a[0])
p = head

for i in range(1,len(a)):
    node = Node(a[i])
    p.next = node
    p = node
    
########################################################
# reversing k elements in a linked list

node = head
k = 3
queue = []
headNodeCheck = False

while node != None:
    finalConnection = firstNode = node
    node = node.next
    count = 1
    
    # reversing k nodes in the linked lists
    while count != k and node != None:
        tempConnection = node.next
        node.next = firstNode
        firstNode = node
        node = tempConnection
        count += 1

    # setting the first node of the linkedList        
    if headNodeCheck == False:
        head = firstNode
        headNodeCheck = True        
    
    # connecting the last element of k reversed linked list                
    if len(queue) != 0:
        queue[0].next = firstNode
        del queue[0]    
    queue.append(finalConnection)
    finalConnection.next = node
        
        
p = head

# printing linked list in reverse order
while p:
    print(p.value)
    p = p.next        
        