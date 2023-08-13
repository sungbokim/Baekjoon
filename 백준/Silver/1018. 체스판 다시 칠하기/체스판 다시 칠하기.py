#체스판 다시 칠하기

n,m=map(int,input().split())

board=[]
count=[]
for j in range(n):
    board.append(list(input()))

for i in range(n-7):
    for j in range(m-7):
        B=0
        W=0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2==0:
                    if board[a][b] != 'B':
                        B+=1
                    if board[a][b] != 'W':
                        W+=1
                else:
                    if board[a][b] !='W':
                        B+=1
                    if board[a][b] !='B':
                        W+=1
        count.append(B)
        count.append(W)
print(min(count))

