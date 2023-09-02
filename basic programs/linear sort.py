def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
my_list = [4, 2, 7, 1, 9, 5]
target_value = 7

result = linear_search(my_list, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}.")
else:
    print(f"Element {target_value} not found in the list.")
