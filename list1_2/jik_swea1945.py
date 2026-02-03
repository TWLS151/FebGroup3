import sys
sys.stdin = open('sample_input2.txt')
# 테스트 케이스 입력
T = int(input())


for tc in range(1, T+1) :
    # 양수 개수 입력
    N = int(input())
    
    # 초기값 입력
    a = b = c =d = e = 0
    
    
    while N % 2 == 0 :
        N = N // 2 
        a = a + 1
        
    while N % 3 == 0 :
        N = N // 3 
        b = b + 1
        

    while N % 5 == 0 :
        N = N // 5
        c = c + 1
        
    while N % 7 == 0 :
        N = N // 7 
        d = d + 1
        

    while N % 11 == 0 :
        N = N // 11 
        e = e + 1
        
    #출력
    print(f'#{tc} {a} {b} {c} {d} {e}')