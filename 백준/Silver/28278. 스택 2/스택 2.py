import sys
input=sys.stdin.readline
from collections import deque

q=deque()
n=int(input())
res=[]
for _ in range(n):
    cmd=list(map(int,input().split()))
    # cmd=input().split()
    if cmd[0]==1:
        q.append(cmd[1])
    elif cmd[0]==2:
        if len(q)>0:
            # q.pop()
            print(q.pop())
        else: 
            print(-1)
    elif cmd[0]==3:
        print(len(q))
    elif cmd[0]==4:
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]==5:
        if len(q)> 0:
            print(q[-1])
        else:
            print(-1)




