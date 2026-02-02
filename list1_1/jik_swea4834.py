import sys

sys.stdin = open('02.txt')
# 테스트 케이스 개수
T = int(input())


for tc in range(1, T+1) :
    #N개의 숫자의 각 개수 입력할 list 생성
    arr_count = []
    # 카드 장수 개수
    N = int(input())
    # N개의 숫자 
    arr = list(input())
    # N개의 숫자 내림차순 정렬
    arr.sort(reverse= True)
   
   # N개의 카드 숫자의 장 수 계산
    for i in range(len(arr)) :
        value = arr.count(arr[i])
        arr_count.append(value)
    
    # 가장 많은 카드 숫자와 장 수 초기값
    max_v = arr[0]
    max_count = arr_count[0]

    for k in range(len(arr_count)) :
        if max_count < arr_count[k] :
            max_count = arr_count[k]
            max_v = arr[k]

    # 값 출력
    print(f'#{tc} {max_v} {max_count}')
    
