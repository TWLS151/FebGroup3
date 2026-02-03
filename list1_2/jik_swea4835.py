import sys
sys.stdin = open('sample_input.txt')
# 테스트 케이스 입력
T = int(input())

for tc in range(1, T+1) :
    #정수 및 구간 개수 입력
    N, M = map(int, input().split()) 
    # N개의 정수 list 
    arr = list(map(int, input().split()))
    # 구간합들의 list 생성
    sum_list = []
    # 구간합의 첫번째 수가 될 수 있는 수까지 순환
    for i in range(N - M + 1) :
        sum = 0
        # 구간합 첫번째 수부터 구간 범위까지의 순환
        for k in range(i, i+M) :
            sum += arr[k] 
        sum_list.append(sum)
    # 출력
    print(f'#{tc} {max(sum_list)-min(sum_list)}')



