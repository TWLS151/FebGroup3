T = int(input())
# 테스트 케이스 수 만큼 반복
for i in range(T):
    N = int(input())
    # 카드 덱 입력
    decks = input()
    # 카드 개수를 세기 위한 딕셔너리
    cards = {}
    for j in range(N):
        # 카드 덱의 각 카드를 확인
        if cards.get(int(decks[j])):
            # 이미 딕셔너리에 있으면 개수 1 증가
            cards[int(decks[j])] += 1
        else:
            # 딕셔너리에 없으면 개수 1로 초기화
            cards[int(decks[j])] = 1
    # 카드 개수로 정렬, 개수가 같으면 카드 숫자로 정렬
    answer = sorted(cards.items(), key=lambda x: (x[1], x[0] ),reverse=True)[0]
    print(f'#{i+1} {answer[0]} {answer[1]}')