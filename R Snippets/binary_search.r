binary_search <- function(nums, target) {
    low <- 0
    high <- length(nums)

    while (low <= high) {
        mid <- (low + high) %/% 2

        if (nums[mid] == target) {
            return(mid)
        } else if (nums[mid] < target) {
            low <- mid + 1
        } else {
            high <- mid - 1
        }
    }

    return(-1)
}

sample_vector <- c(1, 2, 5, 10, 12, 13, 16, 19, 20)
print(binary_search(sample_vector, 13))