name = "김철수"  # "김철수"라는 문자열 값을 name이라는 변수에 할당합니다.
age = 28      # 28이라는 정수 값을 age라는 변수에 할당합니다.
height = 175.5 # 175.5라는 실수 값을 height라는 변수에 할당합니다.
is_student = False # False라는 불리언 값을 is_student라는 변수에 할당합니다.
a, b, c = "짜루", 30, True #이렇게도 할당 가능
d = e = f = 10 #이렇게도 할당 가능

print(f"키는 {height}cm 입니다.") # 결과값 : 키는 175.5cm 입니다.

print("키는 {height}cm 입니다.") # 결과값 : 키는 {height}cm 입니다.

x = 10      # x는 정수(int) 타입이 됩니다. 결과값 : <class 'int'>
print(type(x))

x = "hello" # x는 문자열(str) 타입으로 변경됩니다. 결과값 : <class 'str'>
print(type(x))

x = 3.14    # x는 실수(float) 타입으로 변경됩니다. 결과값 : <class 'float'>
print(type(x))

import keyword
print(keyword.kwlist) #키워드 확인할 때

my_name = "파이썬"
print(my_name)       # 출력: 파이썬
print("안녕하세요,", my_name, "입니다.") # 출력: 안녕하세요, 파이썬 입니다.

num1 = 10
num2 = 20
sum_result = num1 + num2 # num1은 10으로, num2는 20으로 대체되어 10 + 20 연산
print(sum_result)    # 출력: 30

# if = 10
# print(if) > SyntaxError: invalid syntax 오류 발생

my_id = "  python_user  "
print(f"'{my_id.strip()}'") # 출력: 'python_user' (양쪽 공백 제거)
print(f"'{my_id.lstrip()}'") # 출력: 'python_user  ' (왼쪽 공백만 제거)
print(f"'{my_id.rstrip()}'") # 출력: '  python_user' (오른쪽 공백만 제거)

eng_text = "Hello Python"
print(eng_text.upper()) # 출력: HELLO PYTHON
print(eng_text.lower()) # 출력: hello python

text = "안녕하세요"
print(len(text)) # 출력: 5

fruits_string = "사과,바나나,딸기,포도"
fruits_list = fruits_string.split(',') # 쉼표(,)를 기준으로 나눔
print(fruits_list)        # 출력: ['사과', '바나나', '딸기', '포도']
print(fruits_list[0])     # 출력: 사과 (리스트의 첫 번째 요소)

sentence = "Life is too short"
words = sentence.split() # 공백을 기준으로 나눔
print(words)              # 출력: ['Life', 'is', 'too', 'short']

original_text = "나는 파이썬을 싫어해요."
modified_text = original_text.replace("싫어해요", "좋아해요")
print(modified_text) # 출력: 나는 파이썬을 좋아해요.

sample_text = "Hello, world! Hello, Python!"
print(sample_text.find("Hello"))  # 출력: 0 (첫 번째 Hello의 시작 위치)
print(sample_text.find("Python")) # 출력: 19
print(sample_text.find("Bye"))    # 출력: -1 (찾는 문자열이 없음)

# print(sample_text.index("Bye")) # 이 줄은 주석을 풀면 ValueError 발생!
# 문자열 메서드는 이것들 말고도 아주 많아요! 필요할 때마다 검색해서 찾아 쓰는 능력이 중요합니다.

is_active = True
is_greater = 5 > 3  # 5 > 3은 참(True)이므로 is_greater 변수에는 True가 저장됩니다.
is_equal = (10 == 20) # 10 == 20은 거짓(False)이므로 is_equal 변수에는 False가 저장됩니다.

print(is_active)     # 출력: True
print(is_greater)    # 출력: True
print(is_equal)      # 출력: False
print(type(is_active)) # 출력: <class 'bool'>

# 세부 목표 1 & 2 복습 문제

# 좋습니다! 약속대로 변수와 데이터 타입에 대한 간단한 복습 문제를 드릴게요. 다음 요구사항에 맞춰 파이썬 코드를 작성해 보세요.
# 다 작성하신 후에는 각 변수의 타입이 무엇일지, 그리고 최종 출력 결과가 어떨지 예상도 한번 해보세요!

# item_name 이라는 변수에 구매하려는 상품의 이름(예: "신라면")을 문자열로 저장하세요.
item_name = '신라면'
# item_price 라는 변수에 해당 상품의 가격(예: 1500)을 정수형으로 저장하세요.
item_price = 1500
# item_quantity 라는 변수에 구매할 수량(예: 3)을 정수형으로 저장하세요.
item_quantity = 3
# is_member 라는 변수에 회원 여부를 불리언 값(True 또는 False)으로 저장하세요.
is_member = True
# f-string을 사용하여 다음과 같은 형식으로 영수증 내용을 출력하세요: "구매 상품: [상품이름], 가격: [가격]원, 수량: [수량]개, 총액: [가격*수량]원, 회원여부: [회원여부]"
print(f"구매 상품: {item_name}, 가격: {item_price}원, 수량: {item_quantity}개, 총액: {item_price*item_quantity}원, 회원여부: {is_member}")
# item_name, item_price, item_quantity, is_member 변수의 데이터 타입을 각각 type() 함수를 사용하여 확인하고 한 줄에 하나씩 출력하세요.
print(type(item_name))
print(type(item_price))
print(type(item_quantity))
print(type(is_member))

a = 10
b = 3

print(f"{a} + {b} = {a + b}")         # 10 + 3 = 13
print(f"{a} - {b} = {a - b}")         # 10 - 3 = 7
print(f"{a} * {b} = {a * b}")         # 10 * 3 = 30
print(f"{a} / {b} = {a / b}")         # 10 / 3 = 3.333...
print(f"{a} // {b} = {a // b}")       # 10 // 3 = 3 (몫)
print(f"{a} % {b} = {a % b}")         # 10 % 3 = 1 (나머지)
print(f"{a} ** {b} = {a ** b}")       # 10 ** 3 = 1000 (10의 3제곱)