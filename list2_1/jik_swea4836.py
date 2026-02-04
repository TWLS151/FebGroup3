import sys
sys.stdin = open('01.txt')

#테스트 수 입력
T = int(input())

#테스트 수만큼 순환
for tc in range(1, T+1) :
    #영역의 수 입력
    N = int(input())
    #영역의 범위 입력
    arr = [list(map(int, input().split())) for _ in range(N)]
    #빨간색, 파란색 좌표 담을 list 생성
    R1 = []
    R2 = []
    #보라색 영역 개수 초기값
    cnt = 0

    #색깔별 모든 좌표 모으기
    for k in range(len(arr)) :
        if arr[k][-1] == 1 :
            for i in range(arr[k][0],arr[k][2]+1) :
                for j in range(arr[k][1], arr[k][3]+1) :

                    a = (i,j)
                    R1.append(a)
    
        else :
            for i in range(arr[k][0],arr[k][2]+1) :
                for j in range(arr[k][1], arr[k][3]+1) :

                    a = (i,j)
                    R2.append(a)

        #중복되는 좌표 제거
        
        c1  = set(R1) & set(R2)
        
    # 값 출력
    print(f'#{tc} {len(c1)}')
        