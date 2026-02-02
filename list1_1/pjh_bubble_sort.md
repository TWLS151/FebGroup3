# Bubble Sort 풀이

### 입력
```python
numbers = [64, 13, 9, 62, 3]
```
### 출력
```pyhton =
[3, 9, 13, 62, 64]
```

### 오늘 배운 것을 활용하려고 노력함
```python
def bubble_sort(arr):
    """
    arr 리스트를 정렬하는 함수
    """
    # i는 현재 확정할 위치
    for i in range(len(arr)):
        # j는 i보다 오른쪽 구간에서 비교 대상이 되는 인덱스
        # 즉, i보다 작은 값을 찾는 과정
        for j in range(i+1, len(arr)):
            # arr[i]이 arr[j] 보다 크다면
            # arr[i]와 arr[j]의 위치를 변경
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)
```