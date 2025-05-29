empty_list = []
print(empty_list)       # 출력: []
print(type(empty_list)) # 출력: <class 'list'>

numbers = [1, 2, 3, 4, 5]
print(numbers)          # 출력: [1, 2, 3, 4, 5]

mixed_list = [1, "안녕", 3.14, True]
print(mixed_list)       # 출력: [1, '안녕', 3.14, True]

# 인덱싱
my_list = ["사과", "바나나", "딸기", "포도"]
print(my_list[0])  # 첫 번째 요소 -> 출력: 사과
print(my_list[1])  # 두 번째 요소 -> 출력: 바나나
print(my_list[3])  # 네 번째 요소 -> 출력: 포도

my_list = ["사과", "바나나", "딸기", "포도"]
print(my_list[-1]) # 맨 마지막 요소 -> 출력: 포도
print(my_list[-2]) # 뒤에서 두 번째 요소 -> 출력: 딸기

# 슬라이싱
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])  # 인덱스 2부터 인덱스 4까지 (5는 포함 안됨) -> 출력: [2, 3, 4]
print(numbers[0:3])  # 인덱스 0부터 인덱스 2까지 -> 출력: [0, 1, 2]
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[:3])   # 처음부터 인덱스 2까지 -> 출력: [0, 1, 2]
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[3:])   # 인덱스 3부터 끝까지 -> 출력: [3, 4, 5]
numbers = [0, 1, 2, 3, 4, 5]
copy_numbers = numbers[:]
print(copy_numbers)  # 출력: [0, 1, 2, 3, 4, 5]
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[-3:-1]) # 뒤에서 3번째부터 뒤에서 1번째 전까지 -> 출력: [3, 4]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:10:2]) # 인덱스 0부터 9까지, 2칸 간격으로 -> 출력: [0, 2, 4, 6, 8]
print(numbers[::3])    # 전체에서 3칸 간격으로 -> 출력: [0, 3, 6, 9]
print(numbers[::-1])   # 전체를 거꾸로 -> 출력: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

my_list = ["사과", "바나나", "딸기"]
print(f"변경 전: {my_list}") # 변경 전: ['사과', '바나나', '딸기']

my_list[1] = "망고" # 인덱스 1의 "바나나"를 "망고"로 변경
print(f"변경 후: {my_list}") # 변경 후: ['사과', '망고', '딸기']

numbers = [1, 2, 3]
print(f"추가 전: {numbers}") # 추가 전: [1, 2, 3]

numbers.append(4) # 리스트 맨 뒤에 4를 추가
print(f"추가 후: {numbers}") # 추가 후: [1, 2, 3, 4]

numbers.append(5)
print(f"또 추가 후: {numbers}") # 또 추가 후: [1, 2, 3, 4, 5]

fruits = ["오렌지", "포도", "수박", "키위"]
list_length = len(fruits)
print(f"과일 리스트: {fruits}")
print(f"과일의 종류는 총 {list_length}가지 입니다.") # 과일의 종류는 총 4가지 입니다.

empty_one = []
print(f"빈 리스트의 길이: {len(empty_one)}") # 빈 리스트의 길이: 0