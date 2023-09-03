def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i  
    return -1  

my_list = [4, 2, 7, 1, 9, 5]
n=int(input("enter the element:"))

result = linear_search(my_list, n)

if result != -1:
    print(f"Element found at index",result)
else:
    print(f"Element not found in the list.")
