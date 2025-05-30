# st05_30_calcul.py 파일의 맨 위에 추가
print("st05_30_calcul 모듈이 로드되었습니다!")

# 모듈 변수
pi = 3.14159
author = "나만의 계산기 모듈"

# 모듈 함수
def add(a, b):
    """두 수를 더한 결과를 반환합니다."""
    return a + b

def subtract(a, b):
    """a에서 b를 뺀 결과를 반환합니다."""
    return a - b

def multiply(a, b):
    """두 수를 곱한 결과를 반환합니다."""
    return a * b

def greet():
    print(f"안녕하세요! '{author}' 입니다.")

if __name__ == "__main__":
    print("모듈을 직접 실행했습니다. 테스트를 시작합니다...")
    
    # 함수 테스트
    result_add = add(10, 5)
    print(f"add(10, 5) 결과: {result_add}")
    
    result_sub = subtract(10, 5)
    print(f"subtract(10, 5) 결과: {result_sub}")
    
    print(f"모듈 변수 pi: {pi}")
    greet()
    print("테스트 종료.")