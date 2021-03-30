import time

def merge(left, right):

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(data):

    if len(data) <= 1: 
        return data

    half = len(data) // 2
    left = merge_sort(data[:half])
    right = merge_sort(data[half:])

    return merge(left, right)


