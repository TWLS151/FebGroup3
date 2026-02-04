import sys
sys.stdin = open('연습문제1_in.txt')

#테스트 수 입력
T = int(input())
# 테스트 개수만큼 순환
for tc in range(1, T+1) :
    #행의 수 입력
    N = int(input())
    #행렬 생성
    arr = [list(map(int, input().split())) for _ in range(N)]
    #열의 수 생성
    M = len(arr[0])
    # 각 요소별 절댓값의 합을 담을 list 생성
    sum_list = []
    #행렬 요소 순환
    for i in range(N) :
        for j in range(M) :
            # 요소별 절댓값 합 초기값
            s = 0
            # 요소의 기준 위치 
            r, c  = i , j

            #4방향의 델타 정의
            dr = [-1,1,0,0]
            dc = [0,0,-1,1]
            
            # 기준점 기준 변화한 위치 
            for k in range(len(dr)) :
                nr = r + dr[k]
                nc = c + dc[k]

                #경계 체크
                if 0 <= nr < N and 0 <= nc < M :
                    # 절댓값 체크
                    abs_n = arr[nr][nc] - arr[r][c]
                    if abs_n < 0 :
                        abs_n = -(abs_n)
                    #기준점인 요소의 절댓값 합
                    s += abs_n
            #모든 요소의 절댓값 list
            sum_list.append(s)
    # 모든 요소의 절댓값 총합 출력
    print(f'#{tc} {sum(sum_list)}')
                
                
