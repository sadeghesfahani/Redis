def linear_search(list_of_objects, number_of_objects, value_we_are_looking_for):
    for i in range(0, number_of_objects):
        if list_of_objects[i] == value_we_are_looking_for:
            return i
    return -1


array = [24, 41, 31, 11, 9]
x = 11
n = len(array)
result = linear_search(array, n, x)
if result == -1:
    print("Element not found")
else:
    print("Element is Present at Index: ", result)


def binary_search(list_of_objects, value_we_are_looking_for, low, high):
    while low <= high:

        mid = low + (high - low) // 2

        if list_of_objects[mid] == value_we_are_looking_for:
            return mid

        elif list_of_objects[mid] < value_we_are_looking_for:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [2, 4, 5, 17, 14, 7, 11, 22]
x = 22

result = binary_search(array, x, 0, len(array) - 1)

if result != -1:
    print(str(result))
else:
    print("Not found")
