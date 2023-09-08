def sequential_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i  
    return -1  
arr = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
target = int(input("Enter the number you want to search for: "))
index = sequential_search(arr, target)

if index != -1:
    print(f"{target} found at index {index}")
else:
    print(f"{target} not found in the list")
