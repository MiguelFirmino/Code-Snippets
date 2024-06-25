def longest_substring(string):
  '''
  Given a string, find the length of the
  longest substring in it that has no
  repeating characters
  '''
  longest_sequence = ""
  current_sequence = ""
  viewed_chars = set() # chars that appeared in the current sequence

  for index in range(len(string)):
    char = string[index]

    if char in viewed_chars:
      # reset current sequence
      viewed_chars = set(char)
      current_sequence = char

      # trace back the characters until the repeated
      # character and add them to the current sequence
      left_pos = index - 1
      left_char = string[left_pos]
      while left_char != char and left_pos > 0:
        viewed_chars.add(left_char)
        current_sequence = left_char + current_sequence
        left_pos -= 1
        left_char = string[left_pos]

    else:
      # increment current sequence
      current_sequence += char
      viewed_chars.add(char)

    # register the longest sequence
    if len(current_sequence) > len(longest_sequence):
      longest_sequence = current_sequence

  return longest_sequence

test_string = "abcabdcder"
print(f"String: {test_string}")
 
result = longest_substring(test_string)
print(f"Longest substring: {result}")
