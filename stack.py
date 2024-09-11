# Python program to (Last in first out)
# demonstrate stack implementation
# using list

stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')

print('Initial stack')
print(stack)

# Pop() function 
element=stack.pop()
print("pop",element)

# Peek()function 
topElement=stack[-1]
print("Peek",topElement)

# isEmpty () function
notEmpty=not bool(stack)
print("notEmpty",notEmpty)

# size
print("size",len(stack))