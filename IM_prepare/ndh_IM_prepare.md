## IM prepare

### Царь-бомба 차르 봄바
```python
# Царь-бомба 차르 봄바
# 요구사항 정리 -> N*M 지역에 십자 모양의 범위 P인 폭탄 최대 화력을 구하는 것 (P는 요소의 값과 일치한다)
# 아이디어 -> 델타

T = int(input())

for test in range(1, T+1):
    N, M = map(int, input().split())
    boom = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    boom_effect_list = []

    for row in range(N):
        for col in range(M):
            P = boom[row][col]
            boom_num = P
            for i in range(4):
                for j in range(1, P+1):     # 정해진 방향에서 탐색을 진행한다.
                    nr = row + dr[i]*j
                    nc = col + dc[i]*j
                    if 0 <= nr < N and 0 <= nc < M:
                        boom_num += boom[nr][nc]
            boom_effect_list.append(boom_num)
    result = max(boom_effect_list)
    print(f'#{test} {result}')
```

### Score System 채점 시스템 만들기
```python
# Score System 채점 시스템 만들기
# 요구사항 분석 -> 연속번호 O 경우 점수 n + 1, 연속번호 X 경우 점수 1
# 아이디어 -> 문항 수 M과 동일한 0으로 채워진 리스트 설정하고 맞으면 1 아니면 0으로 채움, 1 연속되면 연속 점수 부여

T = int(input())

for test in range(1, T+1):
    N, M = map(int, input().split())
    correct_ans = list(map(int, input().split()))
    student_ans = [list(map(int, input().split())) for _ in range(N)]   # 여기까지 문제 입력값
    score_list = [[0]*M for _ in range(N)]      # 학생들의 문항별 점수를 담는 리스트입니다.
    student_number = 0                          # 인덱스 번호를 대체하기 위한 변수입니다.
    for student in student_ans:                 # 순서대로 학생 답안을 꺼냅니다.
        for i in range(M):                      # 2차원 탐색을 위한 이중 for문을 구성합니다.
            if student[i] == correct_ans[i]:    # 두 답안이 일치하는지 조건문을 통해서 탐색합니다.
                score_list[student_number][i] = 1       # 답안이 일치한다면 요소 0을 1로 대체합니다.
                if i > 0 and score_list[student_number][i-1] >= 1:  # 연속 정답인 경우를 탐색합니다.
                    score_list[student_number][i] = score_list[student_number][i-1] + 1     # 연속 가산 점수를 부여합니다.
        student_number += 1                     # 다음 학생 채점을 위해서 인덱스 번호를 1 올립니다.
    final_list = []                             # 최고점과 최저점 계산 위한 새 리스트를 만듭니다.
    for x in score_list:
        y = sum(x)                              # 2차원 리스트의 개별 점수들을 합산합니다.
        final_list.append(y)
    final_list.sort()
    output = final_list[-1] - final_list[0]     # 최고점과 최저점의 차이를 구합니다.
    print(f'#{test} {output}')
```

### Guard 경비병
```python
# Guard 경비병
# 요구사항 정리 -> N*N 공간에서 0이 통로, 2는 경비병, 1은 기둥??, 경비병은 상하좌우 N 만큼 탐색 가능, 이동 가능 공간 넓이
# 아이디어 -> 0을 모두 합산한 다음 2에서 상하좌우로 닿는 0 제외하는 방식으로 접근한다.
#          -> 또는 2를 먼저 찾아낸 다음 2와 바로 상하좌우로 연속하는 0들에 대해서 -1로 값을 변경한 다음 합산
#          -> 델타 활용에서 겪는 어려움
#          -> 2와 1 사이의 0들만 1로 변환해야 하는데 이 부분에 어려움이 있다.
#          -> 2부터 시선이 시작해서 상하좌우로 1이 없다면 해당 줄의 0을 전부 -1로 변환하고, 1이 존재한다면 0의 변환은 멈춘다.
T = int(input())

for test in range(1, T+1):
    N = int(input())
    campus_lobby = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for row in range(N):
        for col in range(N):
            if campus_lobby[row][col] == 2:         # 경비병을 만나는 조건
                for i in range(4):
                    for d in range(1, N):           # 정해진 방향에서 전진하면서 조건 탐색한다.
                        nr = row + dr[i]*d
                        nc = col + dc[i]*d
                        if not (0 <= nr < N and 0 <= nc < N):   # 경계값을 벗어난 경우 종료
                            break
                        if campus_lobby[nr][nc] == 1:           # 이미 1로 채워진 칸을 만나면 종료
                            break
                        if campus_lobby[nr][nc] == 0:           # 조건에 맞는 0을 탐색한다.
                            campus_lobby[nr][nc] = -1           # 해당 0들을 -1로 채운다.
        # print(campus_lobby)                       # 디버깅 코드
    aisle = 0                                       # 전체 행렬에서 0의 개수를 세고 담을 변수
    for go_home in campus_lobby:
        aisle += go_home.count(0)
    print(f'#{test} {aisle}')
```

### 4466 SWEA 최대 성적표 만들기
```python
# 4466 SWEA 최대 성적표 만들기
# 요구사항 정리 -> 입력된 N개의 성적 중 K개를 선택해서 최대의 점수 뽑아내기
# 아이디어 -> 정렬 후 최대값에서 K개 만큼 합산한다.

T = int(input())

for test in range(1, T+1):
    N, K = map(int, input().split())
    score_list = list(map(int, input().split()))
    score_list.sort()
    sum_max_score = 0       # 최대 점수를 담을 변수를 설정합니다.
    for i in range(K):      # 성적 K 개를 선택하고 반복합니다.
        sum_max_score += score_list[-1]     # 최대값을 더하고
        score_list.pop()                    # 해당 값을 제거하는 작업을 반복합니다.
    print(f'#{test} {sum_max_score}')
```

### 1220 SWEA Magnetic
```python
# 1220 SWEA Magnetic
# 요구사항 정리 -> 자기장 흐르는 테이블 위에 N극, 아래에 S극 있다. 앞에 장애물이 있어서 교착 상태인 횟수 구하기
# 아이디어 -> 각 열마다 상단에 장애물 없는 S(2)극 하단에 장애물 없는 N(1)극 제외, N극과 S극 직접 맞닿는 횟수 카운팅
#          -> 편의를 위해서 모든 칸의 공백(0)은 제외하고 1과 2만 자리 그대로 남긴 열을 만드는 작업을 먼저 진행한다.
#          -> 요구사항대로 최하단 1, 최상단 2 제외한다 (둘 모두 연속도 포함)
#          -> 정리된 열의 모습은 반드시 최상단 1로 시작해서 최하단 2로 끝난다.
#          -> 1과 2가 교차하는 횟수 카운팅하고 출력한다.

for test in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    mag_cnt = 0

    for col in range(N):
        # 1. 해당 열에서 0을 제외하고 N(1)과 S(2)만 추출하여 리스트를 생성한다.
        col_matrix = []
        for row in range(N):
            if matrix[row][col] != 0:
                col_matrix.append(matrix[row][col])

        # 2. 리스트를 순회하며 "1 다음에 바로 나오는 2"를 카운트
        # 상단 S(2)나 하단 N(1)은 자연스럽게 쌍을 이루지 못해 제외된다.
        for i in range(len(col_matrix) - 1):
            if col_matrix[i] == 1 and col_matrix[i + 1] == 2:
                mag_cnt += 1

    print(f'#{test} {mag_cnt}')
```

### 2805 SWEA 농작물 수확하기
```python
# 2805 SWEA 농작물 수확하기
# 요구사항 정리 -> N*N 정사각형에서 마름모 모양 경계 내부 모든 값의 합 구하기 (N은 항상 홀수)
# 아이디어 -> 마름모 슬라이싱해서 보면 열마다 값이 2n+1 (0<=n<N//2) 로 증가한다. 중간 기점 계산

T = int(input())

for test in range(1, T + 1):
    N = int(input())
    farm_matrix = [list(map(int, input())) for _ in range(N)]

    farm_count = 0
    mid = N // 2
    dist = 0      # 중심(mid)에서 위아래로 퍼져나갈 칸의 거리를 의미함

    for col in range(N):    # 열(col)을 기준으로 순회
        # 현재 열에서 수확할 행의 범위: (중심 - dist) ~ (중심 + dist)
        for row in range(mid - dist, mid + dist + 1):
            farm_count += farm_matrix[row][col]
        # 다음 열로 넘어가기 전, dist(확장 폭)를 조절
        if col < mid:
            # 중간에 도달할 때까지는 수확 범위가 넓어짐
            dist += 1
        else:
            # 중간을 지나면 다시 수확 범위가 좁아짐
            dist -= 1

    print(f'#{test} {farm_count}')
```