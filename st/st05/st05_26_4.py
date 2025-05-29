my_set1 = {1, 2, 3, 4, 5}
my_set2 = {"apple", "banana", "cherry"}
my_set3 = {1, "hello", 3.14, True} # 다양한 타입 저장 가능

print(my_set1)       # 출력 예시: {1, 2, 3, 4, 5} (순서는 바뀔 수 있음)
print(my_set2)       # 출력 예시: {'cherry', 'apple', 'banana'}
print(type(my_set1)) # 출력: <class 'set'>

my_set1 = {1, 2, 3, 4, 5}
my_set2 = {"apple", "banana", "cherry"}
my_set3 = {1, "hello", 3.14, True} # 다양한 타입 저장 가능

print(my_set1)       # 출력 예시: {1, 2, 3, 4, 5} (순서는 바뀔 수 있음)
print(my_set2)       # 출력 예시: {'cherry', 'apple', 'banana'}
print(type(my_set1)) # 출력: <class 'set'>

empty_set = set()    # 이렇게 해야 빈 세트!
empty_dict = {}      # 이건 빈 딕셔너리!

print(empty_set)       # 출력: set()
print(type(empty_set)) # 출력: <class 'set'>
print(type(empty_dict))# 출력: <class 'dict'>

my_list = [1, "a", "b", "a", 2, 2]
set_from_list = set(my_list)
print(set_from_list) # 출력 예시: {1, 2, 'b', 'a'} (순서 무관, 중복 제거)

my_string = "hello"
set_from_string = set(my_string)
print(set_from_string) # 출력 예시: {'e', 'h', 'l', 'o'}

numbers = {1, 2, 3}
numbers.add(4)
print(numbers) # 출력 예시: {1, 2, 3, 4}
numbers.add(2) # 이미 있는 2를 또 추가해도 변함 없음 (중복 불가)
print(numbers) # 출력 예시: {1, 2, 3, 4}

numbers = {1, 2, 3, 4}
numbers.remove(3)
print(numbers) # 출력 예시: {1, 2, 4}
# numbers.remove(5) # 이 줄은 주석 풀면 KeyError 발생! (5가 없음)

numbers.discard(4)
print(numbers) # 출력 예시: {1, 2}
numbers.discard(5) # 5가 없지만 오류 발생 안 함
print(numbers) # 출력 예시: {1, 2}

my_set = {"red", "green", "blue"}
print(len(my_set)) # 출력: 3

my_set = {10, 20, 30}
print(10 in my_set)    # 출력: True
print(40 not in my_set) # 출력: True

# 1. 'greet'라는 이름의 함수 만들기 (정의)
def greet():
    print("안녕하세요! 함수를 처음 만들어봤어요.")
    print("만나서 반갑습니다!")

# 2. 'greet' 함수 사용하기 (호출)
print("함수를 호출해볼게요...")
greet() # greet 함수가 실행되면서 안에 있는 print문들이 동작합니다.

print("\n한 번 더 호출해볼까요?")
greet() # 필요할 때마다 이렇게 여러 번 호출할 수 있어요!