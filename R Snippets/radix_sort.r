radix_sort <- function(nums) {
  highest_num <- max(nums)
  highest_pos <- nchar(highest_num)

  buckets <- list()

  # create bucket dict
  for (key in 0:9) {
    buckets[[as.character(key)]] <- vector()
  }

  helper <- nums

  for (position in 1:highest_pos) {
    # fill buckets
    for (number in helper) {
      # get the index starting from the right of the number
      index <- nchar(number) - position + 1
      char <- substr(number, index, index)

      if (index <= 0) {
        buckets[["0"]] <- append(buckets[["0"]], number)
      } else {
        buckets[[char]] <- append(buckets[[char]], number)
      }
    }

    # reset helper vector
    helper <- vector()

    # empty buckets
    for (key in names(buckets)) {
      helper <- append(helper, buckets[[key]])
      buckets[[key]] <- vector()
    }
  }

  return (helper)
}

sample_array <- sample(0:50, 25, replace=TRUE)
cat("Unsorted Array:", sample_array, "\n")

sorted_array <- radix_sort(sample_array)
cat("Sorted Array:  ", sorted_array, "\n")
