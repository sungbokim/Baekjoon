color=[]
for i in range(3):
    color.append(input())

dic_a={'black':[0,10**0],'brown':[1,10**1],'red':[2,10**2],'orange':[3,10**3],'yellow':[4,10**4],'green':[5,10**5],'blue':[6,10**6],'violet':[7,10**7],'grey':[8,10**8],'white':[9,10**9]}

first=dic_a[color[0]]
first=first[0]
second=dic_a[color[1]]
second=second[0]
third=dic_a[color[2]]
third=third[1]

num=str(first)+str(second)
num=int(num)
print(third*num)