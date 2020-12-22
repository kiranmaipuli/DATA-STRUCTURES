""" check if a linked list is circular or not """

a = [1,2,1]

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
# creating linked lists        
q = head = Node(a[0])
for i in range(1,len(a)):
    p = Node(a[i])
    q.next = p
    q = p
    p = p.next

#############################################
#method1: traversing the linked list and storing in string
palindromeString = ""
p = head
while p:
    palindromeString += str(p.value)         
    p = p.next

print(palindromeString)
length = len(palindromeString) - 1

reverseString = ""
while length >= 0:
    reverseString += palindromeString[length]
    length -= 1

if palindromeString == reverseString:
    print("linked list is a palindrome")
else:
    print("linked list is not a palindrome")
    
    