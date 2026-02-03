def counting_sort(input_arr, k):
    temp = [0] * len(input_arr)
    counts = [0] * (k + 1)
    for i in range(len(input_arr)):
        counts[input_arr[i]] += 1
    for i in range(1, k + 1):
        counts[i] += counts[i-1]
    for i in range(len(input_arr) - 1, -1, -1):
        counts[input_arr[i]] -= 1
        temp[counts[input_arr[i]]] = input_arr[i]
        
    return temp

arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))