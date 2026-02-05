import sys 
sys.stdin = open('04.txt')
# 테스트 개수 입력
T = int(input())
# 테스트 개수만큼 순환
for tc in range(1,T+1) :
    #양수 개수 입력
    N, M = map(int, input().split())
    #행렬 생성
    arr = [list(map(int,input().split())) for _ in range(N)]
    #합들을 담을 list 생성
    sum_list=[]
    for i in range(N) :
        for j in range(N) :
            #각 합의 초기값 생성
            sum = sum1 = arr[i][j]
            
            # 요소의 기준 위치 
            r, c  = i , j

            #dr,dc(+), dk,dp(x)
            dr = [-1,1,0,0] 
            dc = [0,0,-1,1]
            dk = [-1,-1,1,1]
            dp = [-1,1,-1,1]

            #M에 따라 변화하는 좌표위치
            for h in range(M-1) :
                for k in range(len(dr)) :
                    nr = r + dr[k]* (h+1)
                    nc = c + dc[k] * (h+1)
                    nk = r + dk[k]* (h+1)
                    np = c + dp[k]* (h+1)

                    #+모양들의 합
                    if 0 <= nr < N and 0 <= nc < N:
                        sum += arr[nr][nc]
                            
                    sum_list.append(sum)
                
                    #x모양들의 합
                    if 0 <= nk < N and 0 <= np < N :
                        sum1 += arr[nk][np]
                    sum_list.append(sum1)
    # 출력
    print(f'#{tc} {max(sum_list)}')
                    
            

    

