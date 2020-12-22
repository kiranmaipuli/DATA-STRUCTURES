""" Given a stack of integers, how do you check whether each successive pair of
numbers in the stack is consecutive or not. The pairs can be increasing or decreasing, and
if the stack has an odd number of elements, the element at the top is left out of a pair. For
example, if the stack of elements are [4, 5, -2, -3, 11, 10, 5, 6, 20], then the output should
be true because each of the pairs (4, 5), (-2, -3), (11, 10), and (5, 6) consists of
consecutive numbers. """

stack = [4, 5, -2, -3, 11, 10, 0, 6]

#stack = [4, 5, -2, -3, 11, 10, 5, 6, 20]
flag = True

# checking whether the stack has odd number of elements
if len(stack) % 2 == 0:
    noOfIterations = len(stack)
else:
    noOfIterations = len(stack) - 1

index = 1

while index < noOfIterations:
    
    # checking whether the elements of stack are consecutive pairs
    if (stack[index] == stack[index-1] + 1) or (stack[index] == stack[index-1] - 1):
        index += 2
    
    # if not consecutive pairs, break out of the loop
    else:
        flag = False    
        break
    
print(flag)

