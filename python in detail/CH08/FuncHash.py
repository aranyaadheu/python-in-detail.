def find_pair(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return[seen[target - num], i]
        seen[num] = i
print(find_pair([2, 7, 11], 9))