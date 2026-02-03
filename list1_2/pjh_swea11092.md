# SWEA 11092. 최대 최소의 간격

## 코드 방향성 / 구상한 내용
문제를 보고 방향성을 정한 게 아니라 코드를 작성하면서 마음가는대로 작성한 듯.
다음부턴 좀 생각하고 코드를 짜야겠다

## 어려웠던 점


```python
import sys

sys.stdin = open('11092.txt')

T = int(input())

for tc in range(1, T+1):

    # 양수의 개수
    N = int(int(input()))

    # 양수 ai 리스트
    ai = list(map(int, input().split()))

    # ai 리스트 중 최댓값과 최솟값을 0번째 인덱스로 지정
    max_val = ai[0]
    min_val = ai[0]

    # 반복문을 통해 ai 리스트의 최댓값과 최솟값을 할당
    for num in range(N):
        if ai[num] > max_val:
            max_val = ai[num]
        if ai[num] < min_val:
            min_val = ai[num]

    # ai 리스트에서 최솟값을 가지는 첫번째 인덱스
    min_position = ai.index(min_val)

    # ai 리스트에서 최댓값을 가지는 인덱스의 리스트 중 마지막 인덱스
    # 즉, ai 리스트의 최댓값 중 마지막 인덱스
    max_position = list(filter(lambda x: ai[x] == max_val, range(len(ai))))[-1]

    # 최댓값 인덱스 - 최솟값 인덱스의 절댓값
    result = abs(max_position - min_position)

    print(f"#{tc} {result}")
```