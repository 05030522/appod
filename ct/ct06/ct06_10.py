# 체육복
def solution(n, lost, reserve):
    # set으로 변환하여 중복 제거 및 차집합 연산 수행
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    for r in sorted(list(real_reserve)):
        if r - 1 in real_lost: # 앞번호 학생에게 빌려줄 수 있는 경우
            real_lost.remove(r - 1)
        elif r + 1 in real_lost: # 뒷번호 학생에게 빌려줄 수 있는 경우
            real_lost.remove(r + 1)

    return n - len(real_lost)




import math

# 기능개발
def solution(progresses, speeds):
    answer = []
    days_left = []
    for i in range(len(progresses)):
        days = math.ceil((100 - progresses[i])/speeds[i])
        days_left.append(days)

    max_day = days_left[0]
    count = 1
    for i in range(1, len(days_left)):
        if days_left[i] <= max_day:
            count += 1
        elif days_left[i] > max_day:
            answer.append(count)
            max_day = days_left[i]
            count = 1
    answer.append(count)

    return answer
