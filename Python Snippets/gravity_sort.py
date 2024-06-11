from random import randint

def gravity_sort(nums):
  sorted_nums = [float("-inf")] # temporary negative infinity

  for unsorted_number in nums:
    for index, sorted_number in enumerate(sorted_nums):
      if unsorted_number >= sorted_number:
        sorted_nums.insert(index, unsorted_number)
        break

  sorted_nums.pop() # remove the negative infinity

  return sorted_nums

sample_array = [randint(-10, 10) for i in range(10)]
print(f"Unsorted array: {sample_array}")

sorted_array = gravity_sort(sample_array)
print(f"Sorted array: {sorted_array}")
