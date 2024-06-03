def filterNumbers(text):
  filteredText = list(filter(lambda x: x.isnumeric() == True, text))

  return "".join(filteredText)

def maskText(text, mask):
  textList = [i for i in text]
  textList = mask(textList, len(text))

  return "".join(textList)

def dateMask(textList, textLength):
  textList.insert(2, "-") if textLength > 2 else 0
  textList.insert(5, "-") if textLength > 4 else 0

  return textList

def hourMask(textList, textLength):
  textList.insert(2, ":") if textLength > 2 else 0

  return textList

def cpfMask(textList, textLength):
  textList.insert(3, ".") if textLength > 3 else 0
  textList.insert(7, ".") if textLength > 6 else 0
  textList.insert(11, "-") if textLength > 9 else 0

  return textList

def phoneMask(textList, textLength):
  textList.insert(0, "(") if textLength > 1 else 0
  textList.insert(3, ") ") if textLength > 2 else 0
  textList.insert(8, "-") if textLength > 6 else 0
  if textLength > 10:
    textList.pop(8)
    textList.insert(9, "-")

  return textList
