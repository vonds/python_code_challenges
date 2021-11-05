# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144

def first_non_consecutive(arr):
    if not arr: return 0
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]

# def first_non_consecutive(arr):
#     i = 1
#     for x in arr:
#         if i < len(arr) and arr[i] - arr[i-1] != 1:
#             return arr[i]
#         i += 1
#     return None