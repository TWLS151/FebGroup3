## Start 1-2

### 4881 SWEA 배열 최소 합
- 이 문제를 풀면서 어려웠던 점 : itertools.product와 permutations를 중첩해 사용했으나, 이는 $O((N!)^2)$ 이상의 지수적인 시간 복잡도를 유발하여 런타임 에러가 발생했습니다. 완전 탐색 시 탐색 공간(Search Space)을 효율적으로 설정하는 것이 얼마나 중요한지 깨달았습니다.
- 이 문제를 풀면서 개선할 점 : 각 행에서 서로 다른 열을 하나씩 선택한다"는 조건은 결국 **열 인덱스의 순열**(**$N!$**)과 같다는 점을 파악하여 로직을 단순화했습니다. 
```python
# 4881 SWEA 배열 최소 합
# 요구사항 정리 -> 열이 겹치지 않고 행마다 최소값 구하는 문제
from itertools import permutations
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    min_matrix = [list(map(int, input().split())) for _ in range(N)]
    mini_sum_result = float('inf')
    for p in permutations(range(N)):
        current_sum = 0
        for i in range(N):
            current_sum += min_matrix[i][p[i]]
            if current_sum >= mini_sum_result:
                break       # 이미 최솟값보다 크면 탈출
        else:
            if current_sum < mini_sum_result:
                mini_sum_result = current_sum
    print(f'#{tc} {mini_sum_result}')
```

### 4837 SWEA 부분집합의 합
- 이 문제를 풀면서 어려웠던 점 : 서브셋(Subset)을 효율적으로 필터링하는 로직이 필요했습니다.
- 이 문제를 풀면서 개선할 점 : 비트 연산을 이용한 방법도 공부하도록 하겠습니다.
```python
# 4837 SWEA 부분집합의 합
# 요구사항 정리 -> 집합 A에 대한 부분집합 구하기
from itertools import combinations
A = [n for n in range(1, 13)]
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    subset_cnt = 0
    for i in combinations(A, N):
        if sum(i) == K:
            subset_cnt += 1
    print(f'#{tc} {subset_cnt}')
```

### 5102 SWEA 노드의 거리
- 이 문제를 풀면서 어려웠던 점 : 무향 그래프에서 최단 거리를 구하기 위해 재귀(DFS)를 시도했으나, 방문 처리 미흡으로 인한 무한 루프와 Recursion Error가 발생했습니다.
- 이 문제를 풀면서 개선할 점 : 가중치가 없는 그래프의 최단 경로는 **BFS**(**너비 우선 탐색**)가 정석임을 이해하고 deque를 활용해 구현했습니다. visited 배열에 단순 방문 여부가 아닌 **시작점으로부터의 거리**(**Level**)를 누적 저장하여 별도의 변수 없이도 간선의 개수를 한 번에 계산할 수 있도록 개선했습니다.
```python
# 5102 SWEA 노드의 거리
# 요구사항 정리 -> 무향그래프 정점 사이의 간선 수 세기, 인접 리스트 활용, 재귀
from collections import deque
def go_path_bfs(start_node, end_node, adj_list, V_num):
    visited = [0] * (V_num + 1)
    queue = deque([start_node])
    visited[start_node] = 1

    while queue:
        current = queue.popleft()

        if current == end_node:
            return visited[current] - 1

        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)
    return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    distance_info = []
    for _ in range(E):
        x, y = map(int, input().split())
        distance_info.append(x)
        distance_info.append(y)
    start, end = map(int, input().split())

    path_list = [[] for _ in range(V + 1)]
    for i in range(E):
        n1, n2 = distance_info[i * 2], distance_info[i * 2 + 1]
        path_list[n1].append(n2)
        path_list[n2].append(n1)

    print(f'#{tc} {go_path_bfs(start, end, path_list, V)}')
```

### 5189 SWEA 전자카트
- 이 문제를 풀면서 어려웠던 점 : 순열 생성 시 고정된 인덱스를 제외하는 처리와, 마지막 구역에서 다시 0번으로 돌아오는 경로를 인덱싱하는 과정에서 TypeError 등 잔실수가 있었습니다.
- 이 문제를 풀면서 개선할 점 : `permutations(range(1, N))`를 통해 사무실을 제외한 경로만 순열로 생성하여 연산량을 최적화했습니다.
```python
# 5189 SWEA 전자카트
# 요구사항 정리 -> 처음과 마지막 인덱스 1로 고정, 나머지 인덱스 순열 정리
from itertools import permutations
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    work_matrix = [list(map(int, input().split())) for _ in range(N)]
    min_battery_used = float('inf')
    for i in permutations(range(1, N)):
        battery_used = 0
        battery_used += work_matrix[0][i[0]]
        battery_used += work_matrix[i[-1]][0]
        for k in range(len(i) - 1):
            battery_used += work_matrix[i[k]][i[k+1]]
        if battery_used < min_battery_used:
            min_battery_used = battery_used
    print(f'#{tc} {min_battery_used}')
```