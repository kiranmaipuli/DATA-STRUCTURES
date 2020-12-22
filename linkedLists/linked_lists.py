""" creating doubly linked lists and printing the linked list elements in reverse order """

"""
Created on Sat Mar 14 15:12:57 2020

@author: kiranmai
"""

#linked lists

x = [1,2,3,4,5,6]

class Node:
    def __init__(self):
        self.data = 0
        self.next = None
        self.previous = None
        
class linkedLists:
    
    # creating doubly linked list    
    for index, value in enumerate(x):
        node = Node()
        node.data = value
        if index == 0:
            startingPoint = node
            head = node
        else:
            node.previous = startingPoint
            startingPoint.next = node
            startingPoint = node
        
    linkedListIteration = head
    
    # printing linked list elements
    while linkedListIteration != None:
        print(linkedListIteration.data)
        if linkedListIteration.next == None:
            endPoint = linkedListIteration
        linkedListIteration = linkedListIteration.next
        
        
    # printing doubly linked list in reverse order
    print("printing elements in reverse order")
    reverseIteration = endPoint
    while reverseIteration != None:
        print(reverseIteration.data)
        reverseIteration = reverseIteration.previous

linked = linkedLists()



