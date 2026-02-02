def bubble_sort(arr):
    # list 마지막 index 부터 순환
    for k in range(len(arr) - 1, 0 ,-1) :
        for j in range(k):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
        
    
numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)