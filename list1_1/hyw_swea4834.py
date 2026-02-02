T = int(input())

for i in range(T):
    N = int(input())
    decks = input()
    cards = {}
    for j in range(N):
        if cards.get(int(decks[j])):
            cards[int(decks[j])] += 1
        else:
            cards[int(decks[j])] = 1
    print(f'#{i+1} {sorted(cards.items(), key=lambda x: (x[1], x[0] ),reverse=True)[0][0]} {sorted(cards.items(), key=lambda x: (x[1], x[0] ),reverse=True)[0][1]}')