## Start 1-1

### SWEA 7465 창용 마을 무리의 개수
- 이 문제를 풀면서 어려웠던 점 : 마을 사람들의 연결 관계를 집합으로 정리하는 과정에서 어려움이 있었습니다.
- 이 문제를 풀면서 개선할 점 : 중복된 코드 부분을 보완하는 작업이 필요합니다. 
```python
# SWEA 7465 창용 마을 무리의 개수
# 요구사항 정리 -> 무향그래프 수 세기, 인접 행렬 또는 인접 리스트 활용

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())    # 정점(N), 간선(M) 개수
    neighbor_info = []
    for _ in range(M):
        x, y = map(int, input().split())
        neighbor_info.append(x)
        neighbor_info.append(y)

    relation_list = [[] for _ in range(N + 1)]                  # 인접 리스트
    for i in range(M):
        n1, n2 = neighbor_info[i * 2], neighbor_info[i * 2 + 1]
        relation_list[n1].append(n2)
        relation_list[n2].append(n1)

    idx = 1
    for party in relation_list[1:]:
        party.append(idx)
        idx += 1

    for i in range(1, N):
        for j in range(i + 1, N + 1):
            relation_inter = set(relation_list[i]) & set(relation_list[j])
            if relation_inter:
                relation_list[i] = list(set(relation_list[i]) | set(relation_list[j]))
                relation_list[j] = list(set(relation_list[i]) | set(relation_list[j]))

    for i in range(1, N):
        for j in range(i + 1, N + 1):
            relation_inter = set(relation_list[i]) & set(relation_list[j])
            if relation_inter:
                relation_list[i] = list(set(relation_list[i]) | set(relation_list[j]))
                relation_list[j] = list(set(relation_list[i]) | set(relation_list[j]))

    party_dict = {}
    for party in relation_list[1:]:
        party_dict[f"{party}"] = 1

    print(f"#{tc} {len(party_dict)}")
```

### SWEA 1267 작업순서
- 이 문제를 풀면서 어려웠던 점 : 아직 BFS로 응용 문제를 푸는 것에 많은 어려움이 있습니다.
- 이 문제를 풀면서 개선할 점 : 수업시간 정리 코드를 거의 그대로 사용했기 때문에 저만의 언어로 다시 작성하는 작업이 필요합니다.
```python
# SWEA 1267 작업순서
# 위상정렬의 올바른 진행 순서를 출력하는 문제
from collections import deque
for tc in range(1, 11):             # 10개의 테스트 케이스로 제한
    V, E = map(int, input().split())    # V개의 정점과 E개의 간선
    go_degree = [0] * (V + 1)           # 모든 노드의 진입차수를 0으로 초기화
    E_info_list = list(map(int, input().split()))
    connect_list = [[] for _ in range(V + 1)]   # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
    for i in range(E):      # 방향 그래프의 모든 간선 정보를 입력
        x, y = E_info_list[i * 2], E_info_list[i * 2 + 1]
        connect_list[x].append(y)   # 정점 x에서 y로 가는 간선
        go_degree[y] += 1           # y노드로 들어가는 진입차수 1 증가

    def workflow_sort():        # 위상정렬 함수
        result = []             # 알고리즘 수행 결과를 저장
        q = deque()
        for i in range(1, V+1):     # 진입 차수가 0인 노드를 큐에 삽입하고 시작
            if go_degree[i] == 0:
                q.append(i)
        while q:
            now = q.pop()       # 큐에서 다음 노드 꺼내기
            result.append(now)
            for i in connect_list[now]:     # 해당 노드와 연결된 노드들의 진입차수에서 1 빼기
                go_degree[i] -= 1
                if go_degree[i] == 0:       # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
                    q.append(i)
        print(*result)          # 수행 결과 출력

    print(f'#{tc}', end=' ')
    workflow_sort()
```