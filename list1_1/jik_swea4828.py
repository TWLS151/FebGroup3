import sys

sys.stdin = open('01.txt')
# 테스트 케이스 수
T = int(input()) 

for tc in range(1, T+1) : 
    #양수의 개수
    N = int(input())  
    #N개의 양수 리스트
    arr = list(map(int, input().split())) 
    #최소, 최대 초기값 
    min_v = max_v = arr[0]  

    for i in range(len(arr)) :
        if max_v < arr[i] :
            max_v = arr[i]
        if min_v > arr[i] :
            min_v = arr[i]
            
    print(f'#{tc} {max_v - min_v}')