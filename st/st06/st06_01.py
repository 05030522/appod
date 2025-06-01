# try:
#     # 예외 발생 가능성이 있는 코드
#     실행문1
# except 예외종류A:
#     # 예외종류A가 발생했을 때 실행될 코드
#     처리문A
# except 예외종류B:
#     # 예외종류B가 발생했을 때 실행될 코드
#     처리문B
# else:
#     # try 블록에서 예외가 발생하지 않았을 때만 실행될 코드
#     성공_시_실행문

try:
    num_str = input("숫자를 입력하세요: ")
    num = int(num_str)
except ValueError:
    print("잘못된 입력입니다. 숫자를 입력해야 합니다.")
else:
    # try 블록에서 ValueError가 발생하지 않았을 때만 실행
    print(f"입력하신 숫자는 {num}이고, 제곱은 {num**2}입니다.")

print("--- 다음 코드 ---")


# try:
#     # 예외 발생 가능성이 있는 코드
# except 예외종류:
#     # 예외 처리 코드
# else: # (선택 사항)
#     # 예외 미발생 시 코드
# finally:
#     # 예외 발생 여부와 관계없이 항상 실행될 코드
#     마무리_작업_코드

file = None # 파일 객체를 담을 변수 초기화
try:
    print("try 블록 시작")
    # file = open("없는파일.txt", "r") # 예외를 발생시키려면 이 줄의 주석을 푸세요
    num = int(input("숫자를 입력하세요 (오류 발생시키려면 문자 입력): "))
    print(f"입력한 숫자: {num}")
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except ValueError:
    print("숫자가 아닌 값을 입력했습니다.")
else:
    print("try 블록이 예외 없이 성공적으로 실행되었습니다.")
finally:
    print("finally 블록은 항상 실행됩니다! (리소스 정리 등)")
    if file: # 만약 파일이 열렸었다면
        # file.close() # 파일을 닫는 작업 등을 여기에!
        print("파일이 열렸었다면 여기서 닫습니다. (지금은 예시)")

print("--- try-except-finally 구문 끝 ---")



try:
    num_str = input("숫자를 입력하세요: ")
    num = int(num_str)
    result = 100 / num
    print(f"100을 {num}(으)로 나눈 결과: {result}")
except ValueError:
    print("잘못된 입력입니다! 반드시 숫자를 입력해주세요.")
except ZeroDivisionError:
    print("이런! 0으로는 나눌 수 없어요.")


try:
    data = {"key1": 10}
    value_str = input("값을 입력하세요 (숫자 또는 'key1' 중 하나): ")
    if value_str == "key1":
        result = data[value_str] # KeyError 가능성
    else:
        result = int(value_str)    # ValueError 가능성
    print(f"결과: {result}")
except (KeyError, ValueError): # KeyError 또는 ValueError가 발생하면 이 블록 실행
    print("키가 존재하지 않거나, 잘못된 숫자 형식입니다.")



try:
    x = int(input("숫자를 입력하세요: "))
    y = int(input("다른 숫자를 입력하세요: "))
    result = x / y
    print(f"나눗셈 결과: {result}")
except Exception as e: # 모든 종류의 예외(Exception 클래스의 자식들)를 잡고, 그 정보를 e에 저장
    print(f"오류가 발생했습니다! 오류 메시지: {e}")
    print(f"오류 타입: {type(e)}")



# 주의! except: 만 사용하는 것 vs except Exception as e:

# 그냥 except: 라고만 쓰면 정말 모든 예외를 다 잡아버립니다.
# 심지어 프로그램을 종료시키는 SystemExit나 사용자가 Ctrl+C를 눌러 발생하는 KeyboardInterrupt 같은 예외까지도요.
# 그래서 보통은 이렇게 너무 광범위하게 잡는 것은 피하는 것이 좋습니다.
# except Exception as e: 는 대부분의 프로그래밍 오류를 포함하면서도,
# SystemExit나 KeyboardInterrupt 같은 시스템 종료 관련 예외는 잡지 않아서 좀 더 안전하고 권장되는 방식입니다.



# 여러 개의 except 블록을 사용할 때는 위에서부터 순서대로 예외 타입을 확인합니다.
try:
    # ... 코드 ...
    num = int("abc") # ValueError 발생
except ValueError as ve:
    print(f"값 오류 발생: {ve}")
except Exception as e: # ValueError가 아닌 다른 모든 표준 오류
    print(f"일반 오류 발생: {e}")



# raise ValueError  # 이렇게 하면 ValueError가 발생합니다.



# try:
#     # ... 코드 ...
# except SomeError as e:
#     print("일단 여기서 로그를 남기고...")
#     raise  # 잡았던 SomeError를 그대로 다시 발생시킴



def set_age(age):
    if age < 0:
        raise ValueError("나이는 음수가 될 수 없습니다.") # 음수 나이는 잘못된 값이므로 ValueError 발생
    elif age > 150:
        raise ValueError("나이가 너무 많습니다. 현실적인 값을 입력해주세요.")
    print(f"나이가 {age}세로 설정되었습니다.")

try:
    set_age(25)
    set_age(-5) # 여기서 ValueError가 발생하고 아래 except 블록으로 이동
    set_age(200) # 이 코드는 실행되지 않음
except ValueError as e:
    print(f"입력 오류: {e}")

# 예상 출력:
# 나이가 25세로 설정되었습니다.
# 입력 오류: 나이는 음수가 될 수 없습니다.





def process_data(data):
    try:
        # 데이터를 처리하는 복잡한 로직이 있다고 가정
        if not data: # 데이터가 비어있으면 TypeError를 직접 발생
            raise TypeError("처리할 데이터가 없습니다.")
        result = 100 / len(data) # 만약 data가 숫자면 len()에서 TypeError, data가 비어있으면 ZeroDivisionError (위에서 잡히겠지만)
        return result
    except TypeError as te:
        print(f"[로그] 데이터 타입 관련 오류 발생: {te}")
        raise # 잡았던 TypeError를 다시 발생시켜서 이 함수를 호출한 곳에서 처리하도록 함
    except Exception as e:
        print(f"[로그] 기타 오류 발생: {e}")
        # 여기서는 다시 raise 하지 않았으므로, 이 함수 수준에서 오류 처리가 끝남
        return None # 또는 다른 적절한 값 반환

try:
    # 정상적인 경우
    # my_list = [1, 2]
    # print(f"처리 결과: {process_data(my_list)}")

    # TypeError를 발생시키는 경우 (None 전달)
    print(f"처리 결과: {process_data(None)}")

except TypeError as final_e: # process_data에서 다시 raise된 TypeError를 여기서 잡음
    print(f"최종 처리기에서 잡은 오류: {final_e}")
except Exception as general_e:
    print(f"최종 처리기에서 잡은 기타 오류: {general_e}")

# 예상 출력 (None을 전달했을 때):
# [로그] 데이터 타입 관련 오류 발생: 처리할 데이터가 없습니다.
# 최종 처리기에서 잡은 오류: 처리할 데이터가 없습니다.













# 파일 입출력(File I/O)
# 오늘은 딱 이 정도 개념만!

# 파일 입출력은 파일에서 데이터를 읽고 쓰는 것이다.
# 데이터를 오래 보관하거나 공유할 때 필요하다.
# 기본적으로 파일을 '열고', '작업하고', '닫는' 순서로 이루어진다.