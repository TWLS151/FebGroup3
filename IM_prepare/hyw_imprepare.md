```python
T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for test_num in range(1,1+T):
    n = int(input())
    floor_map = []
    for _ in range(n):
        floor_map.append(list(map(int,input().split())))
    can_look = 0
    cnt =1#경비원 본인
    for i in range(n):
        for j in range(n):
            if floor_map[i][j] ==1:
                cnt+=1
            if floor_map[i][j] ==2:# 경비경 찾기
                for delta in range(4): #상하좌우를 돌며
                    for look in range(1,n):        
                        if 0<=i+dx[delta]*look<n and 0<=j+dy[delta]*look<n: #볼수 있는데 까지 보고
                            #범위 안에서 1 나오기 전까지 전부 추가
                            if floor_map[i+dx[delta]*look][j+dy[delta]*look]==1:
                                break
                            else:
                                can_look+=1
    # print(can_look)
    print(f'#{test_num} {n*n - can_look-cnt}')


```
```python
T = int (input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(x,y):
    global mountain ,N
    longest = 0 #만약 더 갈 곳이 없으면 0 +1 리턴
    for delta in range(4):
        if  0 <= x+dx[delta] <N and \
            0 <= y+dy[delta] < N and \
            mountain[x][y] > mountain[x+dx[delta]][y+dy[delta]] : # 범위 내에 있고 나보다 작은 곳이 있으면 가라 
            longest = max(longest, DFS(x+dx[delta],y+dy[delta]) )# 
        # print((x,y))
    return longest+1 #4가지 갈림길에서 가장 멀리 갈 수 있는 거리에다가 날 추가해서 출력
for test_num in range(1,T+1):
    N,K = map(int,input().split())
    mountain  = []
    for _ in range(N):
        mountain.append(list(map(int,input().split())))
        # 공원 전체 입력 받음
    max_val = max(map(max, mountain))
        # 그리곤 젤 높은 높이 확인
        # 위치도 확인 할것
    starts = []
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_val:
                starts.append((i,j))
    
    # 모든 곳 숫자를 빼보면서 산책로 경우의 수 구하기
    answer = 0
    for k in range(K+1):
        
        for i in range(N):
            for j in range(N):
                # if i ==2 and j ==3:
                mountain[i][j] -= k # 빼고 구해봄
                temp = 0
                for x in range(N):
                    for y in range(N):
                        if mountain[x][y] == max_val:
                            t = DFS(x,y)
                            if temp < t:
                                temp = t
                    if answer < temp:
                        answer = temp
                mountain[i][j] += k # 공사 원복


    print(f'#{test_num} {answer}')
```
```python
T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for test_num in range(1,T+1):
    N,M = map(int,input().split())
    bombs = []
    for _ in range(N):
        bombs.append(list(map(int,input().split())))
    answer = 0
    for i in range(N):
        for j in range(M):
            temp = bombs[i][j]
            for blast in range(1,bombs[i][j]+1):
                for delta in range(4):
                    if 0<=i+dx[delta]*blast<N and 0<=j+dy[delta]*blast<M:
                        temp+= bombs[i+dx[delta]*blast][j+dy[delta]*blast]
            if temp > answer:
                answer =temp
    print(f'#{test_num} {answer}')
```