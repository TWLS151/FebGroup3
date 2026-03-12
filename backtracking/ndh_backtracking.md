## Backtracking

### 5209 SWEA 최소 생산 비용
- 이 문제를 풀면서 어려웠던 점 : 가능한 경우의 수가 매우 많아지므로 시간 초과나 비효율이 걱정되었습니다.
- 이 문제를 풀면서 개선할 점 : `visited`를 리스트 대신 비트마스크 정수로 바꾸면 약간 더 빠르고 메모리 접근 비용을 줄일 수 있습니다.
```python
# 5209 SWEA 최소 생산 비용
def factory_cost(factory_idx, current_sum):
    global minimum_sum

    if current_sum >= minimum_sum: # 가지치기
        return  # 최솟값보다 이미 큰 값은 더 탐색하지 않습니다.

    if factory_idx == N:
        minimum_sum = min(current_sum, minimum_sum)
        return

    for product_idx in range(N):
        if not visited[product_idx]:
            visited[product_idx] = True
            factory_cost(factory_idx + 1, current_sum + cost_matrix[factory_idx][product_idx])
            visited[product_idx] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost_matrix = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    minimum_sum = float('inf')

    factory_cost(0, 0)

    print(f'#{tc} {minimum_sum}')
```

### 1231 SWEA 중위순회
- 이 문제를 풀면서 어려웠던 점 : 기초적인 중위순회 문제의 입력 방식과 차이가 있어서 이 부분에 어려움이 있었습니다.
- 이 문제를 풀면서 개선할 점 : 재귀 함수의 안전한 종료 조건을 `if node > V or text_list[node] == 0: return`처럼 명확히 해 예외 상황을 방지할 필요가 있습니다.
```python
# 1231 SWEA 중위순회
def inorder(node):
    if node <= V:
        inorder(node * 2)
        print(text_list[node], end='')
        inorder(node * 2 + 1)
for tc in range(1, 11):
    V = int(input())

    text_list = [0] * (V + 1)

    for _ in range(V):
        info = input().split()
        node_idx = int(info[0])
        char = info[1]

        text_list[node_idx] = char

    print(f'#{tc} ', end='')
    inorder(1)
    print()
```