### 260204 List2_1

## 1.1(기본) / 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

## 코드 방향성 / 구상한 내용

셀렉션 알고리즘을 통해서 큰 숫자와 작은 숫자를 앞에서부터 순서대로 놓아야하는데,

일단 오름차순으로 정리해봄

그리고 인덱스가 짝수면 큰 숫자, 홀수면 작은 숫자를 교환해야겠다는 생각을 가지게 됨

## 어려웠던 점
없음

```python
import sys

sys.stdin = open('4843.txt')

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 입력
for tc in range(1, T+1):

    # 수열의 길이
    N = int(input())

    # 정렬한 숫자 리스트
    numbers = list(map(int, input().split()))

    # 선택 정렬 기반하여
    # i가 짝수면 -> 큰 값
    # i가 홀수면 -> 작은 값
    # 결과 형태:
    # [최대, 최소, 2번째 최대, 2번째 최소, ...]
    for i in range(N-1):

        # 현재 위치 i에 들어갈 값의 인덱스
        max_min_val = i

        # i 구간 이후 조건에서 맞는 값 탐색
        for j in range(i+1, N):

            # i가 짝수라면 구간 내 가장 큰 값
            if i % 2 == 0 and numbers[max_min_val] < numbers[j]:
                max_min_val = j

            # i가 홀수라면 구간 내 가장 작은 값
            elif i % 2 == 1 and numbers[max_min_val] > numbers[j]:
                max_min_val = j
        # 선택된 값과 현재 위치 i의 값을 교환
        numbers[i], numbers[max_min_val] = numbers[max_min_val], numbers[i]

    # 문제 요구사항인 정렬 결과 중 앞의 10개만 출력
    print(f'#{tc}', *numbers[:10])
```

## 1966. 숫자를 정렬하자

## 코드 방향성 / 구상한 내용

그냥 선택 정렬 연습한다고 생각하고 구현

## 어려웠던 점
없음

```python
import sys

sys.stdin = open('1966.txt')

# 선택 정렬 함수
def selection_sort(arr, n):
    # 선택 정렬(오름차순)
    # i번째 자리에 들어갈 가장 작은 값을 i 구간 이후 찾아서 교환하는 방식
    for i in range(n-1):
        # 현재 구간에서 최소 값의 인덱스
        min_val = i

        # i 다음 위치부터 끝까지 탐색
        for j in range(i + 1, n):

            # 더 작은 값이 발견되면 인덱스 갱신
            if arr[min_val] > arr[j]:
                min_val = j

        # i번째 값과 최소값 위치의 값을 교환
        arr[i], arr[min_val] = arr[min_val], arr[i]

    return arr

# 테스트 케이스 입력
T = int(input())

# 테스트 케이스 처리
for tc in range(1, T+1):

    # 정렬할 숫자의 개수
    N = int(input())

    # 정렬 대상 숫자 리스트
    numbers = list(map(int, input().split()))

    # 함수 호출
    answer = selection_sort(numbers, N)

    print(f'#{tc}', *answer)
```

## 12712. 파리퇴치3

## 코드 방향성 / 구상한 내용

델타를 정직하게 사용한다고 생각.

근데 십자모양과 x모양 스프레이 함수를 한번에 짜고 싶었는데, 

더 생각하기 귀찮아서 그냥 함


## 어려웠던 점

NO

```python
import sys

sys.stdin = open('12712.txt')


def plus_spray(arr, M):
    """
    + 모양 분사:
    현재 칸을 중심으로 상/하/좌/우 방향으로
    거리 1 ~ M-1 까지의 값을 더해
    촤대로 잡을 수 있는 파리의 수를 구한다.
    """

    # 상, 우, 하, 좌 방향 델타
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # + 모양 분사 중 최대로 잡을 수 있는 파리 수
    max_fly = 0

    # 격자의 모든 칸을 분사 중심으로 탐색
    for r in range(N):
        for c in range(N):

            # 현재 칸의 파리 수가 기본 값
            s = arr[r][c]

            # 4방향 탐색 시작
            for d in range(4):

                # 분사 거리별 탐색
                for v in range(1, M):
                    nr = r + dr[d]*v
                    nc = c + dc[d]*v

                    # 격자 범위 안이면 파리 수 누적
                    if 0 <= nr < N and 0 <= nc < N:
                        s += arr[nr][nc]

            # 현재 분사가 파리 최대 킬이면 갱신
            if max_fly < s:
                max_fly = s
    return max_fly

def x_spray(arr, M):
    """
    x 모양 분사:
    현재 칸을 중심으로 대각선 4방향으로
    거리 1 ~ M-1까지의 값을 더해
    최대로 잡을 수 있는 파리의 수를 구한다.
    """

    # 대각선 방향 델타
    dr = [1, 1, -1, -1]
    dc = [-1, 1, 1, -1]

    # x 모양 분사 중 최대로 잡을 수 있는 파리 수
    max_fly = 0
    # 격자의 모든 칸을 분사 중심으로 탐색
    for r in range(N):
        for c in range(N):

            # 현재 칸의 파리 수가 기본 값
            s = arr[r][c]

            # 4방향 탐색 시작
            for d in range(4):

                # 분사 거리별 탐색
                for v in range(1, M):
                    nr = r + dr[d] * v
                    nc = c + dc[d] * v

                    # 격자 범위 안이면 파리 수 누적
                    if 0 <= nr < N and 0 <= nc < N:
                        s += arr[nr][nc]

            # 현재 분사가 파리 최대 킬이면 갱신
            if max_fly < s:
                max_fly = s
    return max_fly

# 테스트 케이스 입력
T = int(input())

# 테스트 케이스 처리
for tc in range(1, T+1):

    # N: 격자 크기, M: 분사 범위
    N, M = map(int, input().split())

    # N x N 격자 입력(파리 개수)
    arr = [list(map(int, input().split())) for _ in range(N)]

    # + 스프레이 분사 결과
    answer1 = plus_spray(arr, M)

    # x 스프레이 분사 결과
    answer2 = x_spray(arr, M)

    # 두 분사 방식 중 최대값 출력
    print(f'#{tc} {max(answer1, answer2)}')
```

## 16504. Gravity

## 코드 방향성 / 구상한 내용

회전된 상태의 상자를 만듦(상자는 1, 빈 공간은 0)

반시계 방향으로 상자를 회전 시킴

그리고 한 행마다 열을 훑으며 상자 오른쪽에 있는 0을 카운트함


## 어려웠던 점

그냥 처음 생각한 가장 높은 수 오른쪽에 있는 걸로 할껄;

```python
import sys

sys.stdin = open('gravity.txt')

# 테스트 케이스 입력
T = int(input())

# 테스트 케이스 처리
for tc in range(1, T+1):

    # 박스 개수
    N = int(input())

    # 각 열에 쌓인 박스의 높이
    box_list = list(map(int, input().split()))

    # 전체 박스 중 가장 높은 높이
    # 새 2차원 행렬의 세로 크기로 사용
    height = max(box_list)

    # 박스 배열을 2차원 행렬로 표현
    # box[i][j] = 1 : i번째 열의 j번째 높이에 박스가 있음
    # box[i][j] = 0 : 비어있음
    box = [[0]*(height) for _ in range(N)]

    # 각 열마다 아래부터 1로 채움
    for i in range(N):
        for j in range(height):
            if j < box_list[i]:
                box[i][j] = 1

    # 반대로 회전
    # 왜 why?
    # 처음에 상자를 쌓은 행렬을 90도 돌아간 상태로 만들어서
    # 원래 상태로 만들기 위함
    rotated_90_left_box = list(map(list, zip(*box)))[::-1]

    # 박스가 떨어질 수 있는 최대 거리
    max_zero = 0

    # 회전된 박스에서 각 행 확인
    # 회전된 박스는 열이 진행되는 것이 떨어지는 거리임
    for x in rotated_90_left_box:

        # 각 행 내에서 인덱스 탐색
        for i in range(len(x)):

            # 박스(1)을 발견하면
            if x[i] == 1:

                # 해당 박스 오른쪽에 있는 빈 공간(0)의 개수 계산
                # 박스가 떨어질 수 있는 거리
                drop = x[i:].count(0)

                # 최대 낙하 거리 재할당
                if drop > max_zero:
                    max_zero = drop

    print(f'#{tc} {max_zero}')
```