def word_count(book_content):
  return len(book_content)


def letter_count_dictionary(book_content):
  letter_count = {}
  for letter in book_content:
    if letter.isalpha():
      letter = letter.lower()
      if letter in letter_count:
        letter_count[letter] += 1
      else:
        letter_count[letter] = 1
  return letter_count

def letter_list(letter_count_dictionary):
  list = []
  for letter in letter_count_dictionary:
    dictionary = {
      "char": letter,
      "count": letter_count_dictionary[letter]
    }
    list.append(dictionary)
  return list

def sort_on(items):
  return items["count"]

def counter(sorted_list):
  dict = {}
  for item in sorted_list:
    dict[item["char"]] = item["count"]
  return dict
