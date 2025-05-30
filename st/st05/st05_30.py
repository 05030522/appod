# # 1. calcul 모듈 불러오기
# #    (파일 이름에서 .py 확장자는 제외하고 모듈 이름만 씁니다)
# import st05_30_calcul

# # 2. my_calculator 모듈의 함수와 변수 사용하기
# num1 = 100
# num2 = 50

# # 모듈 이름.함수이름() 형태로 호출
# sum_result = st05_30_calcul.add(num1, num2)
# diff_result = st05_30_calcul.subtract(num1, num2)
# prod_result = st05_30_calcul.multiply(num1, num2)

# print(f"{num1} + {num2} = {sum_result}")
# print(f"{num1} - {num2} = {diff_result}")
# print(f"{num1} * {num2} = {prod_result}")

# # 모듈 이름.변수이름 형태로 사용
# print(f"원주율 (st05_30_calcul 모듈에서 가져옴): {st05_30_calcul.pi}")

# # 모듈의 다른 함수도 호출
# st05_30_calcul.greet()

################################################################################################################

# # st05_30_calcul 모듈에서 add 함수와 pi 변수만 직접 가져오기
# from st05_30_calcul import add, pi

# # 이제 모듈 이름 없이 바로 사용 가능
# result = add(10, 20)
# print(f"10 + 20 = {result}")
# print(f"원주율: {pi}")

# # subtract 함수는 직접 가져오지 않았으므로 바로 사용할 수 없어요.
# # diff = subtract(5, 2) # 이 줄은 NameError 발생!


################################################################################################################


# # st05_30_calcul 모듈의 모든 것을 가져오기
# from st05_30_calcul import *

# # 모듈 이름 없이 바로 사용 가능
# result_sum = add(7, 3) # st05_30_calcul.add
# result_sub = subtract(7, 3) # st05_30_calcul.subtract
# print(f"합: {result_sum}, 차: {result_sub}")
# print(f"파이 값: {pi}") # st05_30_calcul.pi
# # ⚠️ 사용 시 매우 주의! (일반적으로 권장하지 않음)

################################################################################################################

# st05_30_calcul 모듈을 mc 라는 별명으로 가져오기
import st05_30_calcul as mc

sum_val = mc.add(5, 4)
print(f"5 + 4 = {sum_val}")
print(f"원주율 (mc 모듈): {mc.pi}")

# 원래 이름인 st05_30_calcul 더 이상 사용할 수 없어요 (이 import 문에서는)
# print(st05_30_calcul.author) # NameError 발생 가능

# my_calculator 모듈에서 add 함수는 my_add로, pi 변수는 MY_PI로 가져오기
from st05_30_calcul import add as my_add, pi as MY_PI

result = my_add(100, 1)
print(f"덧셈 결과: {result}")
print(f"나만의 파이: {MY_PI}")

# 원래 이름인 add나 pi는 직접 사용할 수 없어요.
# print(add(1,1)) # NameError
# print(pi) # NameError

# 모듈의 상단에는 함수, 클래스, 변수 정의 등을 둡니다.
def my_function():
    print("함수가 호출되었습니다.")

variable = "모듈 변수"

# 이 아래 부분이 핵심입니다.
if __name__ == "__main__":
    # 이 블록 안의 코드는 이 파일이 직접 실행될 때만 실행됩니다.
    # 다른 파일에서 이 모듈을 import 할 때는 실행되지 않아요.
    print("이 파일이 직접 실행되었습니다!")
    my_function()
    print(f"모듈 변수 값: {variable}")
    # 여기에 모듈 테스트 코드나 예제 코드를 넣으면 좋습니다.

# my_project/                  <-- 프로젝트 최상위 폴더
# ├── main_program.py          <-- 패키지를 사용할 메인 프로그램
# └── my_package/              <-- 'my_package' 라는 이름의 패키지 폴더
#     ├── __init__.py          <-- 이 폴더가 패키지임을 알림 (내용은 비어있어도 됨)
#     ├── module1.py           <-- 패키지 안의 모듈 1
#     └── module2.py           <-- 패키지 안의 모듈 2
# 위와 같은 패키지 일시

####################################1번####################################
# # main_program.py
# import my_package.module1
# # 사용할 때는 패키지이름.모듈이름.함수이름() 형태로 사용
# my_package.module1.some_function_in_module1()

# #####################################2번####################################
# # main_program.py
# from my_package import module1

# # 사용할 때는 모듈이름.함수이름() 형태로 사용
# module1.some_function_in_module1()

# #####################################3번####################################
# # main_program.py
# from my_package.module1 import some_function_in_module1
# # 사용할 때는 함수이름() 형태로 바로 사용
# some_function_in_module1()

# main_program.py

# # 방법 1
# import my_package.module1
# my_package.module1.greet_module1()

# # 방법 2
# from my_package import module1
# module1.greet_module1()

# # 방법 3
# from my_package.module1 import greet_module1
# greet_module1()

# 숫자를 입력해야 하는데 사용자가 글자를 입력했을 때 (ValueError)
# 0으로 어떤 숫자를 나누려고 할 때 (ZeroDivisionError)
# 리스트에 없는 인덱스를 사용하려고 할 때 (IndexError)
# 딕셔셔너리에 없는 키를 사용하려고 할 때 (KeyError)

# try:
#     # 예외가 발생할 수 있는 코드
#     실행할_코드
# except 발생할_수_있는_오류의_종류:
#     # 위에서 지정한 오류가 발생했을 때 실행될 코드
#     오류_처리_코드

try:
    num_str = input("나눌 숫자를 입력하세요: ")
    num = int(num_str)  # 여기서 ValueError가 발생할 수 있음 (문자 입력 시)
    result = 10 / num   # 여기서 ZeroDivisionError가 발생할 수 있음 (0 입력 시)
    print(f"10 / {num} = {result}")

except ValueError:
    print("앗! 숫자가 아닌 것을 입력하셨네요. 숫자를 입력해주세요!")
except ZeroDivisionError:
    print("앗! 0으로는 나눌 수 없어요.")
except Exception as e: # 혹시 모를 다른 모든 종류의 예외를 잡고 싶을 때 (선택 사항)
    print(f"예상치 못한 오류가 발생했습니다: {e}")

print("프로그램이 (어쨌든) 종료됩니다.")