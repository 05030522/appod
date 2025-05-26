# 키-값 쌍 (Key-Value Pair): 딕셔너리의 핵심입니다. 각 키는 고유해야 하며, 이 키를 통해 연결된 값을 참조합니다.
# 순서 (Order): Mutable
# Python 3.7 이전 버전에서는 딕셔너리가 순서가 없는(unordered) 자료구조였습니다. 즉, 입력한 순서대로 저장되지 않을 수 있었어요.
# Python 3.7 이상 버전부터는 입력한 순서가 유지됩니다. 하지만 여전히 딕셔너리의 주된 접근 방식은 순서(인덱스)가 아닌 '키'를 통하는 것입니다. 리스트나 튜플처럼 숫자 인덱스로 값에 접근하지 않아요.
# 변경 가능 (Mutable): 딕셔너리는 생성 후에도 새로운 키-값 쌍을 추가하거나, 기존 쌍을 수정하거나 삭제할 수 있습니다.

# 키의 특징: Unique, Immutable
# 고유해야 합니다 (Unique): 딕셔너리 내에서 키는 중복될 수 없습니다. 만약 중복된 키를 사용하면 마지막에 할당된 값으로 덮어쓰입니다.

# 변경 불가능한(Immutable) 값이어야 합니다: 문자열, 숫자, 튜플 등은 키로 사용할 수 있지만, 리스트나 다른 딕셔너리처럼 변경 가능한 객체는 키로 사용할 수 없습니다.
# 값의 특징: 값은 어떤 데이터 타입이든 올 수 있고, 중복되어도 상관없습니다.

# 학생의 정보를 담는 딕셔너리
student = {
    "name": "Alice", # "name"이 키, "Alice"가 값
    "age": 20,       # "age"가 키, 20이 값
    "major": "Computer Science"
}
print(student)
# 출력: {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}
print(type(student)) # 출력: <class 'dict'>

empty_dict1 = {}
empty_dict2 = dict() # dict() 생성자 사용
print(empty_dict1) # 출력: {}
print(empty_dict2) # 출력: {}

person = dict(name="Bob", city="Seoul", job="Developer")
print(person) # 출력: {'name': 'Bob', 'city': 'Seoul', 'job': 'Developer'}

info_list = [("country", "Korea"), ("language", "Korean")]
country_info = dict(info_list)
print(country_info) # 출력: {'country': 'Korea', 'language': 'Korean'}student = {"name": "Alice", "age": 20}
print(student.get("name"))      # 출력: Alice
print(student.get("major"))     # 출력: None (오류 발생 안 함!)
print(student.get("major", "N/A")) # 출력: N/A ("major" 키가 없으므로 기본값 "N/A" 반환)

student = {"name": "Alice", "age": 20, "major": "CS"}
print(student["name"])  # 출력: Alice
print(student["age"])   # 출력: 20
# print(student["grade"]) # 이 줄은 주석을 풀면 KeyError 발생! ("grade" 키가 없음)

person = {"name": "Charlie"}
print(f"수정 전: {person}")

# 새로운 키-값 쌍 추가
person["age"] = 22
print(f"age 추가 후: {person}") # 출력: {'name': 'Charlie', 'age': 22}

person["city"] = "Busan"
print(f"city 추가 후: {person}") # 출력: {'name': 'Charlie', 'age': 22, 'city': 'Busan'}

# 기존 키의 값 수정
person["name"] = "Charles"
print(f"name 수정 후: {person}") # 출력: {'name': 'Charles', 'age': 22, 'city': 'Busan'}

student = {"name": "Alice", "age": 20, "major": "CS"}
print(f"삭제 전: {student}")

removed_age = student.pop("age")
print(f"age 삭제 후: {student}, 삭제된 값: {removed_age}")
# 출력: age 삭제 후: {'name': 'Alice', 'major': 'CS'}, 삭제된 값: 20

# 없는 키를 pop 하려고 할 때 기본값 사용
removed_grade = student.pop("grade", "N/A") # "grade" 키가 없으므로 "N/A" 반환
print(f"grade pop 시도 후: {student}, 반환된 값: {removed_grade}")
# 출력: grade pop 시도 후: {'name': 'Alice', 'major': 'CS'}, 반환된 값: N/A

# 없는 키를 pop 하려고 할 때 기본값 없이 시도 (오류 발생)
# removed_city = student.pop("city") # 이 줄은 KeyError 발생

person = {"name": "Bob", "city": "Seoul", "job": "Developer"}
print(f"삭제 전: {person}")

item_removed = person.popitem() # Python 3.7+ 에서는 ('job', 'Developer')가 삭제될 가능성이 높음
print(f"popitem 후: {person}, 삭제된 항목: {item_removed}")
# 예시 출력: popitem 후: {'name': 'Bob', 'city': 'Seoul'}, 삭제된 항목: ('job', 'Developer')

item_removed_again = person.popitem()
print(f"popitem 또 후: {person}, 삭제된 항목: {item_removed_again}")
# 예시 출력: popitem 또 후: {'name': 'Bob'}, 삭제된 항목: ('city', 'Seoul')

car = {"brand": "Hyundai", "model": "Sonata", "year": 2023}
print(f"삭제 전: {car}")

del car["year"]
print(f"year 삭제 후: {car}")
# 출력: year 삭제 후: {'brand': 'Hyundai', 'model': 'Sonata'}

# del car["color"] # 이 줄은 KeyError 발생 ("color" 키가 없음)

settings = {"volume": 80, "brightness": 50, "darkMode": True}
print(f"삭제 전: {settings}")

settings.clear()
print(f"clear 후: {settings}") # 출력: clear 후: {}

student = {"name": "Alice", "age": 20, "major": "CS"}
student_keys = student.keys()
print(f"키들: {student_keys}") # 출력: dict_keys(['name', 'age', 'major'])

# 리스트로 변환해서 사용 가능
key_list = list(student_keys)
print(f"키 리스트: {key_list}") # 출력: ['name', 'age', 'major']

student = {"name": "Alice", "age": 20, "major": "CS"}
student_values = student.values()
print(f"값들: {student_values}") # 출력: dict_values(['Alice', 20, 'CS'])

value_list = list(student_values)
print(f"값 리스트: {value_list}") # 출력: ['Alice', 20, 'CS']

student = {"name": "Alice", "age": 20, "major": "CS"}
student_items = student.items()
print(f"아이템들: {student_items}") # 출력: dict_items([('name', 'Alice'), ('age', 20), ('major', 'CS')])

item_list = list(student_items)
print(f"아이템 리스트: {item_list}") # 출력: [('name', 'Alice'), ('age', 20), ('major', 'CS')]

person1 = {"name": "Chris", "age": 25}
person2 = {"age": 26, "city": "New York", "job": "Engineer"}

# person1에 person2의 내용을 합치기
person1.update(person2)
print(f"업데이트 후 person1: {person1}")
# 출력: {'name': 'Chris', 'age': 26, 'city': 'New York', 'job': 'Engineer'}
# age는 26으로 업데이트 되었고, city와 job이 추가되었습니다.

# 키워드 인자로도 추가/수정 가능
person1.update(country="USA", age=27)
print(f"키워드 인자 업데이트 후 person1: {person1}")
# 출력: {'name': 'Chris', 'age': 27, 'city': 'New York', 'job': 'Engineer', 'country': 'USA'}

student = {"name": "Alice", "age": 20, "major": "CS"}
print("\n학생 정보 (키 기준):")
for key in student:
    print(f"{key}: {student[key]}") # 키를 이용해서 값을 가져옴
# 출력:
# name: Alice
# age: 20
# major: CS

student = {"name": "Alice", "age": 20, "major": "CS"}
print("\n학생 정보 (값 기준):")
for value in student.values():
    print(value)
# 출력:
# Alice
# 20
# CS

# 생성:
# 중괄호 {} 사용: my_dict = {"name": "Alice", "age": 30}
# dict() 생성자 사용: my_dict = dict(name="Alice", age=30) 또는 my_dict = dict([("name", "Alice"), ("age", 30)])
# 주요 연산 및 메소드:
# 값 접근:
# my_dict[key]: 키를 통해 값에 접근 (키가 없으면 KeyError).
# my_dict.get(key, default_value): 키를 통해 값에 접근 (키가 없으면 None 또는 default_value 반환).
# 추가 및 수정:
# my_dict[key] = value: 새 키-값 쌍을 추가하거나 기존 키의 값을 수정.
# my_dict.update(other_dict): 다른 딕셔너리의 내용으로 현재 딕셔너리를 업데이트.
# 삭제:
# del my_dict[key]: 특정 키-값 쌍 삭제.
# my_dict.pop(key, default_value): 키-값 쌍을 삭제하고 해당 값을 반환.
# my_dict.popitem(): 마지막으로 추가된 (또는 임의의) 키-값 쌍을 삭제하고 (키, 값) 튜플로 반환 (Python 3.7+ LIFO).
# my_dict.clear(): 모든 키-값 쌍 삭제.
# 정보 얻기/반복:
# my_dict.keys(): 모든 키들을 모은 객체 반환.
# my_dict.values(): 모든 값들을 모은 객체 반환.
# my_dict.items(): 모든 (키, 값) 튜플 쌍들을 모은 객체 반환 (주로 반복문에 사용).
# key in my_dict: 딕셔너리 안에 해당 키가 있는지 확인 (결과는 True 또는 False).
# len(my_dict): 딕셔너리의 키-값 쌍 개수 반환.
# 반복: for key in my_dict:, for value in my_dict.values():, for key, value in my_dict.items():

fruit_stock = {"apple": {"재고":10, "가격":1000}, "banana": {"재고":5, "가격":500}, "orange": {"재고":0, "가격":1500}}
fruit_stock["grape"] = {"재고":7, "가격":2000}
fruit_stock["banana"]["재고"] += 2
del fruit_stock["orange"]
for key in fruit_stock:
    print(f"{key}: {fruit_stock[key]["가격"]}원")
a = input("과일 이름을 입력해주세요")
if a in fruit_stock:
    print(fruit_stock[a]["재고"])
else:
    print("해당 과일은 없습니다.")
print(len(fruit_stock.keys()))