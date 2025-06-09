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