def binary_search(nums, target):
  '''
  given an array of numbers and a target
  number, return the targets index
  '''
  low = 0
  high = len(nums) - 1

  while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  return -1

sample_numbers = [10, 5, 3, -4, 15, 2, 1, 15]
index = binary_search(sample_numbers, 0)