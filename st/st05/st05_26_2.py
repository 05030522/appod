my_tuple1 = (1, 2, 3, 4, 5)
my_tuple2 = ("apple", "banana", "cherry")
my_tuple3 = (1, "hello", 3.14, True)

print(my_tuple1)       # 출력: (1, 2, 3, 4, 5)
print(my_tuple2)       # 출력: ('apple', 'banana', 'cherry')
print(my_tuple3)       # 출력: (1, 'hello', 3.14, True)
print(type(my_tuple1)) # 출력: <class 'tuple'>

my_tuple4 = 10, 20, "world" # 소괄호 없이도 튜플 생성 가능
print(my_tuple4)       # 출력: (10, 20, 'world')
print(type(my_tuple4)) # 출력: <class 'tuple'>

single_element_tuple = (10,) # 쉼표가 있어서 튜플입니다!
not_a_tuple = (10)         # 이건 그냥 숫자 10을 괄호로 묶은 것 (int 타입)

print(single_element_tuple)       # 출력: (10,)
print(type(single_element_tuple)) # 출력: <class 'tuple'>

print(not_a_tuple)                # 출력: 10
print(type(not_a_tuple))          # 출력: <class 'int'>

my_list = [1, 2, 3]
tuple_from_list = tuple(my_list)
print(tuple_from_list) # 출력: (1, 2, 3)

string_val = "abc"
tuple_from_string = tuple(string_val)
print(tuple_from_string) # 출력: ('a', 'b', 'c')

# 비슷한점
my_tuple = ("월", "화", "수", "목", "금")
print(my_tuple[0])  # 출력: 월
print(my_tuple[-1]) # 출력: 금
my_tuple = (0, 1, 2, 3, 4, 5)
print(my_tuple[1:4]) # 출력: (1, 2, 3)
print(my_tuple[:3])  # 출력: (0, 1, 2)
print(my_tuple[3:])  # 출력: (3, 4, 5)
my_tuple = (10, 20, 30)
print(len(my_tuple)) # 출력: 3
tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1 + tuple2) # 출력: (1, 2, 3, 4)
print(tuple1 * 3)    # 출력: (1, 2, 1, 2, 1, 2)
my_tuple = ('a', 'b', 'c')
print('a' in my_tuple)    # 출력: True
print('d' not in my_tuple) # 출력: True

my_tuple = (10, 20, 30)

# 요소를 변경하려고 시도하면?
# my_tuple[0] = 100  # 이 줄은 주석을 풀면 TypeError 발생! ('tuple' object does not support item assignment)

# 요소를 추가하거나 삭제하는 메소드도 없습니다.
# my_tuple.append(40)  # AttributeError 발생! ('tuple' object has no attribute 'append')
# del my_tuple[0]      # TypeError 발생! ('tuple' object doesn't support item deletion)

my_tuple = (1, 2, 'a', 'b', 2, 'a', 2)
print(f"값 2의 개수: {my_tuple.count(2)}")    # 출력: 3
print(f"값 'a'의 위치: {my_tuple.index('a')}") # 출력: 2