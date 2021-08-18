def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return -1
    min, max = ints[0], ints[0]

    for element in ints:
        if min > element:
            min = element
        elif max < element:
            max = element

    return min, max

    print(min, max)


def test_function(input):
    import random

    random.shuffle(input)
    output = get_min_max(input)

    print(output)
    if not input:
        if output == -1:
            print("Pass\n")
        else:
            print("Fail\n")
    elif output == (min(input), max(input)):
        print("Pass\n")
    else:
        print("Fail\n")


print("[Edge Case]")
input = [i for i in range(0, 1)]  # a list containing 0
test_function(input)
# (0, 0)

print("[Edge Case]")
input = []  # an empty list
test_function(input)
# -1

## Example Test Cases of Ten Integers
input = [i for i in range(0, 10)]  # a list containing 0 - 9
test_function(input)
# (0,9)

input = [i for i in range(20, 30)]  # a list containing 20 - 29
test_function(input)
# (20, 29)
