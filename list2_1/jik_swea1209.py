import sys
sys.stdin = open('04.txt')
# 테스트 개수
T = 10

#테스트 개수만큼 순환
for tc in range(1, T+1) :
    N = int(input())
    #행렬 생성
    arr = [list(map(int, input().split())) for _ in range(100)]
    #대각선의 합 초기값
    c=d=0
    #각 행과 열의 합 담을 list 생성
    sum_a= []
    sum_b= []
  
    #행, 열, 대각선 합 계산
    for i in range(100) :
        a = b = 0
        c += arr[i][i]
        d += arr[i][99-i] 

        for j in range(100):
            a += arr[i][j]
            b += arr[j][i]
        sum_a.append(a)
        sum_b.append(b)

    #행과 열의 최댓값 
    a = max(sum_a)
    b = max(sum_b)
    
    #출력
    print(f'#{N} {max(a,b,c,d)}')



    
        