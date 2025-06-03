# 자주 사용되는 파일 열기 모드:

# 'r' (Read - 읽기):

# 파일을 읽기 위한 모드입니다. (기본값이라 생략하면 이 모드로 열립니다.)
# 파일이 존재하지 않으면 FileNotFoundError 오류가 발생합니다.
# 예: file = open("my_file.txt", "r", encoding="utf-8")
# 'w' (Write - 쓰기):

# 파일에 내용을 쓰기 위한 모드입니다.
# 파일이 존재하면 기존 내용은 모두 삭제되고 새로 작성됩니다 (덮어쓰기). 매우 주의해야 해요!
# 파일이 존재하지 않으면 새로운 파일을 생성합니다.
# 예: file = open("new_file.txt", "w", encoding="utf-8")
# 'a' (Append - 추가):

# 파일의 끝에 새로운 내용을 추가하기 위한 모드입니다.
# 파일이 존재하면 기존 내용 뒤에 이어서 씁니다.
# 파일이 존재하지 않으면 새로운 파일을 생성합니다.
# 예: file = open("log.txt", "a", encoding="utf-8")
# 'x' (Exclusive creation - 배타적 생성):

# 새로운 파일을 만들 때만 사용합니다.
# 파일이 이미 존재하면 FileExistsError 오류가 발생합니다.
# 실수로 기존 파일을 덮어쓰는 것을 방지하고 싶을 때 유용합니다.
# 예: file = open("unique_file.txt", "x", encoding="utf-8")
# 텍스트 모드와 바이너리 모드:

# 위의 모드들('r', 'w', 'a', 'x')은 기본적으로 텍스트 모드에서 동작합니다. 문자열 데이터를 다룰 때 사용해요.
# 이미지, 동영상, 실행 파일 등 텍스트가 아닌 바이너리(이진) 데이터를 다룰 때는 모드 뒤에 'b'를 붙여줍니다.
# 'rb': 바이너리 읽기 모드
# 'wb': 바이너리 쓰기 모드
# 'ab': 바이너리 추가 모드
# 예: image_file = open("photo.jpg", "rb")
# 읽고 쓰기 동시 모드 (+ 추가):

# 기존 모드에 '+'를 추가하면 읽기와 쓰기를 동시에 할 수 있는 모드가 됩니다.
# 'r+': 읽기 및 쓰기 모드. 파일이 없으면 오류. (기존 내용 위에 덮어쓸 수 있음)
# 'w+': 쓰기 및 읽기 모드. 파일이 없으면 새로 생성, 있으면 내용 다 지움.
# 'a+': 추가 및 읽기 모드. 파일이 없으면 새로 생성. (파일 포인터가 글쓰기를 위해 항상 파일 끝으로 이동)

# 이 모드들은 파일 포인터의 위치를 잘 이해하고 사용해야 해서 조금 더 복잡할 수 있습니다. 처음에는 'r', 'w', 'a'를 명확히 구분해서 사용하는 것이 좋습니다.




# try:
#     with open("exmaple1.txt", "r", encoding="utf-8") as f:
#         content = f.read()
#         print("--- read()로 읽은 전체 내용 ---")
#         print(content)
# except FileNotFoundError:
#     print("exmaple1.txt 파일을 찾을 수 없습니다.")

# import os
# print(f"현재 작업 디렉토리: {os.getcwd()}")

# # 여기에 원래 작성하셨던 try-except 코드가 이어집니다.
# try:
#     with open("example.txt", "r", encoding="utf-8") as f:
#         content = f.read()
#         print("--- read()로 읽은 전체 내용 ---")
#         print(content)
# except FileNotFoundError:
#     print("example.txt 파일을 찾을 수 없습니다.")



# try:
#     with open("example1.txt", "r", encoding="utf-8") as f:
#         print("\n--- readline()으로 한 줄씩 읽기 ---")

#         line1 = f.readline() # 첫 번째 줄 읽기
#         print(f"첫 번째 줄: [{line1.strip()}]") # .strip()으로 양쪽 공백 및 줄바꿈 문자 제거 후 출력

#         line2 = f.readline() # 두 번째 줄 읽기
#         print(f"두 번째 줄: [{line2.strip()}]")

#         line3 = f.readline() # 세 번째 줄 읽기
#         print(f"세 번째 줄: [{line3.strip()}]")

#         line4 = f.readline() # 네 번째 줄 시도 (더 이상 내용 없음)
#         if not line4: # line4가 빈 문자열이라면 (파일의 끝이라면)
#             print("더 이상 읽을 내용이 없습니다.")
#         else:
#             print(f"네 번째 줄: [{line4.strip()}]")

# except FileNotFoundError:
#     print("example1.txt 파일을 찾을 수 없습니다.")


try:
    with open("example1.txt", "r", encoding="utf-8") as f:
        lines_list = f.readlines() # 파일의 모든 줄을 리스트로 가져옴
        print("\n--- readlines()로 읽은 전체 리스트 ---")
        print(lines_list)
        # 예상 출력: ['안녕하세요.\n', '파이썬 파일 읽기 연습입니다.\n', '세 번째 줄입니다.\n']
        # (마지막 줄에 \n이 없을 수도 있습니다, 파일 저장 방식에 따라)

        print("\n--- 리스트의 각 줄을 반복문으로 출력 (strip() 사용) ---")
        for line in lines_list:
            print(f"내용: [{line.strip()}]") # .strip()으로 앞뒤 공백 및 줄바꿈 제거
except FileNotFoundError:
    print("example1.txt 파일을 찾을 수 없습니다.")

try:
    with open("example.txt", "r", encoding="utf-8") as file_object: # 파일 객체를 file_object 변수에 담음
        print("\n--- for 루프를 사용하여 파일 내용 한 줄씩 읽기 ---")
        for line_content in file_object: # 파일 객체(file_object)를 직접 for 루프에 사용
            # for 루프의 각 반복마다 line_content 변수에는 파일의 한 줄이 문자열로 담깁니다.
            # 이 문자열에는 줄 끝의 줄바꿈 문자(\n)도 포함될 수 있어요.
            print(f"읽은 내용: [{line_content.strip()}]") # .strip()으로 앞뒤 공백 및 줄바꿈 제거
except FileNotFoundError:
    print("example.txt 파일을 찾을 수 없습니다.")


    # "example.txt" 파일을 쓰기 모드로 열기 (기존 내용이 있다면 삭제됨)
try:
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("첫 번째 줄입니다.\n") # \n을 넣어서 줄바꿈
        f.write("파이썬으로 파일 쓰기 재미있네요!\n")
        num_written = f.write("마지막 줄입니다.") # \n 없음
        print(f"세 번째 write 호출 시 {num_written}개의 문자가 쓰여졌습니다.")
    print("example.txt 파일에 쓰기를 완료했습니다.")
except Exception as e:
    print(f"파일 쓰기 중 오류 발생: {e}")

# 이제 example.txt 파일을 열어보면 위 내용이 저장되어 있을 거예요.
# "마지막 줄입니다." 다음에는 줄바꿈이 없겠죠?



# example.txt 파일에 내용 추가하기
try:
    with open("example.txt", "a", encoding="utf-8") as f:
        f.write("\n이것은 추가된 내용입니다.\n") # \n을 먼저 써서 이전 내용과 줄을 띄움
        f.write("append 모드로 작성했어요.")
    print("example.txt 파일에 내용을 추가했습니다.")
except Exception as e:
    print(f"파일 추가 중 오류 발생: {e}")

# 다시 example.txt 파일을 열어보면 이전 내용 아래에 새로운 내용이 추가되어 있을 겁니다.


lines_to_write = [
    "보고서 제목: 2025년 상반기 실적\n", # 각 문자열 끝에 \n 포함
    "작성자: 파이썬\n",
    "날짜: 2025-06-03\n",
    "------------------------------------\n",
    "내용 요약...\n"
]

try:
    with open("example.txt", "w", encoding="utf-8") as f:
        f.writelines(lines_to_write)
    print("example.txt 파일에 여러 줄 쓰기를 완료했습니다.")
except Exception as e:
    print(f"파일 쓰기 중 오류 발생: {e}")

# example.txt 파일을 열어보면 lines_to_write 리스트의 내용이 그대로 들어가 있을 거예요. 기존 내용은 삭제