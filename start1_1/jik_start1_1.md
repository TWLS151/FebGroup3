``` python

from itertools import combinations

t = int(input())

for tc in range(1,t+1) :
    n, b = map(int, input().split())
    h_list = list(map(int, input().split()))

    # s 초기값(조건 만족하는 최소 합을 찾기 위해 최대값으로 시작)
    s = sum(h_list)
    # 모든 조합 생성
    for i in range(n+1) :
        # i 명 뽑는 조합
        com = list(combinations(h_list,i))

        for j in range(len(com)) :
            c_s = sum(com[j])
            # 조합 키 합이 선반 높이 이상이고 현재 최솟값보다 작으면 갱신
            if b <= c_s and s > c_s:
                s = c_s
    # 선반 높이보다 초과된 높이 출력
    print(f'#{tc} {s-b}')

``` 


``` python

import sys
sys.stdin = open('03.txt')

t = int(input())
dxy = [[0,1],[0,-1],[1,0],[-1,0]]

for tc in range(1, t+1) :
    n = int(input())

    arr = [list(map(int,input().strip())) for _ in range(n)]

    visited = [list([0] * n) for _ in range(n)]
    result = 0
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 2:
                sr,sc = i, j
                
    visited[sr][sc] = 1
    stack = [(sr,sc)]

    while stack :
        r, c = stack.pop()

        for x, y in dxy :
            nx = r + x
            ny = c + y

            if not(0<= nx < n and 0<=ny <n) :
                continue
            if arr[nx][ny] == 1:
                continue
            if visited[nx][ny] == 1:
                continue
            if arr[nx][ny] == 3:
                result = 1
                break
            visited[nx][ny] = 1
            stack.append((nx,ny))
    print(f'#{tc} {result}')


``` 