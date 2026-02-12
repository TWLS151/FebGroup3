### 260210 IM 대비

## 포탈

## 코드 방향성 / 구상한 내용

시키는 것 따라함

포탈 통과하면 +1

뒤돌아가면 다시 끝까지 가

## 어려웠던 점
없음

```python
import sys
sys.stdin = open('portal.txt')

def count_portal(p):

    # 방을 방문했는지 확인
    visit_room = [0]*len(p)

    cnt = 0  # 포탈을 이동한 총 횟수
    i = 0    # 현재 위치한 방의 인덱스 (0번 방에서 시작)

    # 마지막 방에 방문할 때까지 반복
    while visit_room[-1] == 0:
        i += 1    # 현재 방 번호 1 증가
        cnt += 1  # 이동 횟수 증가

        # 아직 방문하지 않은 방이면
        if visit_room[i] == 0:
            visit_room[i] = 1  # 해당 방 방문 처리
            i = p[i]-1         # 포탈을 타고 이동
                               # p[i]는 1부터 시작하는 방이므로 -1
            cnt +=1            # 포탈 탔으니까 이동 횟수 증가
    
    # 마지막 이동은 도착 조건을 만족시키기 위한 중복 카운트이므로 -1
    return cnt-1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    portal = list(map(int, input().split()))

    ans = count_portal(portal)
    print(f'#{tc} {ans}')

```

## 당근 포장하기

## 코드 방향성 / 구상한 내용

전에 못 풀었던 n개로 나누는 문제가 생각남

그거에서 갑자기 힌트를 얻고 풀긴했음

## 어려웠던 점
sort를 안해서 답이 계속 틀림…

SWEA에 예시가 다 정렬이 되어있어서 되어있는줄…

```python
def carrot_div(c, n):
    # 당근 크기를 오름차순으로 정렬
    # → 같은 크기의 당근들이 연속해서 위치하도록 만들기 위함
    c.sort()

    box_limit = n // 2   # 각 상자에 들어갈 수 있는 최대 당근 개수
    box_diff = 9999      # 세 상자의 크기 차이의 최소값 (초기값은 충분히 큰 수)

    # i : 첫 번째 상자와 두 번째 상자의 경계
    # s = c[:i]
    for i in range(1, n - 1):

        # j : 두 번째 상자와 세 번째 상자의 경계
        # m = c[i:j], l = c[j:]
        for j in range(i + 1, n):

            # 세 상자로 분할
            s = c[:i]     # 첫 번째 상자
            m = c[i:j]    # 두 번째 상자
            l = c[j:]     # 세 번째 상자

            # 각 상자의 크기가 제한(N//2)을 넘지 않는지 확인
            # (각 상자에 최소 1개 이상은 들어 있음은 i, j 범위로 보장됨)
            if len(s) <= box_limit and len(m) <= box_limit and len(l) <= box_limit:

                # 같은 크기의 당근이 서로 다른 상자에 나뉘지 않도록 검사
                # - s의 마지막 값이 m에 있으면 같은 크기가 두 상자에 걸림
                # - m의 마지막 값이 l에 있으면 같은 크기가 두 상자에 걸림
                if s[-1] not in m and m[-1] not in l:

                    # 각 상자의 당근 개수
                    carrot_len = [len(s), len(m), len(l)]

                    # 세 상자 중 최대 개수와 최소 개수의 차이 계산
                    diff = max(carrot_len) - min(carrot_len)

                    # 차이를 최소화하는 경우 갱신
                    if box_diff > diff:
                        box_diff = diff

    # 가능한 분할이 한 번도 없었다면 -1 반환
    if box_diff == 9999:
        return -1

    # 세 상자의 개수 차이 최소값 반환
    return box_diff


# 테스트 케이스 처리
T = int(input())
for tc in range(1, T + 1):
    N = int(input())                    # 당근 개수
    Ci = list(map(int, input().split()))  # 당근 크기 목록

    ans = carrot_div(Ci, N)
    print(f'#{tc} {ans}')

```

## 경비병

## 코드 방향성 / 구상한 내용
델타 숙달한다고 생각


## 어려웠던 점

델타 + 배수 그러니까 for d랑 for v에서 순서를 반대로 생각함…

그래서 이걸 어떻게 브레이크를 하지 고민했음

```python
import sys
sys.stdin = open('guard.txt')

def find_space(arr, n):
    cnt = 0  # 감시되지 않은 빈 공간의 개수 카운트

    # 우, 하, 좌, 상 방향
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 감시 여부를 기록할 행렬
    # 1이면 감시되었거나, 벽이거나, 경비병
    # 0이면 감시되지 않는 곳
    cnt_arr = [[0]*n for _ in range(n)]

    # 모든 칸을 순회
    for r in range(n):
        for c in range(n):

            # 1(벽)인 경우 해당 칸은 막힌 공간
            s = arr[r][c]
            if s == 1:
                cnt_arr[r][c] = 1

            # 2(경비병)인 경우도 마찬가지
            elif s == 2:
                cnt_arr[r][c] = 1

                # 경비병 자리에서부터 4방향으로 감시 확장
                for d in range(4):
                    # 현재 위치에서 한 칸씩 멀어지며 탐색
                    for v in range(1,n):
                        nr = r + dr[d]*v
                        nc = c + dc[d]*v

                        # 격자 범위일 때만 처리
                        if 0 <= nr < n and 0 <= nc < n:

                            # 벽을 만나면 해당 방향 감시 중단
                            if arr[nr][nc] == 1:
                                break
                            else:
                                # 감시당하는 공간 추가
                                cnt_arr[nr][nc] = 1

    # 감시되고 있지 않은 공간의 개수 세기
    for r in range(n):
        for c in range(n):
            if cnt_arr[r][c] == 0:
                cnt += 1

    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = find_space(arr, N)
    print(f'#{tc} {ans}')
```

## 탑 쌓기

## 코드 방향성 / 구상한 내용

무거운 것 부터 하나씩 분배 후, 층수 곱하기 


## 어려웠던 점

읎음

```python
import sys
sys.stdin = open('tower.txt')

def tower_weight(w):
    """
    하나의 타워에 쌓인 블록 리스트 w에 대해
    아래에서부터 1, 2, 3의 가중치를 곱한 
    총 무게의 합을 구하는 함수
    """
    l = len(w)
    weight_sum = 0
    
    # i는 층 번호(1층부터 시작)
    for i in range(1, l+1):
        weight_sum += w[i-1]*i
    return weight_sum


def tower_maker(w1, w2, k):
    """
    두 개의 타워를 만들 때
    총 무게 계산 함수
    """
    
    # w1이 항상 더 크거나 같도록 맞추기
    if w1 < w2:
        w1, w2 = w2, w1
    
    # 블록들을 내림차순 정렬(무거운게 먼저 오도록)
    k.sort(reverse=True)

    # 두 번째 타워에 들어갈 블록
    # 가장 무거운 블록부터 하나씩, 짝수 인덱스만 선택
    w2_lst = k[0:w2+1:2]
    
    # 첫 번째 타워에 들어갈 블록
    # w2와 번갈아 배치된 나머지 블록과 남은 블록 전체
    w1_lst = k[1:w2+1:2] + k[w2+1:]
    
    # 각 타워의 가중 무게 합을 더해 반환
    return tower_weight(w1_lst) + tower_weight(w2_lst)



T = int(input())
for tc in range(1, T+1):
    N, W1, W2 = map(int, input().split())
    k = list(map(int, input().split()))

    ans = tower_maker(W1, W2, k)
    print(f'#{tc} {ans}')
```

## 러시아 국기 같은 깃발

## 코드 방향성 / 구상한 내용

처음에 떠오른 직관은 그리디라서 풀긴했는데 답은 틀림

그래서 그냥 당근 배분? 그거랑 비슷하게 푸니까 되긴함

## 어려웠던 점
없음

```python
import sys
sys.stdin = open('portal.txt')

def count_portal(p):

    # 방을 방문했는지 확인
    visit_room = [0]*len(p)

    cnt = 0  # 포탈을 이동한 총 횟수
    i = 0    # 현재 위치한 방의 인덱스 (0번 방에서 시작)

    # 마지막 방에 방문할 때까지 반복
    while visit_room[-1] == 0:
        i += 1    # 현재 방 번호 1 증가
        cnt += 1  # 이동 횟수 증가
import sys

sys.stdin = open('4613.txt')

def make_russia_flag(arr, n, m):
    """
    N x M 행렬 러시아 국기 비슷한 형태로 만들 때
    필요한 최소 색 변경 횟수를 구하는 함수
    W와 B, B와 R의 경계를 완전탐색하는 방식으로 각 구간의 비용을 구함
    """
    # 변경에 드는 최솟값은 전체를 변경해야하는 비용으로 설정
    min_cnt = n * m

    # i: B 구간 시작(=W 구간 끝)
    # j: R 구간 시작(=B 구간 끝)
    # W: 0..i-1, B: i..j-1, R: j..n-1
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            w_part = arr[:i]
            b_part = arr[i:j]
            r_part = arr[j:]
            
            # 현재 주어진 W, B, R 상황에서의 비용
            cnt = 0

            # W 영역은 'W'가 아닌 칸을 칠해야 함
            for row in w_part:
                for s in row:
                    if s != 'W':
                        cnt += 1

            # B 영역은 'B'가 아닌 칸을 칠해야 함
            for row in b_part:
                for s in row:
                    if s != 'B':
                        cnt += 1

            # R 영역은 'R'가 아닌 칸을 칠해야 함
            for row in r_part:
                for s in row:
                    if s != 'R':
                        cnt += 1
                        
						# 최솟값 갱신
            if cnt < min_cnt:
                min_cnt = cnt

    return min_cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    ans = make_russia_flag(arr, N, M)
    print(f'#{tc} {ans}')
```

## 행렬 찾기

## 코드 방향성 / 구상한 내용

빈 행렬을 만들고, 원래 행렬을 순회하며 화학 용기(부분 행렬)를 발견하면 크기를 재서 빈 행렬에 방문 표시를 하고 (중복 방문을 막기 위함) 부분 행렬의 크기와 개수를 반환하려고 함

## 어려웠던 점
코드도 좀 복잡하긴 했는데, 나름 구현하고자 한 방식대로 구현한 듯

근데 마지막 출력 부분이 어려웠음…

안찾아봤으면 1시간 더 써도 못했을듯?

```python
import sys
sys.stdin = open('1258.txt')

def find_submatrix(arr, n):
    blank_arr = [[0] * n for _ in range(n)]
    dr = [0, 1]
    dc = [1, 0]
    matrix_list = []
    cnt = 0
    for r in range(n):
        for c in range(n):
            s = arr[r][c]
            cnt_r = 0
            cnt_c = 0
            if s != 0 and blank_arr[r][c] == 0:
                cnt += 1
                for d in range(2):
                    for v in range(n):
                        nr = r + dr[d]*v
                        nc = c + dc[d]*v
                        if nr < n and nc < n:
                            if arr[nr][nc] == 0:
                                if d == 0:
                                    end_nc = nc
                                else:
                                    end_nr = nr
                                break

                            else:
                                if d == 0:
                                    cnt_c += 1
                                else:
                                    cnt_r += 1

                for x in range(r, end_nr+1):
                    for y in range(c, end_nc+1):
                        blank_arr[x][y] = 1

                matrix_list.append([cnt_r, cnt_c])

    return cnt, matrix_list


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt, lst = find_submatrix(arr, N)
    result = sorted(lst, key=lambda x: (x[0]*x[1], x[0]))

    ans = []
    for sub in result:
        for num in sub:
            ans.append(num)

    print(f'#{tc} {cnt}', *ans)
```

## Ladder2

## 코드 방향성 / 구상한 내용

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도착하게 되는 출발점의 x좌표를 출력한다.

## 어려웠던 점

```python
import sys
sys.stdin = open('1211.txt')

def find_min_route(arr, n):

    min_route = N * N
    min_point = 0

    for c in range(n):
        if arr[0][c] == 1:
            check = c
            r = 0
            cnt = 0
            while r < n-1:
                if c+1 < n and arr[r][c+1] == 1:
                    while c+1 < n and arr[r][c+1] == 1:
                        c += 1
                        cnt += 1

                elif c-1 >= 0 and arr[r][c-1] == 1:
                    while c-1 >= 0 and arr[r][c-1] == 1:
                        c -= 1
                        cnt += 1
                r += 1
                cnt += 1


            if min_route >= cnt:
                min_route = cnt
                min_point = check

    return min_point


T = 10
N = 100
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = find_min_route(arr, N)
    print(f'#{tc} {ans}')
```