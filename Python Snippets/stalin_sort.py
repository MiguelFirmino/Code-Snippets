from random import randint

def stalin_sort(nums):
  sorted_array = []
  highest = float("-inf")

  for number in nums:
    if number >= highest:
      highest = number
      sorted_array.append(number)

  return sorted_array

sample_array = [randint(0, 100) for i in range(20)]
print(f"Unsorted array: {sample_array}")

sorted_array = stalin_sort(sample_array)
print(f"Sorted array: {sorted_array}")
