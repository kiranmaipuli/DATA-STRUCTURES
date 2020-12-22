""" Given an array of characters formed with a’s and b’s. The string is marked with
special character X which represents the middle of the list (for example:
ababa...ababXbabab baaa). Check whether the string is palindrome. """
    
a = "appleXfelppa"    

start = 0
end = len(a) - 1
notPalindrome = "given string is not a palindrome"
palindrome = "given string is a palindrome"

while start < end:
    if a[start] == a[end]:
        start += 1
        end -= 1
    else:
        print(notPalindrome)
        break
        
if start == end and a[start] == 'X':
    print(palindrome)

#solving using stacks
stack = []


for i in range(0,len(a)):
    if a[i] != 'X':
        stack.append(a[i])
    else:
        position = i + 1
        break
count = 0

for i in range(position,len(a)):
    if len(stack) != 0 and a[i] == stack[-1]:
        del stack[-1]
    else:
        count = 1
        break
#    else:
#        print(notPalindrome)
#        break
if len(stack) == 0 and count == 0:
    print(palindrome)
else:
    print(notPalindrome)
#else:
#    print(notPalindrome)









