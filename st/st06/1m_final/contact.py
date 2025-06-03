class Contact:
    def __init__(self, name, number, email="", address=""):
        self.name = name
        self.number = number
        self.email = email
        self.address = address




    def display_contact_info(self):
        print(f"이름 : {self.name}")
        print(f"전화번호 : {self.number}")
        if self.email:
            print(f"이메일 : {self.email}")
        if self.address:
            print(f"주소 : {self.address}")
        print("-" * 20)




    def add_contact(contact_list):
        new_name = input("이름을 입력해주세요")
        new_number = input("전화번호를 입력해주세요")
        new_email = input("메일을 입력해주세요")
        new_address = input("주소를 입력해주세요")
        new_contact = Contact(new_name, new_number, new_email, new_address)
        contact_list.append(new_contact)
        print(f"{new_name}님의 연락처가 추가되었습니다.")




    def view_contacts(contact_list):
        # 1. 리스트가 비어있는지 먼저 확인
        if not contact_list: # contact_list가 비어있는지 확인하는 조건
            print("저장된 연락처가 없습니다.")
            return # 함수를 여기서 끝내버립니다.
    
        # 2. 리스트가 비어있지 않다면, 이제 모든 연락처를 출력
        print("\n--- 전체 연락처 목록 ---")
        for contact in contact_list: # 'contacts' 대신 'contact'로 변수명을 쓰는 게 더 명확해요 (각 연락처 하나를 의미하므로)
            contact.display_contact_info()
        print("--------------------")




    def search_contact(contact_list): # 함수 이름은 search_contact
        key = input("검색할 이름 또는 전화번호를 입력해주세요.").lower()
        found_contacts = False # 검색 결과를 찾았는지 여부를 나타내는 플래그

        print("\n--- 검색 결과 ---")
        for contact in contact_list: # 각 연락처 객체에 대해 반복
        # if 조건문을 사용하여 contact.name 또는 contact.phone_number에 key가 포함되는지 확인
        # (대소문자 구분을 없애기 위해 .lower() 사용)
            if key in contact.name.lower() or key in contact.number.lower():
                contact.display_contact_info()
                found_contacts = True # 연락처를 찾았으니 플래그를 True로 변경

    # 반복문이 모두 끝난 후, 플래그를 확인하여 검색 결과가 없었는지 판단
        if not found_contacts: 
            print("검색 결과가 없습니다.")
        print("----------------------")




    def edit_contact(contact_list):
        if not contact_list:
            print("수정할 연락처가 없습니다.")
            return

        search_keyword = input("수정할 연락처의 이름 또는 전화번호를 입력하세요: ").lower()
    
        found_contacts = [] # 검색된 Contact 객체들을 담을 리스트
        for contact in contact_list:
            if search_keyword in contact.name.lower() or search_keyword in contact.number.lower():
                found_contacts.append(contact) # <-- 여기에 contact 객체 자체를 추가!
    
        if not found_contacts:
            print("수정할 연락처를 찾을 수 없습니다.")
            return

        selected_contact = None # 사용자가 선택한 최종 연락처 객체를 저장할 변수

        if len(found_contacts) == 1:
            # 검색 결과가 하나뿐이면 바로 선택
            selected_contact = found_contacts[0]
            print(f"'{selected_contact.name}' 연락처를 수정합니다.")
        else:
            # 검색 결과가 여러 개일 때 사용자에게 선택 요청
            print("\n여러 개의 연락처가 검색되었습니다. 수정할 연락처의 번호를 입력하세요:")
            for i, contact_obj in enumerate(found_contacts): # 번호와 함께 리스트 출력
                print(f"{i+1}. 이름: {contact_obj.name}, 전화번호: {contact_obj.number}")
            
            while True: # 올바른 번호를 입력받을 때까지 반복
                try:
                    choice = int(input("번호 입력: "))
                    if 1 <= choice <= len(found_contacts):
                        selected_contact = found_contacts[choice - 1] # 리스트 인덱스는 0부터 시작
                        break # 유효한 선택이므로 반복 종료
                    else:
                        print("잘못된 번호입니다. 다시 입력해주세요.")
                except ValueError:
                    print("숫자를 입력해주세요.")

        print(f"\n--- '{selected_contact.name}' 연락처 수정 ---")
        print("수정할 정보만 입력하세요. (변경하지 않으려면 그냥 Enter)")

        # 1. 이름 수정
        new_name = input(f"새로운 이름 (현재: {selected_contact.name}): ").strip()
        if new_name: # 사용자가 뭔가 입력했다면 (빈 문자열이 아니라면)
            selected_contact.name = new_name # 이름 속성 업데이트
        
        # 2. 전화번호 수정
        new_number = input(f"새로운 전화번호 (현재: {selected_contact.number}): ").strip()
        if new_number:
            selected_contact.phone_number = new_number # 전화번호 속성 업데이트 (주의: Contact 클래스에서 self.number로 정의했다면 self.number로 변경)
            
        # 3. 이메일 수정
        new_email = input(f"새로운 이메일 (현재: {selected_contact.email}): ").strip()
        if new_email:
            selected_contact.email = new_email
            
        # 4. 주소 수정
        new_address = input(f"새로운 주소 (현재: {selected_contact.address}): ").strip()
        if new_address:
            selected_contact.address = new_address

        print(f"\n'{selected_contact.name}' 연락처가 성공적으로 수정되었습니다.")
        selected_contact.display_contact_info() # 수정된 정보를 바로 확인


    def delete_contact(contact_list):
        if not contact_list:
            print("삭제할 연락처가 없습니다.")
            return

        search_keyword = input("삭제제할 연락처의 이름 또는 전화번호를 입력하세요: ").lower()
    
        found_contacts = [] # 검색된 Contact 객체들을 담을 리스트

        for contact in contact_list:
            if search_keyword in contact.name.lower() or search_keyword in contact.number.lower():
                found_contacts.append(contact) # <-- 여기에 contact 객체 자체를 추가!
    
        if not found_contacts:
            print("삭제할 연락처를 찾을 수 없습니다.")
            return

        selected_contact = None # 사용자가 선택한 최종 연락처 객체를 저장할 변수

        if len(found_contacts) == 1:
            # 검색 결과가 하나뿐이면 바로 선택
            selected_contact = found_contacts[0]
            # a = input(f"'{selected_contact.name}'의의 연락처를 진짜 삭제하시겠습니까? (y/n)").lower()
            # if a == "y":
            #     contact_list.remove(selected_contact)
            #     print("연락처 삭제를 완료하였습니다.")
            # elif a == "n":
            #     print("연락처 삭제를 취소하였습니다.")
            #     return

        else:
            # 검색 결과가 여러 개일 때 사용자에게 선택 요청
            print("\n여러 개의 연락처가 검색되었습니다. 삭제할 연락처의 번호를 입력하세요:")
            for i, contact_obj in enumerate(found_contacts): # 번호와 함께 리스트 출력
                print(f"{i+1}. 이름: {contact_obj.name}, 전화번호: {contact_obj.number}")
            
            while True: # 올바른 번호를 입력받을 때까지 반복
                try:
                    choice = int(input("번호 입력: "))
                    if 1 <= choice <= len(found_contacts):
                        selected_contact = found_contacts[choice - 1] # 리스트 인덱스는 0부터 시작
                        break # 유효한 선택이므로 반복 종료
                    else:
                        print("잘못된 번호입니다. 다시 입력해주세요.")
                except ValueError:
                    print("숫자를 입력해주세요.")

        print(f"\n--- '{selected_contact.name}' 연락처를 삭제하시겠습니까? ---")
        b = input("y/n").lower()
        if b == "y":
            contact_list.remove(selected_contact)
            print("연락처 삭제를 완료하였습니다.")
        elif b == "n":
            print("연락처 삭제를 취소하였습니다.")
        return
    
    def save_contacts(contact_list, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for contact in contact_list:
                    line_to_write = f"{contact.name},{contact.number},{contact.email},{contact.address}\n"
                    f.write(line_to_write)
                print(f"총 {len(contact_list)}개의 연락처가 '{filename}'에 저장되었습니다.")
        except Exception as e:
            print(f"연락처 저장 중 오류가 발생했습니다 : {e}")
        # contact_list의 각 Contact 객체 정보를 파일에 저장합니다.
        # 각 속성(이름, 전화번호, 이메일, 주소)을 쉼표(,) 등으로 구분하여 한 줄에 저장하는 것이 좋습니다.
        # 파일 쓰기 모드는 w (덮어쓰기) 또는 a (이어쓰기) 중 선택할 수 있지만, 일반적으로는 w 모드를 사용하여 항상 최신 상태로 덮어쓰는 것이 안전합니다.
        # 힌트: 각 Contact 객체를 파일에 저장하기 전에, 객체에서 정보를 추출하여 하나의 문자열로 만드는 과정이 필요합니다.
        # (예: f"{contact.name},{contact.number},{contact.email},{contact.address}\n")
            

    def load_contacts(filename):
        # 파일에서 각 줄을 읽어와 Contact 객체로 다시 변환한 후 리스트에 담아 반환합니다.
        # 힌트: 각 줄을 쉼표(,)를 기준으로 split()하여 속성별로 나누고, 그 값들로 Contact 객체를 생성해야 합니다.
        # try-except FileNotFoundError를 사용하여 파일이 없을 경우 빈 리스트를 반환하거나 사용자에게 알리는 처리가 필수입니다.






def main():
    contact_list = []