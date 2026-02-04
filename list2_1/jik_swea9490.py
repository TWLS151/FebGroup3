import sys
sys.stdin = open('03.txt')

#테스트 개수 입력
T = int(input())

#테스트 수만큼 순환
for tc in range(1, T+1) :
    #행과 열 개수 입력
    N, M = map(int, input().split())
    #행렬 생성
    arr = [list(map(int, input().split())) for _ in range(N)]
    #각 요소별 꽃가루 개수 담을 list 생성
    sum_list = []
    #각 요소 순환
    for i in range(N) :
        for j in range(M) :
            #요소의 꽃가루 합 초기값
            s = arr[i][j]
            # 요소의 기준 위치 
            r, c  = i , j

            #4방향의 델타 정의
            dr = [0] * (arr[i][j]) * 2
            
            for a in range(-arr[i][j], arr[i][j]+1) :
                if a != 0 :
                    dr.append(a)

            dc = dr[::-1]
            
            
            
            # 기준점 기준 변화한 위치 
            for k in range(len(dr)) :
                nr = r + dr[k]
                nc = c + dc[k]

                #경계 체크
                if 0 <= nr < N and 0 <= nc < M :
                    s += arr[nr][nc]
                    

            sum_list.append(s)
    #값 출력
    print(f'#{tc} {max(sum_list)}')
                