def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    cur, next_index_0 = 0, 0
    next_index_2 = len(input_list) - 1

    while cur <= next_index_2:
        if input_list[cur] == 0:
            input_list[next_index_0], input_list[cur] = 0, input_list[next_index_0]
            next_index_0 += 1
            cur += 1
        elif input_list[cur] == 2:
            input_list[next_index_2], input_list[cur] = 2, input_list[next_index_2]
            next_index_2 -= 1
        else:  # input_list[cur] == 1
            cur += 1

    return input_list


def test_function(input):
    sorted_array = sort_012(input)

    print(sorted_array)
    if sorted_array == sorted(input):
        print("Pass\n")
    else:
        print("Fail\n")


print("[Edge Case]")
test_function([2, 1, 0])
# [0, 1, 2]

print("[Edge Case]")
test_function([])
# []

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
