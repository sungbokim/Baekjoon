#에너그램 만들기
alphabet = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for abc in alphabet:
    dic[abc] = 0

word1 = input()
for letter in word1:
    dic[letter] += 1

word2 = input()
for letter in word2:
    dic[letter] -= 1

ans = 0
for i in dic:
    ans += abs(dic[i])

print(ans)