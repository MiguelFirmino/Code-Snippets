expression <- function(lhs, rhs, operator) {
  if (operator == "+") {
    return (lhs + rhs)
  } else if (operator == "-") {
    return (lhs - rhs)
  } else if (operator == "*") {
    return (lhs * rhs)
  } else if (operator == "/") {
    return (division_with_test(lhs, rhs))
  }
}

division_with_test <- function(dividend, divisor) {
  if (divisor == 0) {
    return (NA)
  }
  return (dividend / divisor)
}

polish_calc <- function(calc_text) {
  split_text <-  strsplit(calc_text, " ")[[1]]
  lhs <- NULL
  rhs <- NULL
  operator <- NULL
  result <- NULL

  for (char in split_text) {
    if (grepl(char, "+-*/")) {
      # print(paste("The operator is now:", char))
      operator = char
    }

    is_complete = !is.null(lhs) && !is.null(rhs) && !is.null(operator)
    if (is_complete) {
      result = expression(lhs, rhs, operator)
      lhs = result
      rhs = NULL
      operator = NULL
      next
    }

    if (!grepl("[0-9]", char)) {
      # print(paste("Char:", char, "is not numeric."))
      next
    } else if (is.null(lhs)) {
      lhs = as.integer(char)
      # print(paste("The lhs is now:", char))
      next
    } else {
      rhs = as.integer(char)
      # print(paste("The rhs is now:", char))
      next
    }
  }

  return (result)
}

expression_text = "10 10 *"
polish_calc(expression_text)
