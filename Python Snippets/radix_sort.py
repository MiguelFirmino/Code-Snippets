def radix_sort(nums):
  highest_number = max(nums)
  highest_position = len(str(highest_number))

  buckets = {"0" : [], "1" : [], "2" : [],
             "3" : [], "4" : [], "5" : [],
             "6" : [], "7" : [], "8" : [],
             "9" : []}

  for position in range(1, highest_position + 1):
    helper = []

    for number in nums:
      number_string = str(number)

      if len(number_string) < position:
        buckets["0"].append(number)
      else:
        buckets[number_string[-position]].append(number)

    for bucket in buckets:
      helper += buckets[bucket] # Fill helper array
      buckets[bucket] = [] # Emptying buckets

    nums = helper

  return nums

sample_array = [randint(0, 100) for i in range(20)]
print(f"Unsorted array: {sample_array}")

sorted_array = radix_sort(sample_array)
print(f"Sorted array: {sorted_array}")
