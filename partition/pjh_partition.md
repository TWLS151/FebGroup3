``` python

#4839.
# 문제를 잘 읽읍시다.
import sys
sys.stdin = open('4839.txt')

def binary_search(left, right, target, cnt):

    mid = int((left + right) / 2)
    if mid == target:
        return cnt

    elif mid > target:
        return binary_search(left, mid, target, cnt + 1)
    else:
        return binary_search(mid, right, target, cnt + 1)


T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    A_cnt = binary_search(1, P, A, 1)
    B_cnt = binary_search(1, P, B, 1)

    if A_cnt > B_cnt:
        print(f"#{tc} B")
    elif A_cnt < B_cnt:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')
```

``` python
# 5204
# cnt만 추가
# 근데 오늘 배운 정렬들이 조금 어려운듯...
# 따로 더 공부가 필요함을 느낌

import sys
sys.stdin = open('5204.txt')

def merge(left_arr, right_arr):
    global cnt
    merge_arr = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            merge_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merge_arr.append(right_arr[right_idx])
            right_idx += 1

    if left_arr[-1] > right_arr[-1]:
        cnt += 1
    merge_arr.extend(left_arr[left_idx:])
    merge_arr.extend(right_arr[right_idx:])

    return merge_arr

def merge_sort(arr):
    global cnt
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    ans = merge_sort(arr)
    print(f'#{tc} {ans[N//2]} {cnt}')

```   
``` python

# 5205
# 퀵정렬 연습
def partition(arr, start, end):
    pivot = arr[end]

    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[end] = arr[end], arr[i+1]

    return i+1

def quick_sort(arr, start, end):

    if start < end:
        pivot_idx = partition(arr, start, end)

        quick_sort(arr, start, pivot_idx-1)
        quick_sort(arr, pivot_idx+1, end)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, N-1)
    print(f'#{tc} {arr[N//2]}')
```