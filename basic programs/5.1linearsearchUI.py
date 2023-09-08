def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

arr = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
target = int(input("Enter the number you want to search for: "))
index = linear_search(arr, target)

if index != -1:
    print(f"{target} found at index {index}")
else:
    print(f"{target} not found in the list")
