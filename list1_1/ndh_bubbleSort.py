# 버블 정렬을 파이썬으로
def bubble_sort(bubble_list, N):            # 정렬할 List, N 원소 수
    for i in range(N-1, 0, -1):             # 범위의 끝 위치
        for j in range(i) :                 # 비교할 왼쪽 원소 인덱스 j 
            if bubble_list[j] > bubble_list[j+1] :
                bubble_list[j], bubble_list[j+1] = bubble_list[j+1], bubble_list[j]

bubble_list = [9, 8, 3, 6, 1, 3, 5, 7]      # 정렬 전 bubble_list
bubble_sort(bubble_list, 8)
bubble_list                                 # 정렬 후 bubble_list