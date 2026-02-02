N = int(input())

for i in range(N):
    _ = int(input())
    L = list(map(int,input().split()))
    print(f'#{i+1} {max(L)-min(L)}')