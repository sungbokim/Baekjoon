#로또
#입력빨리 받기
import sys
input=sys.stdin.readline

#내장함수로 조합,순열 사용하기
from itertools import combinations,permutations

#입력받기
while True:
    lst=list(map(int,input().split())) 
    if lst[0]==0:
        break

    del lst[0]
    
    lst_combi=list(combinations(lst,6))
    
    for i in lst_combi:
        print(*i)
    print()









