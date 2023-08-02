#바이러스
from collections import deque
import sys

input_sys=sys.stdin.readline

def bfs(go,com,visited):
    queue=deque([com])
    visited[com]=True
    cnt=0
    while queue:
        v=queue.popleft()
        for i in go[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                cnt+=1
    print(cnt)
    return

com=int(input_sys())
network=int(input_sys())
go=[[] for _ in range(com+1)]
for i in range(network):
    start,end=map(int,input().split())
    go[start].append(end)
    go[end].append(start)

visited=[False]*(com+1)

bfs(go,1,visited)