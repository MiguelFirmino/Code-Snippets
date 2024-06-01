from random import randint

def merge_sort(nums):
  if len(nums) <= 1:
    return nums

  mid = len(nums) // 2

  left = merge_sort(nums[:mid])
  right = merge_sort(nums[mid:])

  return merge(left, right)

def merge(left, right):
  merged_array = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged_array.append(left[i])
      i += 1
    else:
      merged_array.append(right[j])
      j += 1

  merged_array += left[i:]
  merged_array += right[j:]

  return merged_array

unsorted_array = [randint(-10, 10) for i in range(10)]
print(f"Unsorted Array = {unsorted_array}")
print(f"Sorted Array = {merge_sort(unsorted_array)}")