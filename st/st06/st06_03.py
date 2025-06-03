# 기본 사용법:
# 파일객체 = open("파일이름_또는_경로", "열기모드", encoding="인코딩방식")

# "파일이름_또는_경로": 작업하려는 파일의 이름이나 전체 경로를 문자열로 전달합니다.
# 예: "my_data.txt", "C:/Users/Me/Documents/report.docx"
# 파일 이름만 적으면, 현재 파이썬 스크립트가 실행되는 같은 폴더에서 파일을 찾거나 생성합니다.
# "열기모드": 파일을 어떤 목적으로 열 것인지를 지정하는 문자열입니다. 자주 사용되는 모드는 다음과 같아요.
# 'r' (Read): 읽기 모드. 파일의 내용을 읽기 위해 엽니다. 파일이 존재하지 않으면 오류(FileNotFoundError)가 발생합니다. (기본값이라 생략 가능)
# 'w' (Write): 쓰기 모드. 파일에 내용을 쓰기 위해 엽니다.
# 파일이 존재하면 기존 내용은 모두 지워지고 새로운 내용으로 덮어쓰입니다. (주의!)
# 파일이 존재하지 않으면 새로운 파일을 생성합니다.
# 'a' (Append): 추가 모드. 파일의 기존 내용 끝에 새로운 내용을 추가하기 위해 엽니다.
# 파일이 존재하지 않으면 새로운 파일을 생성합니다.
# 'x' (Exclusive creation): 배타적 생성 모드. 새 파일을 만들 때만 사용합니다. 파일이 이미 존재하면 오류(FileExistsError)가 발생합니다.
# 여기에 '+'를 붙여서 읽고 쓰기 모두 가능한 모드(예: 'r+', 'w+')로 열 수도 있고, 텍스트 파일이 아닌 이미지나 동영상 같은 이진(binary) 파일을 다룰 때는 모드 뒤에 'b'를 붙입니다(예: 'rb', 'wb').
# 지금은 주로 텍스트 파일을 다룰 거예요.
# encoding="인코딩방식": 텍스트 파일을 다룰 때 매우 중요한 설정입니다. 파일에 있는 글자들이 어떤 방식으로 저장되어 있는지(또는 저장할지) 알려주는 거예요.
# 한글을 다룰 때는 거의 항상 encoding="utf-8" 을 사용한다고 생각하시면 됩니다. 이걸 지정하지 않으면 한글이 깨져 보이거나 저장될 수 있어요.




# "my_notes.txt" 파일을 쓰기 모드('w')로 열기 (UTF-8 인코딩 사용)
# 만약 my_notes.txt 파일이 없으면 새로 만들어지고, 있으면 내용이 지워짐!
try:
    file = open("my_notes.txt", "w", encoding="utf-8")
    print("my_notes.txt 파일을 쓰기 모드로 열었습니다.")
    # ... (여기에 파일에 쓰는 작업을 하겠죠?) ...
except Exception as e:
    print(f"파일 열기 실패: {e}")
finally:
    if 'file' in locals() and file: # 파일 객체가 실제로 만들어졌고, 열려있다면
        print("파일을 닫습니다.")
        file.close() # 매우 중요! 파일 작업이 끝나면 반드시 닫아야 합니다.



with open("파일이름", "모드", encoding="utf-8") as 파일객체변수:
    # 이 블록 안에서 파일객체변수를 사용하여 파일 작업을 합니다.
    # 예를 들어, 파일객체변수.write("내용 쓰기")
    # 또는 내용 = 파일객체변수.read()
    # ...

# with 블록을 벗어나면 (들여쓰기가 끝나면)
# 파일객체는 자동으로 닫힙니다 (file.close()가 자동으로 호출됨).
# 심지어 try 블록 안에서 오류가 발생해도 자동으로 닫아줘요!




# "greeting.txt" 파일에 내용 쓰기
with open("greeting.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요!\n")
    f.write("파이썬 파일 쓰기 연습입니다.\n")
    print("greeting.txt 파일에 내용을 다 썼습니다. (with 블록 안)")

print("with 블록 바깥: 파일은 자동으로 닫혔습니다.")
# 이제 greeting.txt 파일을 열어보면 내용이 잘 저장되어 있을 거예요.





# greeting.txt 파일 내용 읽기
try:
    with open("greeting.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print("\n--- greeting.txt 파일 내용 ---")
        print(content)
        print("--- 파일 내용 끝 --- (with 블록 안)")
except FileNotFoundError:
    print("greeting.txt 파일을 찾을 수 없습니다.")

print("with 블록 바깥: 파일은 자동으로 닫혔습니다.")