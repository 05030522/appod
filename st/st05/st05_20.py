# 사용자에게 이름을 묻고 입력받기
name = input("당신의 이름은 무엇인가요? ")
print(f"오, {name}님이시군요! 반갑습니다.")

# 사용자에게 나이를 묻고 입력받기
age_str = input("나이가 어떻게 되시나요? ")
print(f"입력하신 나이(문자열): {age_str}")
print(f"나이의 데이터 타입: {type(age_str)}") # <class 'str'> 임을 확인!

# age_str = input("나이를 입력하세요: ") # 예: 사용자가 "30" 입력
# ten_years_later = age_str + 10  # 이 부분에서 TypeError 발생! (문자열과 정수를 더하려고 함)
# print(ten_years_later)

num_str = "100"
num_int = int(num_str)
print(f"문자열 '{num_str}'의 타입: {type(num_str)}")
print(f"정수형으로 변환된 {num_int}의 타입: {type(num_int)}")
print(f"{num_int} + 50 = {num_int + 50}") # 이제 덧셈 가능!

float_num = 3.14
int_from_float = int(float_num)
print(f"{float_num}을 정수로 변환: {int_from_float}") # 결과: 3 (소수점 이하 버림)

# print(int("hello")) # 이 줄은 ValueError 발생!

num_str2 = "25.5"
num_float = float(num_str2)
print(f"문자열 '{num_str2}'의 타입: {type(num_str2)}")
print(f"실수형으로 변환된 {num_float}의 타입: {type(num_float)}")
print(f"{num_float} * 2 = {num_float * 2}")

int_val = 7
float_from_int = float(int_val)
print(f"{int_val}을 실수로 변환: {float_from_int}") # 결과: 7.0

# print(float("world")) # 이 줄은 ValueError 발생!

number = 123
num_to_str = str(number)
print(f"숫자 {number}의 타입: {type(number)}")
print(f"문자열로 변환된 '{num_to_str}'의 타입: {type(num_to_str)}")
print("결과: " + num_to_str) # 문자열끼리 덧셈(이어붙이기) 가능

is_true = True
bool_to_str = str(is_true)
print(f"불리언 {is_true}를 문자열로 변환: '{bool_to_str}', 타입: {type(bool_to_str)}")

name1 = input("이름을 입력하세요")
age1 = input("나이를 입력하세요")
int_age1 = int(age1)
ten_year_ago_age1 = int_age1+10
print(f"{name1}님의 10년 후 나이는 {ten_year_ago_age1}세 입니다.")

item_count = 5
str_item_count=str(item_count)
print("총 개수:"+str_item_count+"1개")

# a = input("안녕")
# b=int(a)
# print(b)