``` python
T = int(input())
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for test_num in range(1,T+1):
    N = int(input())
    visited = set()
    queue = deque()
    maze = [input() for _ in range(N)]
    check = False
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2': 
                visited.add((i,j))
                queue.append((i,j,0))
    while queue:
        x,y,moves = queue.popleft()
        visited.add((x,y))
        for i in range(4):
            if 0<=x+dx[i]<N and 0<=y+dy[i]<N and not (x+dx[i],y+dy[i]) in visited:
                if maze[x+dx[i]][y+dy[i]] =='3':

                    check = True
                    break
                elif maze[x+dx[i]][y+dy[i]] =='0':
                    # 추가
                    queue.append((x+dx[i],y+dy[i],moves+1))
        if check:
            break

    if check:
        print(f"#{test_num} {moves}")
    else:
        print(f"#{test_num} {0}")

```

브레이크문 이 어디서 깨지는지 잘 봐야하는 걸 깨달았습니다.


```python
T = 10
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for test_num in range(1,T+1):
    N = 16
    n = int(input())
    visited = set()
    queue = deque()
    maze = [input() for _ in range(N)]
    # print(maze)
    check = False
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2': 
                visited.add((i,j))
                queue.append((i,j,0))
    while queue:
        x,y,moves = queue.popleft()
        visited.add((x,y))
        for i in range(4):
            if 0<=x+dx[i]<N and 0<=y+dy[i]<N and not (x+dx[i],y+dy[i]) in visited:
                if maze[x+dx[i]][y+dy[i]] =='3':

                    check = True
                    break
                elif maze[x+dx[i]][y+dy[i]] =='0':
                    # 추가
                    queue.append((x+dx[i],y+dy[i],moves+1))
        if check:
            break

    if check:
        print(f"#{test_num} {1}")
    else:
        print(f"#{test_num} {0}")



```


같은 코드로 풀었어용


그리고 다른 문제들을 BFS로 풀었어요.
```python


from collections import deque
T = int(input())

for test_num in range(1,T+1):
    answer = 0
    queue = deque()
    visited = set()
    
    curr,target = map(int,input().split())
    queue.append((curr,0))
    visited.add(curr)
    while queue:
        curr,answer = queue.popleft()

        if curr == target:
            print(f'#{test_num} {answer}')
            break
        if 0<=curr*2 <= 1000000 and not (curr*2 in visited):
            queue.append((curr*2,answer+1))
            visited.add(curr*2)
        if 0<=curr +1 <=1000000 and not (curr+1 in visited):
            queue.append((curr+1,answer+1))
            visited.add(curr+1)
        if curr-1>=0 and not curr-1 in visited:
            queue.append((curr-1,answer+1))
            visited.add(curr-1)
        if curr-10>=0 and not curr-10 in visited:
            queue.append((curr-10,answer+1))
            visited.add(curr-10)
        
        ## 디큐 공부해야합니다....
        #활용형 처럼..
```
