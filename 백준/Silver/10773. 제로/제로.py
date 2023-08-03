#10773번  제로
import sys
from collections import deque
input=sys.stdin.readline

k=int(input())
q=deque()
for i in range(k):
    a=int(input())
    if a==0:
        q.pop()
    else:
        q.append(a)

print(sum(q))