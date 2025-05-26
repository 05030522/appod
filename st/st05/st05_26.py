my_friends = ["Alice", "Bob", "Charlie"]
print(f"삽입 전: {my_friends}")

# 인덱스 1 위치에 "David"를 삽입
my_friends.insert(1, "David")
print(f"David 삽입 후: {my_friends}") # 출력: ['Alice', 'David', 'Bob', 'Charlie']

# 맨 앞에 "Eve"를 삽입 (인덱스 0)
my_friends.insert(0, "Eve")
print(f"Eve 삽입 후: {my_friends}") # 출력: ['Eve', 'Alice', 'David', 'Bob', 'Charlie']

# 아주 큰 인덱스를 주면 맨 뒤에 추가됩니다 (append와 유사)
my_friends.insert(100, "Frank") # 현재 리스트 길이보다 큰 인덱스
print(f"Frank 삽입 후: {my_friends}") # 출력: ['Eve', 'Alice', 'David', 'Bob', 'Charlie', 'Frank']

# 삭제
numbers = [10, 20, 30, 40, 50]
print(f"삭제 전: {numbers}")

# 인덱스 2의 요소 (30) 삭제하고 반환받기
removed_item = numbers.pop(2)
print(f"pop(2) 후: {numbers}, 삭제된 항목: {removed_item}")
# 출력: pop(2) 후: [10, 20, 40, 50], 삭제된 항목: 30

# 맨 마지막 요소 삭제하고 반환받기
last_item = numbers.pop()
print(f"pop() 후: {numbers}, 삭제된 항목: {last_item}")
# 출력: pop() 후: [10, 20, 40], 삭제된 항목: 50

fruits = ["사과", "바나나", "딸기", "바나나", "포도"]
print(f"삭제 전: {fruits}")

# "바나나"를 삭제 (첫 번째로 발견되는 "바나나")
fruits.remove("바나나")
print(f"'바나나' 삭제 후: {fruits}")
# 출력: '바나나' 삭제 후: ['사과', '딸기', '바나나', '포도']

# "오렌지"를 삭제하려고 하면? (리스트에 없음)
# fruits.remove("오렌지") # 이 줄은 주석을 풀면 ValueError 발생!

# 한 번 더 "바나나" 삭제 (남아있는 "바나나")
fruits.remove("바나나")
print(f"두 번째 '바나나' 삭제 후: {fruits}")
# 출력: 두 번째 '바나나' 삭제 후: ['사과', '딸기', '포도']

letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"삭제 전: {letters}")

# 인덱스 0의 요소 ('a') 삭제
del letters[0]
print(f"del letters[0] 후: {letters}")
# 출력: del letters[0] 후: ['b', 'c', 'd', 'e', 'f']

# 인덱스 1부터 2까지 (즉, 'c'와 'd') 삭제
del letters[1:3] # 현재 letters는 ['b', 'c', 'd', 'e', 'f']
                # 여기서 인덱스 1은 'c', 인덱스 2는 'd'
print(f"del letters[1:3] 후: {letters}")
# 출력: del letters[1:3] 후: ['b', 'e', 'f']

# 리스트 전체를 삭제할 수도 있어요 (변수 자체가 사라짐)
# del letters
# print(letters) # 이 줄은 주석을 풀면 NameError 발생! (letters 변수가 삭제되었으므로)

numbers = [5, 2, 8, 1, 9, 3]
print(f"정렬 전: {numbers}")

numbers.sort() # 오름차순 정렬
print(f"오름차순 정렬 후: {numbers}") # 출력: [1, 2, 3, 5, 8, 9]

numbers.sort(reverse=True) # 내림차순 정렬
print(f"내림차순 정렬 후: {numbers}") # 출력: [9, 8, 5, 3, 2, 1]

names = ["Dave", "Alice", "Charlie", "Bob"]
names.sort()
print(f"이름 오름차순 정렬: {names}") # 출력: ['Alice', 'Bob', 'Charlie', 'Dave']

my_list = [3, 1, 2]
result = my_list.sort()
print(f"리스트: {my_list}") # 출력: [1, 2, 3]
print(f"결과: {result}")    # 출력: None

my_list = [1, 3, 2, 5, 4]
print(f"뒤집기 전: {my_list}")

my_list.reverse()
print(f"뒤집은 후: {my_list}") # 출력: [4, 5, 2, 3, 1]

original_numbers = [5, 2, 8, 1, 9, 3]
print(f"원본 리스트: {original_numbers}")

new_sorted_list = sorted(original_numbers) # 오름차순 정렬된 새 리스트
print(f"sorted() 후 원본: {original_numbers}") # 출력: [5, 2, 8, 1, 9, 3] (원본은 그대로!)
print(f"정렬된 새 리스트: {new_sorted_list}")    # 출력: [1, 2, 3, 5, 8, 9]

desc_sorted_list = sorted(original_numbers, reverse=True) # 내림차순
print(f"내림차순 정렬된 새 리스트: {desc_sorted_list}") # 출력: [9, 8, 5, 3, 2, 1]

letters = ['a', 'b', 'c', 'd', 'e', 'b', 'c']
print(f"리스트: {letters}")

index_of_c = letters.index('c')
print(f"'c'의 첫 번째 위치: {index_of_c}") # 출력: 2

index_of_b_after_3 = letters.index('b', 3) # 인덱스 3부터 'b'를 찾음
print(f"인덱스 3 이후 'b'의 첫 번째 위치: {index_of_b_after_3}") # 출력: 5

# 없는 값 찾기
# print(letters.index('z')) # 이 줄은 주석을 풀면 ValueError 발생!

numbers = [1, 2, 3, 2, 4, 2, 5, 2]
print(f"리스트: {numbers}")

count_of_2 = numbers.count(2)
print(f"숫자 2의 개수: {count_of_2}") # 출력: 4

count_of_7 = numbers.count(7)
print(f"숫자 7의 개수: {count_of_7}") # 출력: 0 (리스트에 없음)

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
combined_list = list1 + list2
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"결합된 리스트: {combined_list}") # 출력: [1, 2, 3, 'a', 'b', 'c']

my_list = [0, 1]
repeated_list = my_list * 3
print(f"원본 리스트: {my_list}")
print(f"반복된 리스트: {repeated_list}") # 출력: [0, 1, 0, 1, 0, 1]

separator_list = ["="] * 10
print(separator_list) # 출력: ['=', '=', '=', '=', '=', '=', '=', '=', '=', '=']

fruits = ["사과", "바나나", "딸기", "포도"]

# "딸기"가 fruits 리스트에 있는지 확인
is_strawberry_in = "딸기" in fruits
print(f"'딸기'가 리스트에 있나요? {is_strawberry_in}") # 출력: True

# "망고"가 fruits 리스트에 없는지 확인
is_mango_not_in = "망고" not in fruits
print(f"'망고'가 리스트에 없나요? {is_mango_not_in}") # 출력: True

if "바나나" in fruits:
    print("바나나를 찾았습니다!")
else:
    print("바나나를 찾을 수 없습니다.")


# 2x3 크기의 2차원 리스트 (행렬처럼 생각할 수 있어요)
matrix = [
    [1, 2, 3],  # 첫 번째 행 (인덱스 0)
    [4, 5, 6]   # 두 번째 행 (인덱스 1)
]
print(f"중첩 리스트: {matrix}")
# 출력: 중첩 리스트: [[1, 2, 3], [4, 5, 6]]

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# 첫 번째 행의 첫 번째 요소 (1)
element_0_0 = matrix[0][0]
print(f"matrix[0][0]: {element_0_0}") # 출력: matrix[0][0]: 1

# 두 번째 행의 세 번째 요소 (6)
element_1_2 = matrix[1][2]
print(f"matrix[1][2]: {element_1_2}") # 출력: matrix[1][2]: 6

# 첫 번째 행 전체 ([1, 2, 3])
first_row = matrix[0]
print(f"matrix[0]: {first_row}") # 출력: matrix[0]: [1, 2, 3]

fruits = ["사과", "바나나", "딸기", "포도"]

print("제가 가진 과일들:")
for fruit in fruits:
    print(f"- {fruit}")
# 출력:
# 제가 가진 과일들:
# - 사과
# - 바나나
# - 딸기
# - 포도

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num # 각 숫자를 더해나갑니다.
print(f"숫자들의 합: {sum_of_numbers}") # 출력: 숫자들의 합: 15
subjects = ["국어", "영어", "수학"]

print("과목 목록 (인덱스와 함께):")
for i in range(len(subjects)): # len(subjects)는 3이므로 range(3) -> i는 0, 1, 2
    subject = subjects[i]     # subjects[0], subjects[1], subjects[2] 순으로 접근
    print(f"인덱스 {i}: {subject}")
# 출력:
# 과목 목록 (인덱스와 함께):
# 인덱스 0: 국어
# 인덱스 1: 영어
# 인덱스 2: 수학

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("매트릭스 모든 요소 출력:")
for row in matrix:      # 바깥쪽 리스트(matrix)의 각 요소(행 리스트)를 row에 할당
    # row는 [1, 2, 3], 그 다음 [4, 5, 6], 그 다음 [7, 8, 9]가 됩니다.
    print(f"현재 행: {row}")
    for item in row:    # 안쪽 리스트(row)의 각 요소를 item에 할당
        print(f"  요소: {item}")
# 출력:
# 매트릭스 모든 요소 출력:
# 현재 행: [1, 2, 3]
#   요소: 1
#   요소: 2
#   요소: 3
# 현재 행: [4, 5, 6]
#   요소: 4
#   요소: 5
#   요소: 6
# 현재 행: [7, 8, 9]
#   요소: 7
#   요소: 8
#   요소: 9

students = [["Alice", 90], ["Bob", 85], ["Charlie", 95]]
# students.insert("David", 75)  
# 오답
# students.append(["David", 75]) or
students.insert(0, ["David", 75])
# students.remove("Bob")
# 오답
student_to_remove = None
for student_info in students:
    if student_info[0] == "Bob": # 각 학생 정보 리스트의 첫 번째 요소(이름)가 "Bob"인지 확인
        student_to_remove = student_info
        break # Bob을 찾았으니 더 이상 반복할 필요 없음

if student_to_remove: # student_to_remove가 None이 아니면 (즉, Bob을 찾았으면)
    students.remove(student_to_remove)
else:
    print("삭제하려는 Bob 학생이 명단에 없습니다.") # 예외 처리

students.sort(key=lambda x: x[1], reverse=True)
for student in students:
    print(f"학생: {student[0]}, 점수: {student[1]}점")
# if "Alice" in students:
#     print ("Alice 학생은 명단에 있습니다.")
# else:
#     print("명단에 없는 학생입니다.")
# 오답
alice_found = False
for student_info in students:
    if student_info[0] == "Alice": # 이름이 "Alice"인지 확인
        alice_found = True
        break

if alice_found:
    print("Alice 학생은 명단에 있습니다.")
else:
    print("Alice 학생이 명단에 없습니다.") # 요구사항은 있을 때만 출력하라고 했으니 이 else는 생략 가능

num_st = len(students)
print(num_st)

# 리스트 내용 정리
# 리스트 만들기
# 요소에 접근하기 (인덱싱, 슬라이싱)
# 요소 추가하기 (append, insert)
# 요소 삭제하기 (pop, remove, del)
# 정렬하고 순서 뒤집기 (sort, reverse, sorted)
# 요소 찾고 개수 세기 (index, count)
# 리스트 연산 (+, *, in, not in)
# 중첩 리스트와 반복문으로 리스트 다루기