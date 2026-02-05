import sys 
sys.stdin = open('01.txt')
# 테스트 개수 입력
T = int(input())
# 테스트 개수만큼 순환
for tc in range(1,T+1) :
    #양수 개수 입력
    n = int(input())
    #양수 list 생성
    arr = list(map(int,input().split()))
    
    for i in range(n-1) :
        #최대값 인덱스 
        max_idx = i 
        #짝수인 경우
        if i % 2 == 0:
            for j in range(i+1, n) :
                if arr[j] > arr[max_idx] :
                    max_idx = j
        arr[i],arr[max_idx] = arr[max_idx],arr[i]
        #최솟값 인덱스
        min_idx = i 
        #홀수인 경우
        if i % 2 != 0:
            for j in range(i+1,n) :
                if arr[j] < arr[min_idx] :
                    min_idx = j
            arr[i],arr[min_idx] = arr[min_idx],arr[i]
        
    print(arr[:10])
