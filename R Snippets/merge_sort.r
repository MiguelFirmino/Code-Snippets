merge_sort <- function(nums) {
  if (length(nums) <= 1) {
    return (nums)
  }

  size <- length(nums)
  mid <- size %/% 2

  left <- merge_sort(nums[1:mid])
  right <- merge_sort(nums[(mid + 1):size])

  return (merge(left, right))
}

merge <- function(left, right) {
  i <- 1
  j <- 1
  merged <- c()

  while (i < length(left) + 1 & j < length(right) + 1) {
    if (left[i] <= right[j]) {
      merged <- append(merged, left[i])
      i <- i + 1
    } else {
      merged <- append(merged, right[j])
      j <- j + 1
    }
  }

  if (i < length(left) + 1) {
    merged <- append(merged, left[i:length(left)])
  }
  if (j < length(right) + 1) {
    merged <- append(merged, right[j:length(right)])
  }

  return (merged)
}

sample_numbers <- sample(-10:10, 10)
sorted_numbers <- merge_sort(sample_numbers)
cat("Unsorted Array =", sample_numbers, "\n")
cat("Sorted Array =", sorted_numbers, "\n")