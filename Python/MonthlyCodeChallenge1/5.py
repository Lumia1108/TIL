# 월간 코드 챌린지 시즌1
# 이진 변환 반복하기
# 풀이 2021.09.08
import math

def solution(s):
    binCount = 0
    zeroCount = 0
    while s != '1':
        s = list(s)
        zeroCount += s.count('0')
        s = s.count('1')
        result = ''
        while s > 0:
            result = str(s % 2) + result
            s = math.floor(s / 2)
        s = result
        binCount += 1
    answer = [binCount, zeroCount]
    return answer