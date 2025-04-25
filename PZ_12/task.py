
# def unique_in_order(arr):
#     if not arr: return []
#
#     result = [arr[0]]
#     i = 1
#     while i < len(arr):
#         if arr[i] != result[-1]:
#             result.append(arr[i])
#         i += 1
#     return result

from functools import reduce

def unique_in_order(arr):
    return reduce(lambda accum, x: accum + [x] if not accum or accum[-1] != x else accum, arr, [])


print(unique_in_order(['A1', 'A2', 'A3', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B']))
print(unique_in_order("AAAAAABBBBBBCCCCAAA"))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order((1, 2, 2, 3, 3)))