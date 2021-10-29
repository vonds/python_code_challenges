# https://www.codewars.com/kata/576bb71bbbcf0951d5000044
def count_positives_sum_negatives(arr):
    if not arr: return []
    count = 0
    sum = 0
    for num in arr:
        if num > 0:
            count += 1
        else:
            sum += num
    return [count, sum]