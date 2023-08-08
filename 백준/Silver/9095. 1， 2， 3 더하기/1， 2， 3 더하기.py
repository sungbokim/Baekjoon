#1,2,3더하기


t=int(input())

for _ in range(t):
    list=[1,2,4]
    n=int(input())

    if n==1:
        print(list[0])
    elif n==2:
        print(list[1])
    elif n==3:
        print(list[2])
    else:
        for i in range(4,n+1):
            list.append(list[-2]+list[-3]+list[-1])
        print(list[-1]) 
    
            
       
