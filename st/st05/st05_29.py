# say_hello 함수 만들기 (정의)
def say_hello():
    print("안녕하세요!")
    print("파이썬 함수 공부를 시작합니다.")

# show_my_name 함수 만들기 (정의)
def show_my_name():
    print("제 이름은 커리어 컨설턴트입니다.")

# 이제 함수를 사용해봅시다 (호출)
say_hello()      # say_hello 함수 안의 코드들이 실행됩니다.
print("--- 중간 구분선 ---")
show_my_name()   # show_my_name 함수 안의 코드들이 실행됩니다.
say_hello()      # say_hello 함수를 또 호출할 수도 있어요! (재사용)

def greet_someone(name):  # 여기서 'name'이 매개변수입니다.
    print(f"안녕하세요, {name}님!")
    print("만나서 반갑습니다.")

# 함수 호출 시 매개변수 'name'에 값을 전달합니다.
greet_someone("Alice")  # "Alice"가 'name' 매개변수에 전달되는 인자입니다.
print("---")
greet_someone("Bob")    # "Bob"이 'name' 매개변수에 전달되는 인자입니다.

def greet_someone(name):  # 여기서 'name'이 매개변수입니다.
    print(f"안녕하세요, {name}님!")
    print("만나서 반갑습니다.")

# 함수 호출 시 매개변수 'name'에 값을 전달합니다.
greet_someone("Alice")  # "Alice"가 'name' 매개변수에 전달되는 인자입니다.
print("---")
greet_someone("Bob")    # "Bob"이 'name' 매개변수에 전달되는 인자입니다.

def add_numbers(num1, num2): # num1과 num2가 매개변수
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

add_numbers(5, 3)      # 5는 num1에, 3은 num2에 전달됩니다. (위치에 따라 전달 - 위치 인자)
add_numbers(100, 200)

def describe_pet(animal_type, pet_name):
    print(f"저는 {animal_type}을(를) 키웁니다.")
    print(f"이름은 {pet_name}입니다.")

# 위치 인자로 호출 (순서가 중요)
describe_pet("강아지", "뽀삐")
print("---")

# 키워드 인자로 호출 (순서가 바뀌어도 괜찮음)
describe_pet(pet_name="야옹이", animal_type="고양이")
print("---")

# 위치 인자와 키워드 인자 혼용 (위치 인자가 항상 먼저 와야 함)
describe_pet("햄스터", pet_name="햄토리")
# describe_pet(pet_name="짹짹이", "새") # 오류 발생! 키워드 인자 뒤에 위치 인자가 올 수 없음

def greet(name, message="안녕하세요"): # message 매개변수에 기본값 "안녕하세요" 지정
    print(f"{name}님, {message}!")

# message 인자를 전달하지 않으면 기본값 "안녕하세요" 사용
greet("Alice") # 출력: Alice님, 안녕하세요!

# message 인자를 전달하면 전달한 값 사용
greet("Bob", "좋은 아침입니다") # 출력: Bob님, 좋은 아침입니다!

# 기본값이 있는 매개변수는 뒤쪽에 와야 함
# def wrong_greet(message="Hi", name): # 오류 발생!
#     print(f"{name}님, {message}!")

def add(num1, num2):
    sum_result = num1 + num2
    return sum_result  # 계산된 합(sum_result)을 반환합니다.

# 함수 호출하고, 반환된 값을 변수에 저장
result1 = add(10, 5)
print(f"10 + 5의 결과: {result1}") # 출력: 10 + 5의 결과: 15

result2 = add(100, 200)
print(f"100 + 200의 결과: {result2}") # 출력: 100 + 200의 결과: 300

# 반환된 값을 바로 다른 연산에 사용할 수도 있어요.
final_result = add(3, 4) * 2 # add(3, 4)는 7을 반환하고, 7 * 2 = 14
print(f"(3 + 4) * 2 = {final_result}") # 출력: (3 + 4) * 2 = 14

def calculate_two(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    return addition, subtraction # 덧셈 결과와 뺄셈 결과를 함께 반환

# 반환된 여러 값을 여러 변수에 나누어 받기 (튜플 언패킹)
sum_val, diff_val = calculate_two(10, 3)
print(f"덧셈 결과: {sum_val}, 뺄셈 결과: {diff_val}")
# 출력: 덧셈 결과: 13, 뺄셈 결과: 7

# 반환된 값을 하나의 변수(튜플)로 받기
results_tuple = calculate_two(7, 2)
print(f"결과 튜플: {results_tuple}") # 출력: 결과 튜플: (9, 5)
print(f"튜플의 첫 번째 요소: {results_tuple[0]}") # 출력: 튜플의 첫 번째 요소: 9
print(f"튜플의 두 번째 요소: {results_tuple[1]}") # 출력: 튜플의 두 번째 요소: 5

def print_greeting(name):
    print(f"안녕하세요, {name}님!")
    # 이 함수에는 return 문이 없습니다.

result_of_greeting = print_greeting("Python") # 함수는 실행되지만, 반환하는 값이 없음
print(f"print_greeting 함수의 반환 값: {result_of_greeting}")
# 출력:
# 안녕하세요, Python님!
# print_greeting 함수의 반환 값: None

def do_nothing():
    return # 값 없이 return만 사용

result_of_nothing = do_nothing()
print(f"do_nothing 함수의 반환 값: {result_of_nothing}")
# 출력: do_nothing 함수의 반환 값: None