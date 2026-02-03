# SWEA 1945. 간단한 소인수분해

## 코드 방향성 / 구상한 내용
소수로 나누고 지수를 저장

## 어려웠던 점
while 부분을 처음에 != 0으로 해놓고 결과가 안나와서 답답했음

```python
import sys

sys.stdin = open('1945.txt')
# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    
    # 소인수분해 할 정수 N
    N = int(input())
    
    # 문제에서 요구하는 소수 목록 리스트
    prime_list = [2, 3, 5, 7, 11]
    
    # 각 소수의 지수를 저장할 리스트
    exponent_list = [0]*5

    # 각 소수에 대해서 나눌 수 있을 때까지 반복
    for num in range(len(prime_list)):
        
        # 현재 소수로 N이 더 이상 나누어지지 않을 때까지 반복
        while (N % prime_list[num]) == 0:
            N = N / prime_list[num]
            
            # 해당 소수의 지수 +1
            exponent_list[num] += 1


    print(f'#{tc}', *exponent_list)
```