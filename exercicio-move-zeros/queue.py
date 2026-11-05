from collections import deque

def set_zeros_to_end(arr: list[int]) -> list[int]:
    queue = deque()

    zero_counter = 0
    for i in arr:
        if i != 0:
            queue.append(i)
            continue
        zero_counter += 1

    i = 0
    while queue:
        arr[i] = queue.popleft()
        i += 1

    for i in range(len(arr) - zero_counter, len(arr)):
        arr[i] = 0

    return arr

nums = [0, 1, 0, 3, 12]
set_zeros_to_end(nums)
print(nums)