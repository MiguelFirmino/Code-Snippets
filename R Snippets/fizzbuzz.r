fizzbuzz = function(n) {
  message <- ""

  for (number in 0:n) {
    if (number %% 15 == 0) {
      print("FizzBuzz") # if divisible by 3 AND 5
    } else if (number %% 3 == 0) {
      print("Fizz") # if divisible by 3
    } else if (number  %% 5 == 0) {
      print("Buzz") # if divisible by 5
    } else {
      print(number) # if divisible by none
    }
  }
}

fizzbuzz(100)
