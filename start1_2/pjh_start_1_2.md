### 260304 start1_1

## 이진수

# 코드 구현 방향
16진수를 2진수로 

# 어려웠던 점
없음

```python
def hex_to_dec(s):
    trans = {
        'F': '1111',
        'E': '1110',
        'D': '1101',
        'C': '1100',
        'B': '1011',
        'A': '1010',
        '9': '1001',
        '8': '1000',
        '7': '0111',
        '6': '0110',
        '5': '0101',
        '4': '0100',
        '3': '0011',
        '2': '0010',
        '1': '0001',
        '0': '0000'
    }
    result = ""
    for num in s:
        result += trans[num]

    return result



T = int(input())
for tc in range(1, T+1):
    N, s = input().split()

    ans = hex_to_dec(s)
    print(f'#{tc} {ans}')
```


## 벌꿀채취

# 코드 구현 방향
음...

# 어려웠던 점
일꾼 위치 고르는게 어려웠습니다.
코드 구현보다 훨씬 오래 걸린듯...

```python
from itertools import combinations as comb

def comb_honey(lst):
    max_honey = 0
    for i in range(1, M+1):
        for h in comb(lst, i):
            if sum(h) <= C:
                profit = 0
                for x in h:
                    profit += x**2
                if max_honey < profit:
                    max_honey = profit
    return max_honey

def honey(arr, n, m):
    profit_map = [[0] *N for _ in range(N)]
    total = 0
    for r in range(n):
        for c in range(n-m+1):
            n1 = arr[r][c:c+m]
            profit_map[r][c] = comb_honey(n1)

    for r1 in range(n):
        for c1 in range(n-m+1):
            profit1 = profit_map[r1][c1]
            for r2 in range(r1, n):
                if r1 == r2:
                    if_c2 = c1 + m
                else:
                    if_c2 = 0
                    for c2 in range(if_c2, n-m+1):
                        profit2 = profit_map[r2][c2]
                        if total < profit1 + profit2:
                            total = profit1 + profit2
    return total


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = honey(arr, N, M)
    print(f'#{tc} {ans}')
```