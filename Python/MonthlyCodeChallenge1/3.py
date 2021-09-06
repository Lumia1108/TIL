# 월간 코드 챌린지 시즌1
# 두 개 뽑아서 더하기
# 풀이 2021.09.06

def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                pass
            else:
                answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer