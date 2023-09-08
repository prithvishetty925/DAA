my_array = []
for i in range(5):
    try:
        num = int(input(f"Enter integer {i+1}: "))
        my_array.append(num)
    except ValueError:
        print("Invalid input! Please enter an integer.")
print("Array items:")
for i in range(len(my_array)):
    print(f"Element {i}: {my_array[i]}")
