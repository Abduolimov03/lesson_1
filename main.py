def count_positives_sum_negatives(arr):
    if arr is None or len(arr) == 0:
        return []

    count_positive = 0
    sum_negative = 0

    for num in arr:
        if num > 0:
            count_positive += 1
        elif num < 0:
            sum_negative += num

    return [count_positive, sum_negative]


input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
natija = count_positives_sum_negatives(input_array)
print(natija)