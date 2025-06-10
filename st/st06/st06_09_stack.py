def merge_sort(data_list):
    # --- 1. 재귀의 탈출 조건 ---
    if len(data_list) <= 1:
        return data_list
    
    # --- 2. 분할 (Divide) 단계 ---
    mid = len(data_list) // 2
    left_half = merge_sort(data_list[:mid])
    right_half = merge_sort(data_list[mid:])
    
    # --- 3. 정복 및 병합 (Merge) 단계 ---
    merged_list = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left_half) and right_idx < len(right_half):
        if left_half[left_idx] < right_half[right_idx]:
            merged_list.append(left_half[left_idx])
            left_idx += 1
        else:
            merged_list.append(right_half[right_idx])
            right_idx += 1
    
    merged_list += left_half[left_idx:]
    merged_list += right_half[right_idx:]
    
    # --- 4. 최종 결과 반환 ---
    return merged_list







# 스택을 파이썬 리스트로 표현
my_stack = []
print(f"초기 스택: {my_stack}")

# PUSH 연산
print("\n--- Push ---")
my_stack.append('데이터 1')
print(f"Push '데이터 1': {my_stack}")
my_stack.append('데이터 2')
print(f"Push '데이터 2': {my_stack}")
my_stack.append('데이터 3')
print(f"Push '데이터 3': {my_stack}") # '데이터 3'이 맨 위에 있음

# TOP (PEEK) 연산
if my_stack: # 스택이 비어있지 않다면
    top_item = my_stack[-1]
    print(f"\n현재 맨 위 데이터 확인(top): {top_item}")
    print(f"스택 상태는 그대로: {my_stack}")
else:
    print("\n스택이 비어있습니다.")

# POP 연산
print("\n--- Pop ---")
popped_item_1 = my_stack.pop()
print(f"Pop 한 데이터: '{popped_item_1}', 남은 스택: {my_stack}")
popped_item_2 = my_stack.pop()
print(f"Pop 한 데이터: '{popped_item_2}', 남은 스택: {my_stack}")
popped_item_3 = my_stack.pop()
print(f"Pop 한 데이터: '{popped_item_3}', 남은 스택: {my_stack}")

# 빈 스택에서 pop을 시도하면? -> IndexError 발생
try:
    my_stack.pop()
except IndexError:
    print("\n오류: 비어있는 스택에서 데이터를 꺼낼 수 없습니다.")





def is_valid_parentheses(s):
    """주어진 문자열 s의 괄호들이 올바른지 확인합니다."""
    
    # 스택으로 사용할 리스트
    stack = []
    
    # 괄호 짝을 맞춰볼 딕셔너리
    # key: 닫는 괄호, value: 여는 괄호
    bracket_map = {")": "(", "}": "{", "]": "["}

    print(f"입력 문자열: '{s}'")
    
    # 문자열의 각 글자를 순서대로 확인
    for char in s:
        # 1. 만약 여는 괄호이면, 스택에 추가
        if char in "({[":
            stack.append(char)
            print(f"'{char}' (여는 괄호) -> 스택에 추가. 현재 스택: {stack}")
        # 2. 만약 닫는 괄호이면,
        elif char in ")}]":
            print(f"'{char}' (닫는 괄호) 만남. 스택 확인...")
            # 스택이 비어있거나, 스택에서 꺼낸 괄호가 짝이 맞지 않으면 실패
            # not stack: 스택이 비어있다는 뜻
            # stack.pop() != bracket_map[char]: 스택 맨 위 괄호와 현재 닫는 괄호의 짝이 맞지 않음
            if not stack or stack.pop() != bracket_map[char]:
                print(" -> 실패: 짝이 맞지 않거나, 닫을 괄호가 없습니다.")
                return False
            print(f" -> 성공: 짝이 맞음. 현재 스택: {stack}")

    # 3. 모든 문자열을 확인한 후, 스택이 비어있어야 성공
    if not stack:
        print("최종 결과: 성공! 스택이 비어있습니다.")
        return True
    else:
        print(f"최종 결과: 실패! 스택에 여는 괄호가 남아있습니다: {stack}")
        return False

# 테스트
print("--- 테스트 1 ---")
is_valid_parentheses("{[()]}") # True

print("\n--- 테스트 2 ---")
is_valid_parentheses("{[(])}") # False

print("\n--- 테스트 3 ---")
is_valid_parentheses("((") # False