### 260204 List2_1

## 1.1(기본) / 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기

## 코드 방향성 / 구상한 내용

고민 좀 하다가 결국 아이디어 방향은 빈 행렬을 만들고
빨간색 영역은 1 더하기, 파란색 영역은 2 더하기
그러면 겹쳐진 부분(보라색)은 3이 나올 것
그 뒤로 구현하는데는 크게 문제 없었음

## 어려웠던 점
처음에 입력을 받는 것도 처음 보는 양식이라 좀 헷갈림

```python
import sys

sys.stdin = open('4836.txt')

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 처리
for tc in range(1, T+1):

    # 색칠할 영역 개수
    N = int(input())

    # 각 영역 정보 입력
    # y1 x1 y2 x2 color 형태
    # x[0] = y1, x[1] = x1, x[2] = y2, x[3] = x2, x[4] = color
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 10x10 좌표 생성
    blank_arr =[[0] * 10 for _ in range(10)]

    # 보라색(겹친 칸)의 개수
    cnt = 0

    # 입력 받은 사각형 영역을 하나씩 처리
    for x in arr:

        # r은 y좌표(행)
        # y범위: y1 ~ y2(포함)
        for r in range(x[0], (x[2]+1)):

            # c는 x좌표(열)
            # x범위: x1 ~ x2(포함)
            for c in range(x[1], x[3]+1):

                # 색상에 따라 값을 더해서 겹침(보라색) 표현
                # 빨강이면 +1
                # 파랑이면 +2
                # 둘 다 칠해지면 빨강 + 파랑 = 보라 +3
                if x[4] == 1:
                    blank_arr[r][c] += 1
                else:
                    blank_arr[r][c] += 2

                # 보라색이 된 값을 카운트
                if blank_arr[r][c] == 3:
                    cnt += 1

    print(f'#{tc} {cnt}')
```

## 1209. [S/W 문제해결 기본] 2일차 - Sum

## 코드 방향성 / 구상한 내용

처음엔 배웠던 델타 사용해보려고 헀는데,
도저히 모르겠음

그래서 그냥 행, 열, 대각선 다 따로 구해서 max값 구해버림 

## 어려웠던 점
델타로는 어떻게 푸는 지 모르겠음. 나중에 추가로 공부를 한 다음에 델타로 풀어봐야지

```python
import sys
from pprint import pprint

sys.stdin = open('1209.txt')

# 테스트 케이스
T = 10

# 행렬의 크기
size = 100

# 테스트 케이스 처리
for _ in range(1, T+1):

    # 테스트 케이스 번호
    tc = int(input())

    # 100x100행렬 입력
    arr = [list(map(int, input().split())) for _ in range(size)]

    # max 후보들을 담을 리스트
    # 행 최대값 / 열 최대값/ 대각선 1 합 / 대각선 2 합
    sum_max = []
    max_r = 0
    max_c = 0
    sum_d1 = 0
    sum_d2 = 0

    # 각 행의 합을 계산
    for r in range(size):
        sum_r = sum(arr[r])
        if max_r < sum_r:
            max_r = sum_r
        sum_max.append(max_r)

    # 각 열의 합을 계산
    for c in range(size):
        sum_c = 0
        for r in range(size):
            sum_c += arr[r][c]
        if sum_c > max_c:
            max_c = sum_c
        sum_max.append(max_c)

    # 두 대각선의 합을 계산
    for r in range(size):
        for c in range(size):

            # 왼쪽 위 -> 오른쪽 아래 대각선
            if r == c:
                sum_d1 += arr[r][c]
                sum_max.append(sum_d1)

            # 오른쪽 위 -> 왼쪽 아래 대각선
            if r + c == (size-1):
                sum_d2 += arr[r][c]
                sum_max.append(sum_d2)


    print(f'#{tc} {max(sum_max)}')
```

## 1210. [S/W 문제해결 기본] 2일차 - Ladder1

## 코드 방향성 / 구상한 내용

미로 찾기나 사다리 타기 국룰인 도착점에서 반대로 올라가기 사용했음


## 어려웠던 점

구상은 완벽했던 것 같은데, 구현이 안되서 문제

구현 때문에 2시간은 넘게 사용한 듯

while로 반복할까 생각했는데
내가 생각한 구상이 그게 아니라서 그냥 끝까지 for문으로 구현하긴함

```python
import sys

sys.stdin = open('1210.txt')

# 테스트 케이스
T = 10

# 사다리 격자 크기 100x100
size = 100

for _ in range(1, T+1):
    tc = int(input())

    # 100x100 사다리 맵 생성
    arr = [list(map(int, input().split())) for _ in range(size)]

    # 도착점(2)의 위치 찾기
    for j in range(size):
        if arr[size-1][j] == 2:
            c = j

    # 도착점부터 꼭대기까지 역추적 반복
    # 현재 행에서 좌 또는 우에 길이 있으면 길 끝까지 이동 후 행 이동 반복
    for r in range(size-1, 0, -1):

        # 좌측에 길이 있으면 끝까지 이동
        if c - 1 > 0 and arr[r][c-1] == 1:
            for nc in range(c-1, -1, -1):
                if arr[r][nc] == 1:
                    c = nc
                else:
                    # 길 끊기면 종료
                    break

        # 우측에 길이 있으면 끝까지 이동
        elif c + 1 < size and arr[r][c+1] == 1:
            for nc in range(c+1, size):
                if arr[r][nc] == 1:
                    c = nc
                else:
                    # 길 끊기면 종료
                    break

        # 좌 / 우 둘 다 길이 없으면 아무 행동하지 않고 r이 1 감소함

    # 최종적으로 도달한 c(열)이 출발점의 인덱스
    print(f'#{tc} {c}')
```
