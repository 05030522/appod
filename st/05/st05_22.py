# for 변수 in 반복가능한객체:
    # 반복 실행될 코드 블록 (들여쓰기 필수!)
    # 실행문1
    # 실행문2
# for 문이 끝난 후 실행될 코드

# 0부터 4까지 (총 5번) 반복
# range(stop): 0부터 stop-1까지의 숫자를 만듭니다. stop 값 자체는 포함되지 않아요.
for i in range(5):  # i는 0, 1, 2, 3, 4 순서로 변합니다.
    print(f"현재 i 값: {i}")
# 출력:
# 현재 i 값: 0
# 현재 i 값: 1
# 현재 i 값: 2
# 현재 i 값: 3
# 현재 i 값: 4

# range(start, stop): start부터 stop-1까지의 숫자를 만듭니다.
# 1부터 5까지 (총 5번) 반복
for num in range(1, 6): # num은 1, 2, 3, 4, 5 순서로 변합니다.
    print(f"숫자: {num}")
# 출력:
# 숫자: 1
# 숫자: 2
# 숫자: 3
# 숫자: 4
# 숫자: 5

# 1부터 10까지 2씩 증가하며 반복 (1, 3, 5, 7, 9)
for even_num_plus_one in range(1, 11, 2):
    print(f"홀수?: {even_num_plus_one}")
# 출력:
# 홀수?: 1
# 홀수?: 3
# 홀수?: 5
# 홀수?: 7
# 홀수?: 9

# 10부터 1까지 1씩 감소하며 반복 (10, 9, ..., 2)
for countdown in range(10, 0, -1):
    print(f"카운트다운: {countdown}")
# 출력:
# 카운트다운: 10
# 카운트다운: 9
# ...
# 카운트다운: 1 (0은 포함 안됨)

my_string = "안녕하세요"
for char_item in my_string: # char_item 변수에 "안", "녕", "하", "세", "요"가 차례로 들어갑니다.
    print(char_item)
# 출력:
# 안
# 녕
# 하
# 세
# 요

fruits = ["사과", "바나나", "딸기", "포도"]
for fruit in fruits: # fruit 변수에 "사과", "바나나", "딸기", "포도"가 차례로 들어갑니다.
    print(f"내가 좋아하는 과일: {fruit}")
# 출력:
# 내가 좋아하는 과일: 사과
# 내가 좋아하는 과일: 바나나
# 내가 좋아하는 과일: 딸기
# 내가 좋아하는 과일: 포도

numbers_tuple = (10, 20, 30)
for n in numbers_tuple:
    print(f"숫자: {n}, 제곱: {n*n}")
# 출력:
# 숫자: 10, 제곱: 100
# 숫자: 20, 제곱: 400
# 숫자: 30, 제곱: 900


# 1부터 10까지의 숫자 중 짝수만 출력하기
for i in range(1, 11):
    if i % 2 == 0: # i를 2로 나눈 나머지가 0이면 (즉, 짝수이면)
        print(f"짝수 발견: {i}")

        # while 조건식:
    # 조건식이 True인 동안 반복 실행될 코드 블록 (들여쓰기 필수!)
    # 실행문1
    # 실행문2
    # (중요!) 루프 내에서 조건식의 결과를 바꿀 수 있는 코드가 보통 포함됩니다.
# while 문이 끝난 후 (조건식이 False가 되면) 실행될 코드

count = 1  # 1. 카운터 변수 초기화
while count <= 5:  # 2. 조건식: count가 5보다 작거나 같은 동안 반복
    print(f"현재 count: {count}")
    count += 1  # 3. (중요!) 카운터 변수 증가. 이 부분이 없으면 무한 루프!
print("while 루프 종료!")
# 출력:
# 현재 count: 1
# 현재 count: 2
# 현재 count: 3
# 현재 count: 4
# 현재 count: 5
# while 루프 종료!

command = "" # 명령어 저장 변수 초기화
while command.lower() != "exit": # 명령어가 "exit"(대소문자 무관)이 아닐 동안 반복
    command = input("명령을 입력하세요 ('exit' 입력 시 종료): ")
    if command.lower() != "exit":
        print(f"입력하신 명령: '{command}'을(를) 처리합니다.")
    # 여기서 command.lower()는 사용자가 EXIT, Exit, eXiT 등 어떻게 입력하든 소문자 'exit'로 바꿔서 비교하기 위함입니다.
print("프로그램을 종료합니다.")

is_running = True # 프로그램 실행 상태를 나타내는 플래그
attempts = 0

while is_running:
    print("메뉴: 1. 게임 시작 2. 점수 보기 3. 종료")
    choice = input("선택: ")
    attempts += 1

    if choice == "1":
        print("게임을 시작합니다!")
    elif choice == "2":
        print("점수: 100점")
    elif choice == "3":
        print("게임을 종료합니다.")
        is_running = False # 플래그를 False로 변경하여 루프 종료 조건 만듦
    else:
        print("잘못된 선택입니다.")

    if attempts >= 5 and is_running: # 너무 많은 시도를 하면 강제 종료 (안전장치)
        print("너무 많은 잘못된 시도. 강제 종료합니다.")
        is_running = False

print("플래그를 이용한 while 루프 종료!")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 리스트에서 숫자 5를 찾으면 반복을 멈추고 싶을 때
for num in numbers:
    if num == 5:
        print(f"숫자 {num}을(를) 찾았습니다! 반복을 중단합니다.")
        break  # 여기서 for 루프를 완전히 빠져나옴
    print(f"현재 숫자: {num}")
print("for 루프 바깥입니다.")
# 출력:
# 현재 숫자: 1
# 현재 숫자: 2
# 현재 숫자: 3
# 현재 숫자: 4
# 숫자 5을(를) 찾았습니다! 반복을 중단합니다.
# for 루프 바깥입니다. (5 이후의 숫자들은 출력되지 않음)

count = 0
while True: # 일단 무한 루프 시작
    print(f"현재 count: {count}")
    count += 1
    if count >= 3: # count가 3 이상이 되면
        print("count가 3 이상이므로 break 실행!")
        break # while 루프를 빠져나옴
print("while 루프 바깥입니다.")
# 출력:
# 현재 count: 0
# 현재 count: 1
# 현재 count: 2
# count가 3 이상이므로 break 실행!
# while 루프 바깥입니다.

# 1부터 10까지의 숫자 중 홀수만 출력하기 (짝수는 건너뛰기)
for i in range(1, 11):
    if i % 2 == 0: # i가 짝수이면
        continue   # 현재 반복의 나머지 부분을 건너뛰고 다음 i로 넘어감
    print(f"홀수: {i}")
print("for 루프 바깥입니다.")
# 출력:
# 홀수: 1
# 홀수: 3
# 홀수: 5
# 홀수: 7
# 홀수: 9
# for 루프 바깥입니다. (짝수일 때는 print문이 실행되지 않음)

num = 0
while num < 5:
    num += 1
    if num == 3: # num이 3일 때는
        print("num이 3일 때는 출력을 건너뜁니다.")
        continue # 아래 print문을 실행하지 않고 바로 다음 while 조건 검사로 감
    print(f"현재 num: {num}")
print("while 루프 바깥입니다.")
# 출력:
# 현재 num: 1
# 현재 num: 2
# num이 3일 때는 출력을 건너뜁니다.
# 현재 num: 4
# 현재 num: 5
# while 루프 바깥입니다.

# 문제: 1부터 20까지의 숫자 중에서 다음 규칙에 따라 숫자를 출력하는 프로그램을 작성하세요.

# 숫자가 3의 배수이면서 5의 배수인 경우 (즉, 15의 배수) "FizzBuzz"를 출력하고, 그 이후의 반복은 즉시 종료합니다 (break 사용).
# 위 조건에 해당하지 않으면서, 숫자가 3의 배수인 경우 "Fizz"를 출력합니다.
# 위 조건들에 해당하지 않으면서, 숫자가 5의 배수인 경우 "Buzz"를 출력합니다.
# 위 모든 조건에 해당하지 않으면 그냥 숫자를 출력합니다.
# 단, 숫자가 10인 경우는 아무것도 출력하지 않고 건너뜁니다 (continue 사용).

num=0
while num<20:
    num+=1
    if num%3==0 and num%5==0:
        print("FizzBuzz")
        break
    elif num%3==0 and num%5!=0:
        print("Fizz")
    elif num%3!=0 and num%5==0 and num!=10:
        print("Buzz")
    elif num%3!=0 and num%5!=0:
        print(num)
    elif num==10:
        continue

# 리펙토링링
#     num = 0
# while num < 20:
#     num += 1

#     if num == 10:  # 10인 경우는 가장 먼저 확인해서 건너뛰기
#         continue

#     # 그 외의 경우에 대한 FizzBuzz 로직
#     if num % 3 == 0 and num % 5 == 0: # (또는 num % 15 == 0)
#         print("FizzBuzz")
#         break
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)