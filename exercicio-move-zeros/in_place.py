def set_zeros_to_end(arr: list[int]) -> list[int]:
    position = 0
    for i in arr:
        if i != 0:
            arr[position] = i
            position += 1

    for i in range(position, len(arr)):
        arr[i] = 0

    return arr
    

nums = [0, 1, 0, 3, 12]
set_zeros_to_end(nums)
print(nums)