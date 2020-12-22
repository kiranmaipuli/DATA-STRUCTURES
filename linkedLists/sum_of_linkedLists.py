""" adding two linked lists """

#linked lists:
x = [2,4,3]
y = [5,6,4]
dctNames = {}
count = 0
count1 = 0
carry = 0

# structure of the linked list node
class nodes:  
    def __init__(self,data):
        self.data = data
        self.next = None    
        
class linkedList:  #class for linked lists1
    def __init__(self):
        self.head = None
        
def creatingLinkedLists(a,llist):  #creating linked lists
    count = 0
    llist.head = nodes(a[0])  #creating head of the linked lists
    for i in range(1,len(a)):  #creating rest of the nodes
        dctNames[count] = nodes(a[i])
        count = count + 1
    llist.head.next = dctNames[0]  #linking head with next element

    for i in range(1,len(dctNames)):  #linking rest of the next elements with each other
        dctNames[i-1].next = dctNames[i]


#creating objects for linked lists
llists1 = linkedList()
llists2 = linkedList()
llists3 = linkedList()

creatingLinkedLists(x,llists1)
creatingLinkedLists(y,llists2)

temp1 = llists1.head
temp2 = llists2.head

# doing sum of the linked lists
while (temp1 != None or temp2 != None):
    answer = temp1.data + temp2.data + carry
    if answer > 9:
        carry = int(answer / 10)
        answer = int(answer % 10)        
    if count == 0:
        llists3.head = nodes(answer)
        count = count + 1
    else:
        dctNames[count1] = nodes(answer)
        count1 = count1 + 1
    
    temp1 = temp1.next
    temp2 = temp2.next
    
    
llists3.head.next = dctNames[0]

for i in range(1,len(dctNames)):
    dctNames[i-1].next = dctNames[i]

temp3 = llists3.head

# printing the sum in reverse order
while(temp3):
    print(temp3.data)
    temp3 = temp3.next