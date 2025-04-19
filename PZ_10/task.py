
# array = [19, 5, 42, 2, 77]
test_array = [10, 343445353, 3453445, 3453545353453]

def solve(array: list[int]):
    first_min = min(array)
    array.remove(first_min)
    second_min = min(array)
    return first_min + second_min

print(solve(array=test_array))
