import sys
sys.stdin = open('04.txt')
#테스트 개수 입력
T = int(input())
#테스트 수만큼 순환
for tc in range(1, T+1) :
    #학생수, 문항수 입력
    n, m = map(int,(input().split()))
    #답안지
    ans = list(map(int, input().split()))
    #학생들 답안 행렬 생성
    stu = [list(map(int, input().split())) for _ in range(n)]
    #학생별 점수 담을 list 생성
    result = []
    #학생들 답안 순환
    for i in range(n) :
        # 각 학생들의 점수 및 연속 정답 수 초기값
        c = 0
        s = 0

        for j in range(m):
            # 답안지와 학생답 비교 및 총점 계산
            if ans[j] == stu[i][j]:
                c += 1
                s += c
            else :
                c = 0
        # 학생들 점수 모으기
        result.append(s)
    # 출력
    print(f'#{tc} {max(result) - min(result)}')