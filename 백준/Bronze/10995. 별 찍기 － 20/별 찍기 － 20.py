n=int(input())

star="*"+" "
r_star=" "+"*"
for i in range(1,n+1):
    if i%2==1:
        print(star*n)
    else:
        print(r_star*n)