import re

with open('text.txt', encoding='utf-8') as file:
    t = file.read()

if len(t) == 0:
    print("\nВ обработку передан пустой файл.\nПреобразования пустого файла программой невозможны.")

else:
    en = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
    res = [re.split(r' ', i) for i in re.split(r'[.!?]\s+', re.sub(r'\n', '', t))]
    temp = []
    a = 0

    print("\n--------Результат работы программы--------\n")
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
        else:
            temp.append(f"\nПредложение {i+1} не содержит латинских символов")
            a += 1

    if a != len(res):
        print(*temp)
    else:
        print("Ни одно предложение не содержит латинских символов")
