# 프로그래머스 월간 코드 챌린지 시즌1
# 내적
# 풀이 2021.09.06

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer