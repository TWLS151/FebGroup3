# 16504 SWEA Gravity
# 요구사항 정리 -> 입력받은 리스트에서 첫 인덱스의 숫자와 해당 숫자 제외 제일 큰 숫자 개수에 따른 낙차 구하기
# 아이디어 -> 인덱스[0] 미만의 숫자 개수 구하기 => 답
# 문제 채점 테스트 인풋에 반례 상황이 없는 것으로 판단됨 -> 직접 만든 반례 케이스 대응 코드 추가 작성

T = int(input())

for test in range(T):
    N = int(input())                # 가로길이
    blocks_num = list(map(int, input().split()))    # 각 칸마다 블록의 수 리스트로 정리
    max_output = 0
    for i in range(N):
        current_block = blocks_num[i]
        count_num=0
        for j in range(i+1, N):
            if blocks_num[j] < current_block:
                count_num += 1
        if count_num > max_output:
            max_output = count_num
    print(f'#{test+1}', end=' ')
    print(max_output)