def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two numbers such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    n = len(input_list)

    # Build a max-heap - O(n)
    for i in range(n, -1, -1):
        heapify(input_list, n, i)

    # One by one extract elements - O(n) -- O(n log n) including heapify
    for i in range(n - 1, 0, -1):
        input_list[i], input_list[0] = input_list[0], input_list[i]  # swap
        heapify(input_list, i, 0)  # worst case: O(log n)

    return create_numbers(input_list)


def heapify(arr, n, i):
    # Using i as the index of the current node, find the 2 child nodes (if the array were a binary tree)
    # and find the largest value.   If one of the children is larger swap the values and recurse into that subtree

    # consider current index as largest
    largest_index = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    # compare with left child
    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    # compare with right child
    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    # if either of left / right child is the largest node
    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]

        heapify(arr, n, largest_index)


def create_numbers(input_list):
    first, second = 0, 0
    n = len(input_list)

    for i in range(n - 1, -1, -1):  # O(n)
        if i % 2 == 0:
            first = first * 10 + input_list[i]
        else:
            second = second * 10 + input_list[i]

    return first, second


def test_function(input, solution):
    output = rearrange_digits(input)

    print(output)
    if sum(output) == sum(solution):
        print("Pass\n")
    else:
        print("Fail\n")


print("[Edge Case]")
test_function([1, 0],    [1, 0])
# (0, 1)

print("[Edge Case]")
test_function([0, 0],    [0, 0])
# (0, 0)

test_function([1, 2, 3, 4, 5],    [542,  31])
# (531, 42)

test_function([4, 6, 2, 5, 9, 8], [964, 852])
# (964, 852)
