# 4843 SWEA 특별한 정렬
# 요구사항 정리 -> 입력받은 숫자를 최대값 최소값 그다음 최대값 그다음 최소값 ... 순서로 배치하는 것이 목표
# 파이썬 내장함수 사용 금지

T = int(input())

for test in range(T):
    N = int(input())                               # 입력받을 숫자의 길이
    numbers = list(map(int, input().split()))      # 입력 받은 숫자를 리스트로 담기
    count_numbers = 0
    for n in numbers:
        count_numbers += 1
    # selection 정렬을 활용한 리스트 정렬을 진행합니다.
    for i in range(count_numbers-1):
        min_idx = i
        for j in range(i+1, count_numbers):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    # 리스트 인덱싱을 통해서 요구사항대로 숫자 재배치 진행합니다.
    # n -> 0, 0 -> 1, n-1 -> 2, 1 -> 3, n-2 -> 4, 2 -> 5 ...
    # 규칙성 정리 => 마지막 순서 숫자들 짝수 인덱스(0 포함), 첫 숫자들 홀수 인덱스
    # 입력된 숫자의 길이가 홀수인 경우 정중앙 숫자가 마지막에 배치된다. 따라서 count_numbers 짝수 홀수 여부에 따라 분류
    output = [0]*count_numbers
    half_numbers_start = numbers[:count_numbers // 2]
    half_numbers_last = numbers[count_numbers // 2:][::-1]
    middle = numbers[count_numbers // 2]
    if count_numbers%2!=0:
        half_numbers_last = numbers[count_numbers//2+1:][::-1]
        output[count_numbers//2] = middle
    for x in range(count_numbers // 2):
        output[x * 2] = half_numbers_last[x]
    for y in range(count_numbers // 2):
        output[y * 2 + 1] = half_numbers_start[y]

    print(f'#{test+1}', end=' ')
    print(*output[:10])