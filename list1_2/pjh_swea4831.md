# SWEA 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스


## 코드 방향성 / 구상한 내용
문제에서 제안한 것처럼 전기 충전소 위치를 표시한 리스트를 구현한 후 현재 버스 위치와 비교해서 진행하려고 구상함

## 어려웠던 점
1. break를 적재적소에 사용할 수 있는 능력이 필요함
2. 저번 주 금요일에 2시간동안 고민해서 방향성을 정해놓았던 것이 오늘 푸는데 도움이 많이 됨

```python
import sys

sys.stdin = open('4831.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    M_station = list(map(int, input().split()))

    # 정류장 0 ~ N까지 충전소 여부를 확인할 리스트
    # N을 포함해야 하므로 길이는 N+1
    charge_location = [0]*(N+1)

    # 충전소 위치를 표시
    for c in M_station:
        charge_location[c] += 1

    # cnt: 충전한 횟수
    cnt = 0

    # position: 현재 버스가 위치해 있는 번호
    position = 0

    # 버스의 현재 위치 + 충전횟수가 목적지보다 크면 반복문 끝
    while (position + K) < N:
        
        # 현재 위치에서 K만큼 떨어진 위치부터 현재 위치까지 역순으로 반복
        # 반대로하면 가까운 위치에서 충전을 해버릴 수 있음음
        # 문제가 최소한 몇 번 충전이기에, 가장 먼 충전소에서만 충전을 해야함
       for k in range(position+K, position, -1):
           
           # 해당 위치에 충전소가 있으면
           # 충전 횟수 +1
           # 위치는 해당 위치로 변경
           # 가장 먼 충전소를 찾았으니 현재 반복문 탈출
            if charge_location[k] == 1:
                cnt += 1
                position = k
                break
        # for문에서 충전소를 하나도 못 찾았다면, cnt = 0으로 하고 반복문 탈출
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')
```