class SimpleHashTable:
    def __init__(self, size=10):
        # 크기가 'size'인 리스트를 만들고, 각 요소를 빈 리스트(버킷)로 초기화
        self.size = size
        self.buckets = [[] for _ in range(size)]
        print(f"크기 {size}의 해시 테이블이 생성되었습니다. (빈 버킷들: {self.buckets})")

    def _hash_function(self, key):
        """키를 받아 해시 값(인덱스)을 반환하는 간단한 해시 함수"""
        # 파이썬 내장 hash()를 사용하고, 테이블 크기로 나눈 나머지를 인덱스로 사용
        return hash(key) % self.size

    def put(self, key, value):
        """키와 값을 해시 테이블에 추가하거나 수정합니다."""
        index = self._hash_function(key)
        bucket = self.buckets[index]
        
        # 이미 해당 키가 버킷에 있는지 확인 (수정의 경우)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) # 기존 값을 새로운 값으로 덮어쓰기
                print(f"키 '{key}'의 값을 '{value}'(으)로 수정했습니다. (인덱스: {index})")
                return
        
        # 새로운 키일 경우 버킷에 추가
        bucket.append((key, value))
        print(f"키 '{key}', 값 '{value}'을(를) 추가했습니다. (인덱스: {index})")

    def get(self, key):
        """키를 사용해 값을 찾아 반환합니다."""
        index = self._hash_function(key)
        bucket = self.buckets[index]
        
        # 버킷 안에서 키를 찾아 값을 반환
        for k, v in bucket:
            if k == key:
                print(f"키 '{key}'를 찾았습니다! (인덱스: {index})")
                return v
        
        # 버킷 안에 키가 없으면
        print(f"키 '{key}'를 찾을 수 없습니다.")
        return None

# 해시 테이블 사용해보기
ht = SimpleHashTable(size=5) # 5개의 방(버킷)을 가진 해시 테이블 생성

# 데이터 추가
ht.put("apple", "사과")
ht.put("banana", "바나나")
ht.put("grape", "포도")
ht.put("orange", "오렌지") # "apple"과 "orange"는 충돌이 일어날 수 있음 (해시 값에 따라)

print(f"\n현재 해시 테이블 상태: {ht.buckets}")

# 데이터 조회
print("\n--- 데이터 조회 ---")
print(f"apple의 값: {ht.get('apple')}")
print(f"grape의 값: {ht.get('grape')}")
print(f"kiwi의 값: {ht.get('kiwi')}") # 없는 키 조회

# 데이터 수정
print("\n--- 데이터 수정 ---")
ht.put("apple", "맛있는 사과")
print(f"수정된 apple의 값: {ht.get('apple')}")

print(f"\n최종 해시 테이블 상태: {ht.buckets}")