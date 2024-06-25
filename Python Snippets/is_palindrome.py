def is_palindrome(text):
  '''
  Given a text, define if it's a palidrome or not
  '''
  text = text.lower() # remove case sensitivity
  text = "".join(i for i in text if i.isalnum()) # filter non-alphanumeric chars

  left = 0
  right = len(text) - 1

  while left < right:
    if text[left] != text[right]:
      return False
    left += 1
    right -= 1

  return True

answer = lambda x: f'The text "{x}" is {"a" if is_palindrome(x) else "not a"} palindrome'

print(answer("ovo"))
print(answer("arara"))
print(answer("giant alligator"))
