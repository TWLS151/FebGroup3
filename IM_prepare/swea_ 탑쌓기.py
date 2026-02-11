import sys
sys.stdin = open('06.txt')
#테스트 개수 입력
T = int(input())
#테스트 수만큼 순환
for tc in range(1, T+1) :
    #화물, 탑 높이 입력
    n, w1, w2 = map(int, input().split())
    #화물 무게 내림차순 정렬
    k = sorted(list(map(int, input().split())), reverse = True)
    #모든 탑의 층 오름차순 정렬
    w = sorted(list(range(1,w1+1)) + list(range(1,w2+1)))

    #총 비용 초기값
    s = 0

    #모든 탑의 층 수만큼 순환하며 총 비용 계산
    for i in range(len(w)) :
        s += k[i] * w[i]

    #값 출력
    print(f'#{tc} {s}')

















