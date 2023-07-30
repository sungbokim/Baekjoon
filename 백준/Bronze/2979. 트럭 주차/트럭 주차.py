A,B,C=map(int,input().split())

time=[0]*101
my_list = []
for i in range(3):
    arrive, depart = map(int,(input().split()))
    for j in range(arrive,depart):
        time[j]+=1

one=time.count(1)*A
two=time.count(2)*B*2
three=time.count(3)*C*3

print(one+two+three)