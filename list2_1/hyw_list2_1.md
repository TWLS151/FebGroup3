

## 달팽이 문제 1954풀었습니다.
```python 

def move(x,y,dir):
    if dir == 0:
        return x,y+1
    elif dir == 1:
         return x+1,y
    elif dir == 2:
        return x,y-1
    else :
         return x-1,y
def turn_check(x,y):
    global answer
    global N
    if x < 0 or y < 0 or x==N or y==N:
        return True
    elif answer[x][y] !=0:
        return True
    else:
        return False
def  turn(dir:int ):
    if dir ==3:
        return 0
    else:
        return dir +1
    
T = int(input())
for testcase in range(1,T+1):
    direction = 0 #오른쪽 0 /아래 1/ 왼쪽 2/위쪽 3
    N = int(input())
    answer = [[0]*N for _ in range(N)]
    x,y = 0,0
    for steps in range(1, N*N+1):
        #벽이나 채워진 칸을 만나면 오른쪽으로 방향을 튼다.
        # 이 칸에 스텝 번호로 넣는다.
        answer[x][y] = steps
        # print(answer)
        dest_x,dest_y = move(x,y,direction)
        if turn_check(dest_x,dest_y):
            direction=turn(direction)
            dest_x,dest_y = move(x,y,direction)
        else:
            pass
        x,y = dest_x,dest_y
    print(f'#{testcase}')
    for i in answer:
        print(* i)


```



## 4836색칠하기 => 숫자 3 세기
```python
T = int(input())
for testcase in range(1,T+1):
    arr = [[0]*10 for _ in range(10)]
    answer = 0
    squares = int(input())
    for _ in range(squares):
        x1,y1,x2,y2,color = map(int,input().split())
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                arr[x][y] +=color
                if arr[x][y] == 3:
                    answer +=1
    print(f'#{testcase} {answer}')
```


## 2001 파리 퇴치
```python
T = int(input())
for test_num in range(1,T+1):
    N,M = map(int,input().split())
    status = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        hap = [0]
        for x in temp:
            hap.append(hap[-1] + x)
        status.append(hap)
    #파리상태 입력까지는 받았음 (가로행 누적합으로 받았음)
    snap = []
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            snap_once = 0
            for dr in range(M):
                snap_once += status[r + dr][c + M] - status[r + dr][c]
            snap.append(snap_once)
        
    print(f'#{test_num} {int(max(snap))}')

```
