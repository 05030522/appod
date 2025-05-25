# [PCCE 기출문제] 6번 / 물 부족
def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = usage+(usage * change[i]/100)
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1

# [PCCE 기출문제] 8번 / 닉네임 규칙
def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    while len(answer) < 4:
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer

# [PCCE 기출문제] 1번 / 출력
string_msg = "Spring is beginning"
int_val = 3
string_val = "3"

print(string_msg)
print(int_val + 10)
print(string_val + "10")

# [PCCE 기출문제] 2번 / 피타고라스의 정리
a = int(input())
c = int(input())

b_square = c**2 - a**2
print(b_square)