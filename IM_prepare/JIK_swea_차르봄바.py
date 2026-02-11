#import sys
#sys.stdin = open('03.txt')

#테스트 수 입력
T = int(input())


#테스트 수만큼 순환
for tc in range(1, T+1) :
    #행과 열 수 입력
    n, m = map(int,(input().split()))
    #행렬 생성
    arr = [list(map(int, input().split())) for _ in range(n)]
    #합들을 담을 list 생성
    sum_list = []

    #행렬 각 요소 순환
    for i in range(n) :
        for j in range(m) :

            #기준 좌표 지정
            r, c = i, j
            #합의 초기값
            s = arr[r][c]

            #4방향 델타
            dr = [-1,1,0,0]
            dc = [0,0,-1,1]

            #기준 좌표 기준 변화하는 좌표 위치
            for h in range(arr[r][c]) :
                for k in range(len(dr)) :
                    nr = r + dr[k] * (h+1)
                    nc = c + dc[k] * (h+1)

                    # 경계값 지정
                    if 0<= nr < n and 0<= nc < m :
                        s += arr[nr][nc]

                # 합들 모으기
                sum_list.append(s)
    #최대값 출력
    print(f'#{tc} {max(sum_list)}')












