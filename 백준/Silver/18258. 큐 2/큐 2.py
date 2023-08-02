from collections import deque
N=int(input())
q=deque()
result=[]
for i in range(N):
    cmd=input().split()
    if cmd[0]=='push':
        q.append(int(cmd[1]))
    elif cmd[0]=='pop':
         if len(q)==0:
            result.append(-1)
         else:
            result.append(q.popleft())
    elif cmd[0]=='size':
        result.append(len(q))
    elif cmd[0] == 'empty':
        if len(q)==0:
            result.append(1)
        else: 
            result.append(0)
    elif cmd[0]=='front':
        if len(q)==0:
            result.append(-1)
        else:
            result.append(q[0])
    elif cmd[0]=='back':
        if len(q)==0:
            result.append(-1)
        else:
            result.append(q[-1])

print('\n'.join(map(str, result)))