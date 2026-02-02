for i in range(10):
    N = int(input())
    L = list(map(int,input().split()))
    hap = 0
    for j in range(2,N-2,1):
        #돌면서 빈자리 찾기
        window = max(L[j-2],L[j-1],L[j+1],L[j+2])
        if L[j] > window:
            hap += (L[j] - window)
    print(f'#{i+1} {hap}')