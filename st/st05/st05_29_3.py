# 1. math 모듈을 현재 파일로 불러오기 (가져오기)
import math

# 2. math 모듈 안의 기능 사용하기
# math 모듈 안에 있는 pi (원주율) 라는 이름의 상수 값 사용
print(f"원주율 파이(pi)의 값: {math.pi}")

# math 모듈 안에 있는 sqrt() 라는 이름의 함수 사용 (제곱근 구하기)
number = 16
square_root = math.sqrt(number)
print(f"{number}의 제곱근: {square_root}")

# math 모듈 안에 있는 ceil() 함수 사용 (올림)
num_float = 3.14
print(f"{num_float}의 올림: {math.ceil(num_float)}")

