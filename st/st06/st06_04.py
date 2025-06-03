# with open("example.txt", "r", encoding="utf-8") as f:
#     content_part1 = f.read(5)  # 앞에서 5글자만 읽기
#     print(f"첫 5글자: '{content_part1}'")
#     current_position = f.tell() # 현재 파일 포인터 위치 확인
#     print(f"현재 파일 포인터 위치: {current_position} 바이트")
#     content_part2 = f.read()   # 나머지 내용 읽기
#     print(f"나머지 내용: '{content_part2.strip()}'")

# with open("example.txt", "r", encoding="utf-8") as f:
#     f.seek(6) # 파일 시작점에서 7바이트 위치로 이동 (한글은 1글자가 보통 2~3바이트)
#                 # 정확한 위치는 인코딩과 내용에 따라 달라질 수 있어 텍스트 파일에선 주의 필요
#                 # 보가 3바이트 보고가 6바이트이므로 중간값인 4,5 바이트로 자르려고 하면 오류가 생긴다. 유레카!!!!!!
#     content_from_seek = f.readline().strip()
#     print(f"seek(3) 이후 첫 줄: '{content_from_seek}'")

#     f.seek(0) # 다시 파일의 맨 처음으로 포인터 이동
#     first_line_again = f.readline().strip()
#     print(f"seek(0) 이후 첫 줄: '{first_line_again}'")



# # 문제 풀기
# error_log_num = 0
# log_num = 0
# error_lines_buffer = [] #여러번 오픈하는걸 방지하기 위해서
# try:
#     with open("server_log.txt", "r", encoding="utf-8") as s:
#         for line in s:
#             log_num += 1
#             if line.startswith("[ERROR]"):
#                 error_log_num += 1
#                 error_lines_buffer.append(line)
        
#     with open("error_log.txt", "w", encoding="utf-8") as f:  # 새로 파일 하는거라 w해도 됨됨
#         for error_line in error_lines_buffer:
#             f.write(error_line)

#     print(f"전체 로그 라인 수:[{log_num}]")
#     print(f"기록된 에러 로그 라인 수:[{error_log_num}]")

# except FileNotFoundError:
#     print("server_log.txt 파일을 찾을 수 없습니다.")

# except Exception as e:
#     print(f"log 작업 중 오류 발생 : {e}")




# class Human:
#     # __init__ 메서드: 객체가 생성될 때 자동으로 호출됩니다.
#     # self는 생성되는 객체 자기 자신을 가리킵니다.
#     # name, age, gender는 객체를 만들 때 외부에서 전달받을 값입니다.
#     def __init__(self, name_param, age_param, gender_param):
#         print(f"Human 객체 '{name_param}' 생성 시작...")
        
#         # self.속성이름 = 값 형태로 객체의 속성을 만듭니다.
#         # 이제 이 객체는 name, age, gender라는 자신만의 데이터를 갖게 됩니다.
#         self.name = name_param      # 'name'이라는 인스턴스 속성에 전달받은 name_param 값을 저장
#         self.age = age_param        # 'age'라는 인스턴스 속성에 전달받은 age_param 값을 저장
#         self.gender = gender_param  # 'gender'라는 인스턴스 속성에 전달받은 gender_param 값을 저장
        
#         print(f"'{self.name}' 객체 생성 완료! (나이: {self.age}세, 성별: {self.gender})")

# # Human 클래스(설계도)를 사용해서 실제 Human 객체(인스턴스)를 만들어봅시다!
# # 클래스 이름 뒤 괄호 안에 __init__ 메서드의 매개변수(self 제외)에 전달할 값들을 순서대로 넣어줍니다.
# person_hajw = Human("하지원", 28, "여성") 
# # ↑ 이 코드가 실행되는 순간, Human 클래스의 __init__ 메서드가 다음과 같이 호출되는 것과 비슷합니다:
# # Human.__init__(person_hajw, "하지원", 28, "여성") 
# # (person_hajw 객체가 self로 전달됨)

# person_cew = Human("차은우", 27, "남성")

# print("\n--- 각 객체의 속성 확인 ---")
# # 객체의 속성에 접근할 때는 '객체이름.속성이름' 형태로 사용합니다.
# print(f"{person_hajw.name}님의 나이는 {person_hajw.age}세, 성별은 {person_hajw.gender}입니다.")
# print(f"{person_cew.name}님의 나이는 {person_cew.age}세, 성별은 {person_cew.gender}입니다.")

# # 각 객체는 자신만의 속성 값을 가집니다.
# # 예를 들어 person_hajw의 나이를 바꿔도 person_cew의 나이는 그대로입니다.
# person_hajw.age = 29 
# print(f"\n{person_hajw.name}님의 변경된 나이: {person_hajw.age}세")
# print(f"{person_cew.name}님의 나이는 여전히 {person_cew.age}세 입니다.")







# class Human:
#     def __init__(self, name, age, height, weight, gender):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#         self.gender = gender
#         print(f"{self.name} (이/가) 태어났습니다!")

#     # 인스턴스 메서드 1: 말하기 (speak)
#     def speak(self, words): # self는 필수, words는 외부에서 받을 말입니다.
#         print(f"{self.name} (이/가) '{words}' 라고 말합니다.")

#     # 인스턴스 메서드 2: 걷기 (walk)
#     def walk(self, distance): # self는 필수, distance는 걸을 거리입니다.
#         print(f"{self.name} (이/가) {distance}km를 걷습니다.")
#         # 걷는 행동이 객체의 상태에 영향을 줄 수도 있습니다 (예: 체중 감소 등)
#         # self.weight -= distance * 0.1 # 예시: 걷는 거리에 따라 체중이 줄어든다고 가정

#     # 인스턴스 메서드 3: 정보 보여주기 (show_info)
#     def show_info(self):
#         print(f"\n--- {self.name}의 정보 ---")
#         print(f"이름: {self.name}")
#         print(f"나이: {self.age}세")
#         print(f"키: {self.height}cm")
#         print(f"몸무게: {self.weight}kg")
#         print(f"성별: {self.gender}")
#         print("--------------------")

# # 객체 생성
# print("여기가 시작")
# hajiwon = Human("하지원", 46, 168, 48, "여성")
# chaeunwoo = Human("차은우", 27, 183, 64, "남성")

# # 이제 객체의 메서드를 호출해 봅시다!
# # 객체이름.메서드이름(매개변수) 형식으로 호출합니다.
# print("\n--- 하지원 객체의 행동 ---")
# hajiwon.speak("안녕하세요!")
# hajiwon.walk(5)
# hajiwon.show_info() # 걷기 후 체중 변화를 확인해볼 수 있습니다.

# print("\n--- 차은우 객체의 행동 ---")
# chaeunwoo.speak("반갑습니다.")
# chaeunwoo.walk(2)
# chaeunwoo.show_info()










# 부모 클래스: 모든 사람이 공통적으로 가질 특성을 정의
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(f"Human {self.name} (이/가) 태어났습니다!")

    def speak(self, words):
        print(f"{self.name} (이/가) '{words}' 라고 말합니다.")

    def walk(self, distance):
        print(f"{self.name} (이/가) {distance}km를 걷습니다.")

    def show_info(self):
        print(f"\n--- {self.name}의 기본 정보 ---")
        print(f"이름: {self.name}")
        print(f"나이: {self.age}세")
        print(f"성별: {self.gender}")
        print("--------------------")

# --- 이제 Human 클래스를 상속받는 자식 클래스를 만들어봅시다 ---

# 자식 클래스 1: Student (학생)
# Human 클래스를 상속받습니다.
class Student(Human): # 괄호 안에 부모 클래스 'Human'을 넣어줍니다.
    def __init__(self, name, age, gender, student_id, major):
        # super()는 부모 클래스의 __init__ 메서드를 호출하여 부모의 속성을 초기화합니다.
        # 이렇게 하면 name, age, gender는 Human 클래스에서 초기화됩니다.
        super().__init__(name, age, gender)
        self.student_id = student_id # 학생만의 고유한 속성 추가
        self.major = major           # 학생만의 고유한 속성 추가
        print(f"Student {self.name} (학번: {self.student_id}) (이/가) 생성되었습니다.")

    # 학생만의 새로운 행동(메서드) 추가
    def study(self, subject):
        print(f"{self.name} (이/가) {subject}를 공부합니다.")

    # 부모의 show_info 메서드를 오버라이딩(덮어쓰기)하지 않고, 학생 정보를 추가해서 보여주기
    def show_student_info(self): # 새로운 메서드를 정의합니다.
        super().show_info() # 부모의 show_info를 호출해서 기본 정보를 먼저 출력
        print(f"학번: {self.student_id}")
        print(f"전공: {self.major}")
        print("--------------------")

# 자식 클래스 2: Employee (직원)
# Human 클래스를 상속받습니다.
class Employee(Human):
    def __init__(self, name, age, gender, employee_id, department):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.department = department
        print(f"Employee {self.name} (사번: {self.employee_id}) (이/가) 생성되었습니다.")

    def work(self):
        print(f"{self.name} (이/가) {self.department} 부서에서 일합니다.")

# --- 객체 생성 및 상속 확인 ---

# Human 객체
person1 = Human("김철수", 35, "남성")
person1.speak("안녕하세요, 저는 김철수입니다.")
person1.show_info()

print("\n" + "-"*30 + "\n")

# Student 객체
student1 = Student("박영희", 20, "여성", "20231234", "컴퓨터공학")
student1.speak("교수님, 질문이 있습니다!") # Human으로부터 speak 메서드 상속
student1.walk(1) # Human으로부터 walk 메서드 상속
student1.study("Python") # Student 자신만의 메서드
student1.show_student_info() # Student 자신만의 정보 출력 메서드 (부모 메서드 활용)

print("\n" + "-"*30 + "\n")

# Employee 객체
employee1 = Employee("이민정", 40, "여성", "EMP007", "인사부")
employee1.speak("업무 관련해서 말씀드릴 게 있습니다.") # Human으로부터 speak 메서드 상속
employee1.work() # Employee 자신만의 메서드
employee1.show_info() # Human으로부터 show_info 메서드 상속 (오버라이딩 안 했으니 부모 것 그대로 사용)