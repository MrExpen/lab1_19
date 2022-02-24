import re

with open('text.txt', encoding='utf-8') as file:
    t = file.read()
print(t, "\n")
en = [chr(ord('a') + i//2) if i % 2 == 0 else chr(ord('A') + i//2) for i in range((ord('z') - ord('a') + 1)*2)]
temp = re.split(r'[.\n!?][ ]', t)
res = [re.split(r' ', i) for i in temp]

print("--------Результат работы программы--------")
for i in range(len(res)):
    c = 0
    for j in range(len(res[i])):
        for w in en:
            if w in res[i][j]:
                res[i][j] = res[i][j].upper()
                c += 1
                break
    if c != 0:
        print(*res[i])
