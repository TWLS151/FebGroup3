# SWEA 4835. [파이썬 S/W 문제해결 기본] 1일차 - 구간합


## 코드 방향성 / 구상한 내용
없음

## 어려웠던 점
1. 처음에 문제를 똑바로 안보고 풀어서 sort로 풀었는데 답이 안나와서 문제를 똑바로 보니까 그게 아닌 문제였음

2. 슬라이싱을 하는 구간을 생각하는 것이 어려웠음.

3. 머리가 굳었는 지, 단순한 사칙연산 식 2~3개가 머리에 유지가 안 되는 느낌

4. 종이에 필기하면서 했으면 훨씬 빨리 했을 듯

5. max_sum 이랑 min_sum 값을 아무 생각 없이 0으로 뒀다가 min 값이 갱신 안되는 문제가 발생했음 → sum의 첫 구간으로 설정해서 해결함

```python
import sys

sys.stdin = open('4835.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    # ai 리스트의 합, 일단 0으로 둠
    ai_sum = 0

    # N개의 숫자 중 이웃한 M개의 숫자 합의 max값과 min 값.
    # max와 min은 첫 구간 합으로 설정
    max_sum = sum(ai[0:M])
    min_sum = sum(ai[0:M])


    # 연속 M개 구간합을 구하려면, 구간의 "끝 인덱스" i를 기준으로 잡는다.
    # max와 min 값을 첫 구간으로 설정했으므로
    # i가 N까지 가면 마지막 구간 ai[M : N] 까지 모두 커버된다.
    for i in range(M, N):
        # 슬라이싱으로 "연속 M개"를 잘라서 합을 구한다.
        # ai[i-(M-1) : i+1]  -> 길이가 M인 구간
        #
        # 예시) M=4, i=5이면:
        # ai[5-3 : 6] = ai[2 : 6] = (2,3,4,5번째 원소) 총 4개
        ai_sum = sum(ai[i-(M-1):i+1])

        if ai_sum > max_sum:
            max_sum = ai_sum
        if ai_sum < min_sum:
            min_sum = ai_sum

    print(f'#{tc} {max_sum - min_sum}')
```