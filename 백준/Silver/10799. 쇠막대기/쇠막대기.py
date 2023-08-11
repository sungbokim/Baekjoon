#괄호
T = list(input())


stack = []
pipe=0

for i in range(len(T)):
    if T[i] == '(':
        stack.append(T[i])

    else:
        if T[i-1] == '(': 
            stack.pop()
            pipe += len(stack)

        else:
            stack.pop() 
            pipe += 1 

print(pipe)



