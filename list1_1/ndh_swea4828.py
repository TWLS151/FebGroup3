# SWEA 4828 - min max

# 테스트 번호를 입력받습니다.
T = int(input())

for i in range(T):
		# 첫 줄에 주어질 양수 N개의 값을 입력받습니다.
    N = input()
    # N개의 양수 입력을 리스트로 받습니다.
    a = list(map(int ,input().split()))
    # 최댓값과 최솟값을 보기 위해서 정렬합니다.
    a.sort()
    # 리스트 인덱싱을 통해서 최댓값에서 최솟값을 뺍니다.
    s = int(a[-1])-int(a[0])
    if len(range(int(N)))==len(a):
        print(f'#{i+1}', end=' ')
        print(s)    
