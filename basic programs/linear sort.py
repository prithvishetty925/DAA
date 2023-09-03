def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    
    count = [0] * (max_val - min_val + 1)
    for num in arr:
        count[num - min_val] += 1
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i + min_val] * count[i])
    
    return sorted_arr

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Sorted array:", sorted_arr)
