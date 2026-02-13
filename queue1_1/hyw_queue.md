# 큐 문제를 두개 풀었습니다.


5097
```python
T = int(input())
for test_num in range(1,T+1):
    N,M = map(int,input().split())
    L = list(map(int,input().split()))
    print(f'#{test_num} {L[M%N]}')
```


5099
```python
T = int(input())
for test_num in range(1,1+T):
    N,M = map(int,input().split())
    oven = []
    pizzas = list(map(int,input().split()))
    for i in range(N):
        oven.append({i:pizzas.pop(0)})
    # print(oven)
    j = N
    while len(oven) > 1:
        curr = oven.pop(0)
        key = curr.keys()
        for i in key:
            key = i
            break

        if curr[key]//2 ==0:
            if len(pizzas) >= 1:
                oven.append({j:pizzas.pop(0)})
                j+=1
        else: 
            curr[key] = curr[key]//2
            oven.append(curr)
        # print(oven)
    key = oven[0].keys()
    for i in key:
            key = i
            break

    print(f'#{test_num} {key+1}')
```