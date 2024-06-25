def product_except_index(nums):
  '''
  Given an array of integers 'nums', return
  a list containing the product of all items
  except the item at it's index
  '''
  result = [1] * len(nums)

  left_result = 1
  for index in range(len(nums)):
    result[index] = left_result
    left_result *= nums[index]

  right_result = 1
  for index in range(len(nums)-1, -1, -1):
    result[index] *= right_result
    right_result *= nums[index]

  return result

sample_numbers = [2, 3, 4, 6]
print(f"Sample: {sample_numbers}")

products = product_except_index(sample_numbers)
print(f"Result: {products}")
