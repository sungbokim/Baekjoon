from collections import deque

lst= deque()
answer = []

x, y = map(int, input().split())

for i in range(1, x+1):
    lst.append(i)

while lst:
    for i in range(y-1):
        lst.append(lst.popleft())
    answer.append(lst.popleft())

print("<",end='')
for i in range(len(answer)-1):
    print("%d, "%answer[i], end='')
print(answer[-1], end='')
print(">")