def get_num_words(contents):
  words = contents.split()
  return len(words)

def sort_on(items):
    return items["count"]

def get_chars_dict(words):
  letterCount = {}
  for letter in words:
    if letter.isalpha():
      letter = letter.lower()
      if letter in letterCount:
        letterCount[letter] += 1
      else:
        letterCount[letter] = 1
    else:
      pass
  return letterCount

def chars_dict_to_sorted_list(num_chars_dict):
  sorted_list = []
  for letter in num_chars_dict:
   count = num_chars_dict[letter]

   sorted_list.append({"char": letter, "count": count})

  sorted_list.sort(reverse=True,key=sort_on)

  return sorted_list
