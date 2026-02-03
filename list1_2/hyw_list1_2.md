# list 1-2 문제를 풀어봅시다.


## 카운팅 정렬


```python
def counting_sort(L:list):
    numbers= list(range(min(L),max(L)+1))
    answer = []
    #각숫자의 수를 세면서 그 수를 그 횟수만큼 추가
    for i in range(min(L),max(L)+1):
        C = L.count(i)
        for j in range(C):
            answer.append(i)

    return answer



    
    
arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr))  # [0, 1, 1, 1, 2, 3, 4, 4]
```
## 4835 구간합
``` python
T = int(input())

for i in range(1,T+1):
    N,M = map(int,input().split())
    L = list(map(int,input().split()))
    AL = []
    for j in range(N-M+1):
        
        AL.append(sum(L[j:j+M]))

    answer = max(AL) - min(AL)
    print(f'#{i} {answer}')


```
## 4831 전기버스
```python
T = int(input())

def greedy (curr,K):
    global CS
    # print(CS)
    L  = []
    for i in CS:
        if i <= curr+K:
            L.append(i)
    return L[-1]

    pass
for i in range(1,T+1):
    K,N,M = map(int,input().split())
    # K 한번 충전시 이동가능
    # N  종점 번호
    # M 충전소 갯수
    CS = list(map(int,input().split())) + [N]
    answer = -1
    curr = 0
    far = curr + K
    # CS안에서 가장 멀리 갈 수 있는 만큼 가고, 그걸 취득함
    while True:
        answer+=1
        curr_dest = greedy(curr,K)
        
        
        if curr_dest ==curr:
            answer = 0
            break
        curr = curr_dest
        if curr >= N:
            break 
    print(f'#{i} {answer}')
```
## 1208 평탄화
```python

def dump(L:list) -> list:
    L[-1]= L[-1]-1
    L[0] = L[0]+1
    return L

for i in range(1,11):
    dumps = int(input())
    ground = list(map(int,input().split()))
    # print(ground)
    #조건이 만족될때까지 반복
    while True:
        ground = sorted(ground)
        if ground[-1] - ground[0] == 1 or ground[-1] - ground[0] == 0:
            break 
        dump(ground)
        dumps -=1   
        if dumps ==0:
            break

    answer = max(ground)-min(ground)
    print(f'#{i} {answer}')

```
## 11092 최대 최소 간격
```python
T = int(input())
for i in range(1,T+1):
    len =int(input())
    L = list(map(int,input().split()))

    mi = min(L)
    ma = max(L)
    max_in = 0
    for j in range(len-1,-1,-1):
        if L[j] ==ma:
            max_in = j
            break
    
    print(f'#{i} { abs(max_in-L.index(mi)) }')
```
## 6485 삼성시의 버스 노선
```python
T = int (input())
for i in range(1,T+1):
    N = int(input())
    L = []
    buses = {}
    for j in range(N):
       S, D = map(int,input().split())
       for k in range(S,D+1):
            if buses.get(k):
               buses[k] +=1
            else:
               buses[k] = 1
    #여기서 버스 정류장 별로 지나가는 버스를 모두 추가해준다.
    P = int(input())
    answer = []
    for j in range(P):
        answer.append(int(input()))

    print(f'#{i}',end =' ')
    for j in answer:
        if buses.get(j):
            print(buses[j], end =' ')
        else:
            print(0,end =' ')
    if i ==T:
        pass
    else:
        print()

    

    #딕셔너리에서 없는 경우 문제가 발색하니까 유의하기
```
## 1945 간단한 소인수 분해
```python
T = int(input())
primes = (2,3,5,7,11)
for i in range(1,T+1):
    N = int(input())
    answer = [0,0,0,0,0]
    for j in  range(5):
        while N% primes[j]==0:
            answer[j]+=1
            N = N/primes[j]
    print(f'#{i}',*answer)
```
## 9386 연속한 1의 갯수
```python
T = int(input())

for i in range(1,T+1):
    answer = -1
    M = 0
    N = int(input())
    S = input()
    for j in range(N):
        if S[j] == '1':
            M+=1
        if S[j] == '0':
            if answer < M:
                answer = M
            M = 0
            #이 부분 에러를 멍청하게 못 잡아서 문제가 이썽ㅆ음.
        if j == N-1:
            if answer < M:
                answer = M
    print(f'#{i} {answer}')





```
## 26045 부분 수열 판별
```python
T = int(input())

def subsequence_check(Long:list,short:list):
    if short[0] not in Long:
        return False
    else:#들어있다면?? 들어있다면 거기까지 짤라야지
        if len(short) == 1:
            return True
        else:
            return subsequence_check(Long[Long.index(short[0])+1:],short[1:])


for i in range(1,T+1):
    _ = input()
    Long = list(map(int,input().split()))
    short = list(map(int,input().split()))
    if subsequence_check(Long,short):
        answer = 'YES'
    else:
        answer = "NO"


    print(f'#{i} {answer}')
```