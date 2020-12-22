""" Recursively remove all adjacent duplicates: Given a string of characters,
recursively remove adjacent duplicate characters from string. The output string should not
have any adjacent duplicates. """

inputString = "careermonk"
stack = []

# implementation using stack
for i in inputString:
    
    # if stack is empty, append the element to the stack
    if len(stack) == 0:
        stack.append(i)
    else:
        # if element already exists in the stack
        if stack[-1] == i:
            del stack[-1]            
        else:
            stack.append(i)
print(("").join(stack),"******")
        






































