``` python

#4831.
# 테스트 케이스 입력
t = int(input())

for tc in range(1,t+1) :
    # k
    k,n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    # 종점부터 시작
    e = n
    # 충전 횟수 변수
    c = 0

    # 0번 도착까지 순환
    while e - k >0:
        result = False
        # 충전소 순환
        for i in range(m):
            if e-k <= nums[i] < e :
                c+=1
                e = nums[i]
                result = True
        # 충전소 없는 경우
        if not result:
            c = 0
            break

    # 출력
    print(f'#{tc} {c}')


```

``` python
# 4839

t = int(input())

def page(start, end, ta):
    if start > end:
        return 0

    c = (start + end) // 2

    if c == ta:
        return 1
    elif c < ta:
        return 1 + page(c, end, ta)
    else:
        return 1 + page(start, c, ta)

for tc in range(1, t + 1):
    book = list(map(int, input().split()))
    ac = page(1, book[0], book[1])
    bc = page(1, book[0], book[2])

    if ac > bc :
        print(f'#{tc} B')
    elif ac < bc :
        print(f'#{tc} A')
    else :
        print(f'#{tc} 0')

```   
``` python

# 5201
t = int(input())

for tc in range(1,t+1) :
    n, m = map(int,input().split())
    w_list = sorted(list(map(int, input().split())))
    t_list = sorted(list(map(int, input().split())))
    s = 0

    for i in range(m-1,-1,-1) :
        for j in range(len(w_list)-1,-1,-1) :
            if t_list[i] >= w_list[j] :
                s += w_list[j]
                w_list.pop(j)
                break
            else :
                continue
        else :
            break

    print(f'#{tc} {s}')
    
```

``` python

# 5204

t = int(input())  # 테스트 케이스 수

def merge(left_arr, right_arr):
    global cnt
    # 왼쪽 마지막 원소 > 오른쪽 마지막 원소인 경우
    if left_arr[-1] > right_arr[-1]:
        cnt += 1

    merged_arr = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1


    merged_arr.extend(left_arr[left_idx:])
    merged_arr.extend(right_arr[right_idx:])
    return merged_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])
    return merge(left_sorted, right_sorted)

for tc in range(1, t + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(nums)


    print(f'#{tc} {result[n//2]} {cnt}')
    
```