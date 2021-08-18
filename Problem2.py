def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return binary_search_recursive_soln(input_list, number, 0, len(input_list) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index
    if array[start_index] <= mid_element:
        if array[start_index] <= target < mid_element:
            return binary_search_recursive_soln(array, target, start_index, mid_index - 1)
        else:
            return binary_search_recursive_soln(array, target, mid_index + 1, end_index)
    else:
        if mid_element < target <= array[end_index]:
            return binary_search_recursive_soln(array, target, mid_index + 1, end_index)
        else:
            return binary_search_recursive_soln(array, target, start_index, mid_index - 1)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(input_list, number):
    output = rotated_array_search(input_list, number)
    solution = linear_search(input_list, number)

    print(output)
    if solution == output:
        print("Pass\n")
    else:
        print("Fail\n")


print("[Edge Case]")
test_function([6, 1],  1)
# 1

print("[Edge Case]")
test_function([1],     0)
# -1

print("[Edge Case]")
test_function([],      1)
# -1

test_function([6, 7, 8, 9, 10, 1, 2, 3, 4],    6)
# 0

test_function([6, 7, 8, 9, 10, 1, 2, 3, 4],    1)
# 5

test_function([6, 7, 8, 1, 2, 3, 4],           8)
# 2

test_function([6, 7, 8, 1, 2, 3, 4],           1)
# 3

test_function([6, 7, 8, 1, 2, 3, 4],          10)
# -1
