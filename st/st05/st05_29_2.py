def add(a, b):
    """두 수 a와 b를 더한 결과를 반환합니다."""
    return a + b

def greet(name):
    """주어진 이름에게 간단한 인사를 출력합니다."""
    print(f"안녕하세요, {name}님!")

    def calculate_rectangle_area(width, height):
    """직사각형의 너비와 높이를 받아 넓이를 계산합니다.

    매개변수:
        width (int 또는 float): 직사각형의 너비입니다.
        height (int 또는 float): 직사각형의 높이입니다.

    반환 값:
        int 또는 float: 계산된 직사각형의 넓이입니다.
                       너비나 높이가 음수이면 None을 반환합니다.
    """
    if width < 0 or height < 0:
        return None
    return width * height

def add(a, b):
    """두 수 a와 b를 더한 결과를 반환합니다."""
    return a + b

print(add.__doc__)
# 출력: 두 수 a와 b를 더한 결과를 반환합니다.

def calculate_rectangle_area(width, height):
    """직사각형의 너비와 높이를 받아 넓이를 계산합니다.

    매개변수:
        width (int 또는 float): 직사각형의 너비입니다.
        height (int 또는 float): 직사각형의 높이입니다.

    반환 값:
        int 또는 float: 계산된 직사각형의 넓이입니다.
                       너비나 높이가 음수이면 None을 반환합니다.
    """
    if width < 0 or height < 0:
        return None
    return width * height

help(calculate_rectangle_area)
# 출력:
# Help on function calculate_rectangle_area in module __main__:
#
# calculate_rectangle_area(width, height)
#     직사각형의 너비와 높이를 받아 넓이를 계산합니다.
#
#     매개변수:
#         width (int 또는 float): 직사각형의 너비입니다.
#         height (int 또는 float): 직사각형의 높이입니다.
#
#     반환 값:
#         int 또는 float: 계산된 직사각형의 넓이입니다.
#                        너비나 높이가 음수이면 None을 반환합니다.

def my_function():
    local_var = 10  # my_function 안에서만 유효한 지역 변수
    print(f"함수 안에서 local_var: {local_var}")

my_function()
# print(f"함수 밖에서 local_var: {local_var}") # 이 줄은 주석을 풀면 NameError 발생!
                                        # 함수 밖에서는 local_var를 모릅니다.

global_var = 100  # 전역 변수

def show_global():
    print(f"함수 안에서 global_var 읽기: {global_var}") # 함수 안에서 전역 변수를 읽을 수 있습니다.

def another_function():
    # global_var = 200 # 이렇게 하면 아래 설명할 '새로운 지역 변수'가 됩니다.
    print(f"다른 함수 안에서 global_var 읽기: {global_var}")

show_global()
another_function()
print(f"함수 밖에서 global_var: {global_var}")

global_val = 50

def try_to_modify_global():
    global_val = 5  # 이것은 'global_val'이라는 이름의 '새로운 지역 변수'를 만듭니다.
                    # 전역 변수 global_val과는 다른 변수예요!
    print(f"함수 안에서의 global_val (지역 변수): {global_val}")

try_to_modify_global()
print(f"함수 실행 후 전역 변수 global_val: {global_val}") # 여전히 50이 출력됩니다!
# 만약 함수 안에서 전역 변수와 같은 이름의 변수에 값을 할당하려고 하면, 파이썬은 기본적으로 그 이름으로 새로운 지역 변수를 만듭니다.
# 전역 변수의 값은 바뀌지 않아요. 이것을 이름 가리기(Shadowing) 라고도 합니다.

global_val_to_change = 77

def actually_modify_global():
    global global_val_to_change  # "이제부터 global_val_to_change는 전역 변수를 의미해!"
    global_val_to_change = 777
    print(f"함수 안에서 수정한 global_val_to_change: {global_val_to_change}")

print(f"함수 호출 전 global_val_to_change: {global_val_to_change}")
actually_modify_global()
print(f"함수 호출 후 global_val_to_change: {global_val_to_change}") # 777로 바뀐 것을 볼 수 있습니다!

def add(a, b):
    c = a+b
    return c

def subtract(a, b):
    c = a-b
    return c

def multiply(a, b):
    c = a*b
    return c

def divide(a, b):
    if b==0:
        return print("0으로 나눌 수 없습니다.") # 순서 매우 중요!!
    c = a/b
    return c

num_1 = input("첫 번째 숫자를 입력하세요")
num_2 = input("두 번째 숫자를 입력하세요")
num1 = float(num_1)
num2 = float(num_2)

abc = input("원하는 연산자를 입력하세요")

def calculator(num1, num2, abc):
    if abc=="+":
        return add(num1, num2)
    elif abc=="-":
        return subtract(num1, num2)
    elif abc=="*":
        return multiply(num1, num2)
    elif abc=="/":
        return divide(num1, num2)
    else:
        return "잘못된 연산자입니다." # 문자열을 직접 반환
result = calculator(num1, num2, abc)

try:
    # 사용자가 입력한 문자열을 숫자로 변환 시도
    num1 = float(num_1)
    num2 = float(num_2)

    # 숫자 변환에 성공했을 때만 계산기 함수 호출 및 결과 출력
    calculation_result = calculator(num1, num2, abc)
    print(f"계산 결과: {calculation_result}")

except ValueError:
    # float() 변환 중 ValueError가 발생하면 이 부분이 실행됨
    print("오류: 입력한 값이 숫자가 아닙니다. 정확한 숫자를 입력해주세요.")