N = int(input())
i = 1
distance = 1
road = 1
while road < N:
    road += i * 6
    i += 1
print(i)