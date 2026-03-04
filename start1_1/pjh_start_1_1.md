### 260304 start1_1

## 미로

# 코드 구현 방향
BFS 또는 DFS

# 어려웠던 점
없음

```python
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def find_start(arr, n):
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 2:
                return r, c

def maze(r, c):
    if arr[r][c] == 3:
        return True

    visited[r][c] = True

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and not visited[nr][nc]:
            if maze(nr, nc):
                return True
    return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    r, c = find_start(arr, N)
    ans = maze(r, c)
    if ans:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
```


## 공통조상

# 코드 구현 방향
어떤 알고리즘인지 모르겠음?

# 어려웠던 점
break 넣는 게 어려워요

```python
import sys
sys.stdin = open('1248.txt')


def postorder(node):
    """
    후위 순호로 node를 루트로 하는 서브 트리의 모든 노드를 방문
    방문한 노드를 len_node 리스트에 추가
    """
    if node != 0:
        postorder(left[node])
        postorder(right[node])
        len_node.append(node)

T = int(input())
for tc in range(1, T+1):
    V, E, n1, n2 = map(int, input().split())
    lst = list(map(int, input().split()))

    # 이진트리
    # left: p의 왼쪽 자식
    # right: p의 오른쪽 자식
    left = [0]*(V+1)
    right = [0]*(V+1)

    # 간선 정보를 left, right 배열에 넣기
    for i in range(E):
        parent = lst[i*2]
        child = lst[i*2+1]

        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    # n1의 조상 목록
    n_1 = []

    # 왼쪽 오른쪽 자식 배열을 한번에 순회할 수 있게
    child = [left, right]

    # n1부터 후보로 놔둠
    x = n1
    n_1.append(x)

    # 루트가 1이니까, x가 1이 될 때까지 부모를 계속 찾아오르기
    while x != 1:

        # 이번 싸이클에서 '부모를 찾았는 지' 표시
        found = False

        # left/right 배열을 훑으며 x를 자식으로 찾는 부모 찾기
        # child[i][j] == x인 j가 x의 부모
        for i in range(2):
            for j in range(V+1):
                if child[i][j] == x:
                    # 부모를 조상 목록에 추가
                    n_1.append(j)

                    # x를 부모로 갱신
                    # 그 다음 부모를 찾아야하기 때문
                    x = j
                    found = True
                    break
            if found:
                break

    # n1의 조상들을 set로 만듦
    # 주석 달면서 생각해보니 리스트여도 상관 없을듯
    # 원래 n2도 한번에 하려고 set를 사용했는데
    # 방법을 바꿔서 set로 남아있는듯...
    chosang = set(n_1)

    # n2에서 위로 올라가며 n1 조상 set에 처음 걸리는 노드가 ans
    x = n2

    # x가 n1의 조상 집합에 없으면 계속 올라가기
    while x not in chosang:
        found = False

        # n1과 같은 방법으로 x 부모 노드를 반복해서 찾음
        for i in range(2):
            for j in range(V+1):
                if child[i][j] == x:
                    x = j
                    found = True
                    break
            if found:
                break

    # 반복을 끝내면 x가 공통 조상임
    ans = x
    
    
    len_node = []   # 방문한 노드를 담아 개수를 세기 위한 리스트
    postorder(ans)  # 후위 순회로 ans 서브트리 전체 방문
								    # 전, 중, 후위 상관 X

    print(f'#{tc} {ans} {len(len_node)}')
```

## 작업순서

# 코드 구현 방향
BFS인데, A형 1번 문제와 거의 동일함
A형 풀 때 시간이 더 있었더라도 내가 풀 수 있을까? 하면 아닌듯
그래도 대충은 이해함
몇번 더 풀어보면 감 잡을듯

# 어려웠던 점
all

```python
import sys
from collections import deque

sys.stdin = open('1267.txt')

T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    work = list(map(int, input().split()))

    adj = [[] for _ in range(V+1)]
    grade = [0] * (V+1)

    for i in range(E):
        f, t = work[2*i], work[2*i+1]
        adj[f].append(t)
        grade[t] += 1

    q = deque()
    for i in range(1, V+1):
        if grade[i] == 0:
            q.append(i)

    result = []
    while q:
        w = q.popleft()
        result.append(w)

        for nxt in adj[w]:
            grade[nxt] -= 1
            if grade[nxt] == 0:
                q.append(nxt)

    print(f'#{tc}', *result)
```