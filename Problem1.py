def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    arr = list(range(1, number + 1))
    return sqrt_recur(arr, number)


def sqrt_recur(arr, number):
    size = len(arr)
    if size == 0 and number == -1:
        return 'i'
    elif size == 0:
        return 0
    elif size == 1:
        return arr[0]

    cur = size // 2
    product = arr[cur] * arr[cur]

    if product == number:
        return arr[cur]
    elif product > number:
        # recur on first half of remaining array, not including pivot
        if size == 2:
            return arr[0]
        return sqrt_recur(arr[:cur], number)
    else:  # product < number
        # recur on last half of remaining array, including pivot
        if size == 2:
            return arr[1]
        return sqrt_recur(arr[cur:], number)


def test_function(solution, input):
    output = sqrt(input)

    print(output)
    if solution == output:
        print("Pass\n")
    else:
        print("Fail\n")


print("[Edge Case]")
test_function(0, 0)
# 0

print("[Edge Case]")
test_function('i', -1)
# i

# Remaining Test Cases
test_function(4, 16)
# 4

test_function(3, 9)
# 3

test_function(5, 27)
# 5

test_function(6, 38)
# 6
