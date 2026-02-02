def bubbleSort(L:list):
    if len(L) == 1:
        return L
    else:
        length = len(L)
        for i in range(length-1):
            if L[i] > L[i+1]: #큰게 뒤로 가게 정렬
                L[i],L[i+1] = L[i+1],L[i]
        return bubbleSort(L[:-1]) + [L[-1]]
    

A = [34,5,7,9,5,3,6,89,4]
print(bubbleSort(A))
