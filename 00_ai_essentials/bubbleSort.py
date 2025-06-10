from typing import List
from collections import Counter

def is_permutation(a: List[int], b: List[int]) -> bool:
    return Counter(a) == Counter(b)

def is_sorted_non_decreasing(arr: List[int]) -> bool:
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bubble_sort(input_list: List[int]) -> List[int]:
    output = input_list.copy()
    n = len(output)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if output[j] > output[j + 1]:
                output[j], output[j + 1] = output[j + 1], output[j]

    # Post-condition checks based on Z-spec
    assert len(input_list) == len(output), "Length mismatch after sorting"
    assert is_permutation(input_list, output), "Output is not a permutation of input"
    assert is_sorted_non_decreasing(output), "Output is not sorted in non-decreasing order"

    return output

if __name__ == "__main__":
    user_input = input("Enter a list of integers separated by spaces: ")
    try:
        values = list(map(int, user_input.strip().split()))
        sorted_values = bubble_sort(values)
        print("Sorted output:", sorted_values)
    except ValueError:
        print("Invalid input. Please enter integers only.")
