```python
T = int(input())
for test_case in range(1,T+1):
    cw,tw = map(int,input().split())
    cws = list(map(int,input().split()))
    tws = list(map(int,input().split()))
    cws.sort()
    tws.sort()
    answer = 0
    for i in range(cw):
        a = cws.pop()

        for j in tws:
            if a <= j:
                answer+=a
                tws.remove(j)
                break
    
    print(f'#{test_case} {answer}')
```


```python
T = int(input())
for test_num in range(1,T+1):
    N = int(input())
    L = [tuple(map(int,input().split())) for _ in range(N)]

    L.sort(key=lambda x:(x[1],x[0]))

    curr = 0
    cnt = 0

    for s,e in L:
        if s >= curr:
            curr = e
            cnt +=1

    print(f'#{test_num} {cnt}')
```


