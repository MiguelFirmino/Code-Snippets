from random import randint

def bubble_sort(nums):
  swapped = True

  while(swapped):
    swapped = False
    for i in range(len(nums) - 1):
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
        swapped = True

  return nums

sample_array = [randint(-10, 10) for i in range(10)]
print(f"Unsorted array: {sample_array}")

sorted_array = bubble_sort(sample_array)
print(f"Sorted array: {sorted_array}")
