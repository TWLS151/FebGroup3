# List1-1

오늘은 리스트와 관련된 알고리즘을 배웠습니다.


하여 SWEA의 문제들을 풀었습니다.

## 1. swea 4834 
```python
T = int(input())
# 테스트 케이스 수 만큼 반복
for i in range(T):
    N = int(input())
    # 카드 덱 입력
    decks = input()
    # 카드 개수를 세기 위한 딕셔너리
    cards = {}
    for j in range(N):
        # 카드 덱의 각 카드를 확인
        if cards.get(int(decks[j])):
            # 이미 딕셔너리에 있으면 개수 1 증가
            cards[int(decks[j])] += 1
        else:
            # 딕셔너리에 없으면 개수 1로 초기화
            cards[int(decks[j])] = 1
    # 카드 개수로 정렬, 개수가 같으면 카드 숫자로 정렬
    answer = sorted(cards.items(), key=lambda x: (x[1], x[0] ),reverse=True)[0]
    print(f'#{i+1} {answer[0]} {answer[1]}')
```

## 2. SWEA 4828
```python
N = int(input())

for i in range(N):
    _ = int(input())
    L = list(map(int,input().split()))
    print(f'#{i+1} {max(L)-min(L)}')
```




## 3.SWEA1206
```python
for i in range(10):
    N = int(input())
    L = list(map(int,input().split()))
    hap = 0
    for j in range(2,N-2,1):
        #돌면서 빈자리 찾기
        high = max(L[j-2],L[j-1],L[j+1],L[j+2])
        if L[j] > high:
            hap += (L[j] - high)
    print(f'#{i+1} {hap}')

```



## 4. 번외 버블소트

저는 추억을 되살리면서 버블소트를 재귀로 짜보았습니다.
```python

def bubbleSort(L:list):
    if len(L) == 1:
        return L
    else:
        length = len(L)
        for i in range(length-1):
            if L[i] > L[i+1]: #큰게 뒤로 가게 정렬
                L[i],L[i+1] = L[i+1],L[i]
        return bubbleSort(L[:-1]) + [L[-1]]
        # 맨 뒤까지는 정열되었으니까, 그거 빼고 반복



```