# 1966 SWEA 숫자를 정렬하자
# 오늘 배운 selection 정렬로 문제를 풀어보자
# 파이썬 내장함수 사용 금지

T = int(input())

for test in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    for i in range(N-1):
        min_idx = i
        for j in range(i + 1, N):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    print(f'#{test+1}', end=' ')
    print(*numbers)