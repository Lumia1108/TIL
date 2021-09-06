# 월간 코드 챌린지 시즌1
# 삼각 달팽이
# 풀이 2021.09.06

def solution(n):
    answer = []
    tower = []
    for i in range(n):
        arr = []
        for j in range(i+1):
            arr.append(0)
        tower.append(arr)
    x = 0
    y = 0
    xy = 0
    num = 1
    while n > 0:
        if xy % 3 == 0:
            for i in range(n):
                tower[y][x] = num
                num += 1
                y += 1
            print(x, y)
            y -= 1
            x += 1
        if xy % 3 == 1:
            for i in range(n):
                tower[y][x] = num
                num += 1
                x += 1
            print(x, y)
            x -= 2
            y -= 1
        if xy % 3 == 2:
            for i in range(n):
                tower[y][x] = num
                num += 1
                x -= 1
                y -= 1
            print(x, y)
            x += 1
            y += 2
        n -= 1
        xy += 1
    for i in tower:
        answer += i
    return answer


print(solution(6))