T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = input().strip()   # 숫자를 문자열로 입력 받기 (예: "49679")

    counts = [0] * 10   # 0~9까지 숫자 등장 횟수 저장

    # 숫자를 한 자리씩 순회
    for n in nums:
        digit = int(n)  # 문자 → 숫자 변환
        counts[digit] += 1  # 해당 숫자의 등장 횟수 증가

        # 가장 많이 나온 숫자와 그 횟수 찾기
        max_count = 0
        max_digit = 0

    for i in range(10):
        if counts[i] >= max_count:
            max_count = counts[i]
            max_digit = i

    # 결과 출력
    print(f'#{t} {max_digit} {max_count}')