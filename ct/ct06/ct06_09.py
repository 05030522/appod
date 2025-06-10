# 완주하지 못한 선수

def solution(participant, completion):
    # 1. 참가자 인원수를 세기 위한 빈 딕셔너리(해시)를 만듭니다.
    hash_dict = {}

    # 2. participant 리스트를 돌면서 각 이름의 인원수를 셉니다.
    # 동명이인이 있으면 +1, 처음 보는 이름이면 1로 등록합니다.
    for p in participant:
        hash_dict[p] = hash_dict.get(p, 0) + 1

    # 3. completion 리스트를 돌면서 완주한 선수의 인원수를 1씩 뺍니다.
    for c in completion:
        hash_dict[c] -= 1

    # 4. 딕셔너리에 값이 1로 남아있는 선수를 찾습니다.
    # 그 선수가 완주하지 못한 선수입니다.
    for key, val in hash_dict.items():
        if val == 1:
            return key
        




import collections
def solution(participant, completion):
    # 1. Counter를 이용해 participant 리스트를 딕셔너리 형태로 만듭니다.
    # 결과: Counter({'mislav': 2, 'stanko': 1, 'ana': 1})
    answer = collections.Counter(participant)

    # 2. Counter를 이용해 completion 리스트를 빼줍니다.
    # 결과: Counter({'mislav': 1, 'stanko': 0, 'ana': 0})
    answer -= collections.Counter(completion)

    # 3. Counter의 키(이름)들 중에서 값이 1인 첫 번째 키를 반환합니다.
    return list(answer.keys())[0]





# K번째수
def solution(array, commands):
    answer = []

    # commands 리스트에 있는 각 명령([i, j, k])을 순서대로 처리합니다.
    for command in commands:
        # command에서 i, j, k 값을 각각 변수에 저장합니다.
        i = command[0]
        j = command[1]
        k = command[2]

        # 1. 배열 자르기 (인덱스 보정: i-1)
        # 문제의 'i번째'는 파이썬 인덱스로 'i-1'이므로 i-1부터 j까지 자릅니다.
        sliced_array = array[i-1:j]

        # 2. 자른 배열 정렬하기
        sliced_array.sort()

        # 3. k번째 수 찾기 (인덱스 보정: k-1)
        # 정렬된 리스트의 'k번째' 수는 파이썬 인덱스로 'k-1'입니다.
        kth_number = sliced_array[k-1]

        # 4. 최종 결과 리스트에 추가하기
        answer.append(kth_number)

    return answer





def solution_short(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]



# 모의고사
def solution(answers):
    # 최종 정답을 담을 리스트
    answer = []
    
    # 1. 수포자들의 패턴과 점수판을 초기화합니다.
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]  # [1번, 2번, 3번] 수포자의 점수판

    # 2. 채점을 진행합니다.
    # enumerate를 사용해 정답지의 인덱스(i)와 정답(an)을 동시에 가져옵니다.
    for i, an in enumerate(answers):
        # 각 수포자의 답안과 정답이 일치하는지 "개별적으로" 확인합니다.
        
        # 1번 수포자 채점
        if an == p1[i % len(p1)]:
            scores[0] += 1
            
        # 2번 수포자 채점
        if an == p2[i % len(p2)]:
            scores[1] += 1
            
        # 3번 수포자 채점
        if an == p3[i % len(p3)]:
            scores[2] += 1

    # 3. 최고 득점자를 찾습니다.
    # 먼저, 가장 높은 점수(max_score)를 찾습니다.
    max_score = max(scores)
    
    # 점수판을 다시 확인하며, 가장 높은 점수를 받은 사람을 모두 찾습니다.
    for i in range(len(scores)):
        if scores[i] == max_score:
            # 학생 번호는 인덱스(i) + 1 이므로, i+1을 정답에 추가합니다.
            answer.append(i + 1)
            
    return answer