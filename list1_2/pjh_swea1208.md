# SWEA 1208. [S/W 문제해결 기본] 1일차 - Flatten

## 코드 방향성 / 구상한 내용
정렬과 최댓값 그리고 최솟값 반복

## 어려웠던 점
1. 난이도에 비해서 생각보다 쉬웠음

```python
import sys

sys.stdin = open('1208.txt')


for tc in range(1, 11):

    # 덤프 횟수
    times = int(input())

    # 상자의 높이 값들을 리스트로 받음
    box_height = list(map(int, input().split()))

    # 상자 높이 리스트를 정렬
    box_height.sort()

    # times 횟수 만큼 반복
    # box_height의 마지막 인덱스(최댓값)을 -1
    # box_height의 1번 인덱스(최솟값)을 +1
    # 최댓값과 최솟값을 조정할 때마다, box_height를 재정렬
    for x in range(times):
        box_height[-1] -= 1
        box_height[0] += 1
        box_height.sort()

    print(f'#{tc} {box_height[-1] - box_height[0]}')

```