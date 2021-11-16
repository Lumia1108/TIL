i = 1 # line number
j = 1
X = int(input())
while X > j:
    i += 1
    j += i
X -= (j - i)
value = 1
if i % 2 == 0:
    value = 1
    for k in range(X - 1):
        value += 1
    print('%d/%d' % (value, i + 1 - value))
else:
    value = i
    for k in range(X - 1):
        value -= 1
    print('%d/%d' % (value, i + 1 - value))