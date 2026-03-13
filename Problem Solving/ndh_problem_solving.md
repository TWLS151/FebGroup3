## Problem Solving 1

### 1953 SWEA 탈주범 검거
- 이 문제를 풀면서 어려웠던 점 : 방향과 반대 방향을 매핑(`opp`)하여 연결 가능 여부를 검증하는 로직 설계
- 이 문제를 풀면서 개선할 점 : `visited[curr_r][curr_c] >= L` 조건을 큐에서 꺼낸 후 체크하는데, 큐에 넣을 때 미리 조건을 확인하면 불필요한 큐 삽입을 줄일 수 있음
```python
# 1953 SWEA 탈주범 검거
from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
pipe = [           # 파이프 종류 리스트
    [],            # 빈 공간(통로 없음)
    [0, 1, 2, 3],  # 1. 상하좌우 연결
    [0, 1],
    [2, 3],
    [0, 3],
    [1, 3],
    [1, 2],
    [0, 2]          # 7. 상좌 연결
]
opp = {0: 1, 1: 0, 2: 3, 3: 2}  # 반대 방향 매핑 딕셔너리

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    pipe_matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]   # 방문 여부 + 목적지 도달까지 시간 소요

    visited[R][C] = 1        # 출발점 = 1(시작)
    queue = deque([(R, C)])

    while queue:  # 
        curr_r, curr_c = queue.popleft()

        if visited[curr_r][curr_c] >= L:  # 시간 초과의 경우 가지치기
            continue

        curr_p = pipe_matrix[curr_r][curr_c]

        for direction in pipe[curr_p]:     # 현재 파이프가 열린 방향만 탐색
            nr, nc = curr_r + dr[direction], curr_c + dc[direction]
            # 경계값 만족 and 빈 공간 제외 and 미방문 경우를 동시에 만족하는 경우에 대해서만 탐색 진행
            if 0 <= nr < N and 0 <= nc < M and pipe_matrix[nr][nc] > 0 and not visited[nr][nc]:
                next_p = pipe_matrix[nr][nc]
                # 반대 방향 매핑 딕셔너리로 (양방향)연결 가능 여부 확인
                if opp[direction] in pipe[next_p]:  
                    visited[nr][nc] = visited[curr_r][curr_c] + 1
                    queue.append((nr, nc))

    move_cnt = 0
    for row in visited:
        for cell in row:
            if cell > 0:
                move_cnt += 1
    print(f'#{tc} {move_cnt}')
```

### 10580 SWEA 전봇대
- 이 문제를 풀면서 어려웠던 점 : 왼쪽 기준으로 정렬했을 때, 오른쪽 값이 역전되는 쌍의 수가 교차 횟수임을 파악하는 것 (LIS 문제와 연관성 이해)
- 이 문제를 풀면서 개선할 점 : 변수명 `w`를 `wires`처럼 의미 있는 이름으로 개선하면 가독성 향상
```python
# 10580 SWEA 전봇대
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    w=sorted(tuple(map(int,input().split())) for _ in range(N))
    ans=0
    for i in range(N):
        for j in range(i):
            if w[j][1] > w[i][1]:
                ans+=1
    print(f'#{tc} {ans}')
```

### 20551 SWEA 증가하는 사탕 수열
- 이 문제를 풀면서 어려웠던 점 : `a < b < c` 조건을 만족시키려면 c → b → a 순서로 줄여야 한다는 방향 설정
- 이 문제를 풀면서 개선할 점 : `original_b`, `original_a`를 따로 저장하는 대신 더 간결한 계산 방법 적용
```python
# 20551 SWEA 증가하는 사탕 수열
T = int(input())

for tc in range(1, T+1):
    a, b, c = map(int, input().split())

    if b < 2 or c < 3:
        print(f'#{tc} -1')
        continue

    original_b, original_a = b, a

    b = min(b, c-1)
    a = min(a, b-1)

    eat = (original_b-b) + (original_a-a)

    print(f'#{tc} {eat}')
```

### 1486 SWEA 장훈이의 높은 선반
- 이 문제를 풀면서 어려웠던 점 : 모든 부분집합을 탐색하는 비트마스킹 방식을 적용하는 것
- 이 문제를 풀면서 개선할 점 : 현재 각 서브셋마다 `tmp` 리스트를 만들고 `sum()`을 두 번 호출하는데, 누적 합산으로 단일 패스 처리 가능
```python
# 1486 SWEA 장훈이의 높은 선반
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height_list = list(map(int, input().split()))
    diff_num = float('inf')

    for subset_mask in range(1 << N):
        tmp = []
        for j in range(N):
            if subset_mask & (1 << j):
                tmp.append(height_list[j])

        if sum(tmp) >= B and sum(tmp) - B < diff_num:
            diff_num = sum(tmp) - B

    print(f'#{tc} {diff_num}')
```

### 1861 SWEA 정사각형 방
- 이 문제를 풀면서 어려웠던 점 : 매 칸에서 출발하는 완전탐색이라 중복 계산이 발생할 수 있다는 점, 이동 횟수가 같을 때 방 번호가 더 작은 쪽을 선택해야 하는 조건을 놓치기 쉬움
- 이 문제를 풀면서 개선할 점 : 현재 모든 칸에서 다시 탐색하므로 `O(N³)` 수준인데, `DP` `메모이제이션` 활용을 통해서 재사용하면 `O(N²)`으로 개선 가능
```python
# 1861 SWEA 정사각형 방
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [list(map(int, input().split())) for _ in range(N)]

    # 최댓값을 저장할 변수들
    max_count = 0  # 가장 많이 이동한 횟수
    start_room = float('inf')  # 그때의 출발 방 번호

    for row in range(N):
        for col in range(N):
            # 현재 방에서 출발
            now_r, now_c = row, col
            cnt = 1  # 현재 방도 포함하니까 1부터 시작

            while True:
                found = False
                # 상하좌우 네 방향 확인
                for i in range(4):
                    nr = now_r + dr[i]
                    nc = now_c + dc[i]

                    # 1. 방 범위를 안 벗어나고
                    # 2. 다음 방 숫자가 현재 방 숫자보다 정확히 1 크다면?
                    if 0 <= nr < N and 0 <= nc < N and square[nr][nc] == square[now_r][now_c] + 1:
                        now_r, now_c = nr, nc  # 이동
                        cnt += 1
                        found = True
                        break  # 1 큰 방은 오직 하나뿐이라 찾으면 바로 다음으로

                # 만약 주변에 더 이상 갈 수 있는 방(1 큰 방)이 없다면 중단
                if not found:
                    break

            # 모든 이동이 끝난 후, 최댓값 갱신하기
            if cnt > max_count:
                max_count = cnt
                start_room = square[row][col]
            elif cnt == max_count:
                # 이동 횟수가 같다면, 더 작은 방 번호 선택
                start_room = min(start_room, square[row][col])

    print(f"#{tc} {start_room} {max_count}")
```