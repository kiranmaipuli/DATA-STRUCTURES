""" binary heap operations """

#a = [1,5,9,4,2,10,15,18]
a = [12, 11, 13, 5, 6, 7]


def maxHeapify(i,arrayName,arrayLength):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i         
        if left < arrayLength and a[i] < a[left]:
            largest = left
        if right < arrayLength and a[largest] < a[right]:
            largest = right
        if largest != i:
            arrayName[largest],arrayName[i] = arrayName[i],arrayName[largest]
            maxHeapify(largest,arrayName,arrayLength)

# heapifying an array    
def buildingHeap(arrayName):
    lastNode = len(arrayName) - 1    
    startNode = (lastNode - 1) // 2
    for i in range(startNode,-1,-1):
        maxHeapify(i,arrayName,len(arrayName))    

# popping the max element in the heap
def delete(arrayName):
    arrayName[0] = arrayName[-1]
    del arrayName[-1]
    maxHeapify(0,arrayName,len(arrayName))

# inserting element in the heap and heapyfing after inserting
def insert(arrayName,element):
    arrayName.append(element)
    lastNode = len(arrayName) - 1    
    i = (lastNode - 1) // 2            
    while i >= 0:
        maxHeapify(i,arrayName,len(arrayName))
        i = (i - 1) // 2 

def heapSort(arrayName):
    Arraylength = len(arrayName)
    buildingHeap(arrayName) # O(n)
    for i in arrayName: # O(n)
        arrayName[0],arrayName[Arraylength - 1] = arrayName[Arraylength - 1],arrayName[0]
        Arraylength -= 1
        maxHeapify(0,arrayName,Arraylength) # O(logn)
        
        
buildingHeap(a)
insert(a,20)    
heapSort(a)
#delete(a)
print(a)        