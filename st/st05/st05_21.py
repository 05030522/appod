# if 조건식:
    # 조건식이 True일 때 실행될 코드
#     실행문1
#     실행문2
# if 문과 관계없이 다음으로 실행될 코드 (들여쓰기 없음)

age = 20
if age >= 19:
    print("성인입니다.") # 조건 (age >= 19)이 True이므로 이 줄이 실행됩니다.
print("프로그램을 종료합니다.") # 이 줄은 if문의 조건과 관계없이 항상 실행됩니다.

temperature = 5
if temperature < 10:
    print("날씨가 쌀쌀하네요. 외투를 챙기세요.") # 조건이 True이므로 실행됩니다.

#     if 조건식:
    # 조건식이 True일 때 실행될 코드
#     실행문A1
#     실행문A2
# else:
    # 조건식이 False일 때 실행될 코드
    # 실행문B1
    # 실행문B2
# if-else 문과 관계없이 다음으로 실행될 코드

age = 15
if age >= 19:
    print("성인입니다. 입장이 가능합니다.")
else:
    print("미성년자입니다. 입장이 불가능합니다.") # age가 15이므로 if 조건(15 >= 19)은 False. 따라서 else 블록이 실행됩니다.

money = 10000
price = 12000
if money >= price:
    print("구매 가능합니다.")
else:
    print(f"구매할 수 없습니다. {price - money}원이 부족합니다.") # money < price 이므로 else 블록이 실행됩니다.

    score = 85

if score >= 90:
    grade = "A"
elif score >= 80: # 90점 미만이지만 80점 이상인 경우
    grade = "B"
elif score >= 70: # 80점 미만이지만 70점 이상인 경우
    grade = "C"
elif score >= 60: # 70점 미만이지만 60점 이상인 경우
    grade = "D"
else:             # 60점 미만인 경우
    grade = "F"

print(f"점수: {score}, 학점: {grade}") # score가 85이므로 두 번째 elif 조건(score >= 80)이 True. 따라서 grade는 "B"가 됩니다.

# 조건식이 위에서 확인되면 아래까지는 비교도 안해봄

# 문제: 사용자로부터 정수 하나를 input()으로 입력받아, 그 숫자가 양수인지, 음수인지, 아니면 0인지를 판별하여 출력하는 프로그램을 작성해 보세요.

# 숫자가 0보다 크면 "입력한 숫자는 양수입니다."
# 숫자가 0보다 작으면 "입력한 숫자는 음수입니다."
# 숫자가 0이면 "입력한 숫자는 0입니다."

a = input("정수를 입력해주세요.")
num=float(a)
if num>0:
    print("입력한 숫자는 양수입니다.")
elif num<0:
    print("입력한 숫자는 음수입니다.")
else:
    print("입력한 숫자는 0입니다.")