from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    reverse_list_value: List[int] = []
    for i in range(len(arr) - 1, -1, -1):
        reverse_list_value.append(arr[i])

    return reverse_list_value


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
