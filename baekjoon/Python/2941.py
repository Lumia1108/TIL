import re

alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in alphabet:
    word = re.sub(i, 'X', word)

print(len(word))