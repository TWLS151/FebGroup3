# 스트링 매드무비 찍을라다 참았습니다.



## 팰린드롬 계산하기
```python 
T = int(input())
for test_num in range(1,T+1):
    S = input()
    check = True
    for i in range(len(S)//2):
        if S[i] ==S[-1-i] :
            pass
        else: 
            check = False
    if check:
        print(f'#{test_num} {1}')
    else:
        print(f'#{test_num} {0}')

```
## 안에 몇개있나 확인하기 - > 카운트
```python
T = int(input())
for test_num in range(1,T+1):
    A = input()
    B = input()
    l = []
    for i in range(len(A)):
        l.append(B.count(A[i]))
    print(f'#{test_num} {max(l)}')


```
## 있는지 없는지 확인하기
```python
T = int(input())
for test_num in range(1,T+1):
    A = input()
    B = input()
    if A in B:
        print(f'#{test_num} {1}')
    else:
        print(f'#{test_num} {0}')

```