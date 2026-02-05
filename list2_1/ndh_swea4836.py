# 4836 SWEA 색칠하기
# matrix_dots 안의 모든 요소 dots를 각각의 좌표가 튜플 형식으로 담긴 리스트로 변환 
# dots의 마지막 숫자가 같으면 리스트 합한다. -> 1로 끝나면 튜플 좌표 요소들 하나의 코드에 담는다.
# ex) [(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(4,4)] + [(6,6)]
# dots의 범위를 구하는 로직은 경계값을 구하는 방식으로 구현

T = int(input())

for t in range(T):
    N = int(input())
    matrix_dots = [list(map(int, input().split())) for _ in range(N)]
    red_dots = []
    blue_dots = []
    purple_cnt = 0

    for dots in matrix_dots:
        r1 = dots[0]
        c1 = dots[1]
        r2 = dots[2]
        c2 = dots[3]
        color = dots[4]

        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                dot = (row, col)

                if color==1:
                    red_dots.append(dot)
                else:
                    blue_dots.append(dot)
    
    for red in red_dots:
        if red in blue_dots:
            purple_cnt += 1

    # print(matrix_dots)
    print(f'#{t+1}', end=' ')
    print(purple_cnt)