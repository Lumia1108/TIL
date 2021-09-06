# 월간 코드 챌린지 시즌1
# 3진법 뒤집기
# 풀이 2021.09.06

import math

def solution(n):
    result = ''
    while n > 0:
        result += str(n % 3)
        n = math.floor(n / 3)
    answer = int(result, 3)
    return answer