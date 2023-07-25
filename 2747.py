#피보나치 수열
N=int(input())

pv=[]

for i in range(N):
    k=pv[i]+i
    pv.append(k)
print(pv)
