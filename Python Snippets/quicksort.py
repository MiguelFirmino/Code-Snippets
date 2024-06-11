from random import randint

def quick_sort(nums):
  if len(nums) <= 1:
    return nums

  pivot = nums[len(nums) // 2]
  left = []
  middle = []
  right = []

  for number in nums:
    if number < pivot:
      left.append(number)
    elif number > pivot:
      right.append(number)
    else:
      middle.append(number)

  return quick_sort(left) + middle + quick_sort(right)

sample_array = [randint(-10, 10) for i in range(10)]
print(f"Unsorted array: {sample_array}")

sorted_array = quick_sort(sample_array)
print(f"Sorted array: {sorted_array}")
