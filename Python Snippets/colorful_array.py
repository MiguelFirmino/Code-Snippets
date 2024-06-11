def get_colorful_array(array):
  result = ""

  smallest = min(array)
  highest = max(array)
  mid = (smallest + highest) // 2

  for number in array:
    dist_smallest = abs(number - smallest), "\033[92m"
    dist_mid = abs(number - mid), "\033[93m"
    dist_highest = abs(number - highest), "\033[91m"

    distance, color = min(dist_smallest, dist_mid, dist_highest)

    result += f"{color}{number} {colors.normal}"

  return result
