import sys
sys.stdin = open('07.txt')
#테스트 개수 입력
T = int(input())
#테스트 수만큼 순환
for tc in range(1, T+1) :
    #방 개수 입력
    n = int(input())
    #i 번째 방 왼쪽에 있는 방 번호 list 생성
    room_l = list(map(int, input().split()))
    #모든 방 번호 list 생성
    room = list(range(1,n+1))

    #i 번째 방 왼쪽 생각 안하고 우선 모든 방 기준 포털 이용해 N번방까지 가는 경우의 수
    c = (len(room)-2) * 3 + 1
    # 포털 이용할 수 있는 구간만 순환
    for i in range(1,len(room)-1) :
        # i 번째 방과 왼쪽 방의 차이 나타내는 변수 생성
        d = room[i]- room_l[i]
        # 차이가 1이 아닌 경우 차이에서 1 제외한 값 누적
        if d != 1 :
            c += d-1
    # 값 출력
    print(f'#{tc} {c}')






















