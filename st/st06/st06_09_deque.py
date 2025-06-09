from collections import deque

# 큐를 deque로 생성
my_queue = deque()
print(f"초기 큐: {my_queue}")

# Enqueue 연산 (줄 서기)
print("\n--- Enqueue (데이터 추가) ---")
my_queue.append('손님 1')
print(f"Enqueue '손님 1': {my_queue}")
my_queue.append('손님 2')
print(f"Enqueue '손님 2': {my_queue}")
my_queue.append('손님 3')
print(f"Enqueue '손님 3': {my_queue}")

# Dequeue 연산 (업무 보기)
print("\n--- Dequeue (데이터 꺼내기) ---")
if my_queue: # 큐가 비어있지 않다면
    first_customer = my_queue.popleft() # 왼쪽(맨 앞)에서 꺼냅니다.
    print(f"Dequeue 한 손님: '{first_customer}', 남은 큐: {my_queue}")
    
    second_customer = my_queue.popleft()
    print(f"Dequeue 한 손님: '{second_customer}', 남은 큐: {my_queue}")
    
    third_customer = my_queue.popleft()
    print(f"Dequeue 한 손님: '{third_customer}', 남은 큐: {my_queue}")

# 빈 큐에서 dequeue를 시도하면? -> IndexError 발생
try:
    my_queue.popleft()
except IndexError:

    print("\n오류: 비어있는 큐에서 데이터를 꺼낼 수 없습니다.")