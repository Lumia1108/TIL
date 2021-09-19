N = int(input())
count = N
for i in range(N):
    word = input()
    chr = [word[0]]
    for j in range(1, len(word)):
        if word[j] == word[j-1]:
            pass
        elif word[j] in chr:
                count -= 1
                break
        else:
            chr.append(word[j])

print(count)