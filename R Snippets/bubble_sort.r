bubble_sort <- function(nums) {
  swapped <- TRUE

  while (swapped) {
    swapped <- FALSE

    for (index in 1:(length(nums)-1)) {
      if (nums[index] > nums[index + 1]) {
        temp <- nums[index]
        nums[index] <- nums[index + 1]
        nums[index + 1] <- temp
        swapped <- TRUE
      }
    }
  }

  return (nums)
}

sample_array <- sample(0:50, 25, replace=TRUE)
cat("Unsorted Array:", sample_array, "\n")

sorted_array <- bubble_sort(sample_array)
cat("Sorted Array:  ", sorted_array, "\n")
