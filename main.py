import sys
from stats import (
  word_count,
  letter_count_dictionary,
  letter_list,
  sort_on,
  counter
)

usage = "Usage: python3 main.py <path_to_book>"

if len(sys.argv) != 2:
  print(usage)
  sys.exit(1)
else:
  try:
    open(sys.argv[1])
  except FileNotFoundError:
    print(usage)
    print(f"{sys.argv[1]} not found. Please please provide a valid file path!")
    sys.exit(1)
  except:
    print("Something went wrong")
    sys.exit(1)

  path = sys.argv[1]

def get_book_text(book):
  with open(book) as f:
    return f.read()

def main(book_path):
  book_contents = get_book_text(book_path)
  words_count = word_count(book_contents)
  letter_dictionary = letter_count_dictionary(book_contents)
  letters_list = letter_list(letter_dictionary)
  sorted_dictionary = counter(letters_list)

  letters_list.sort(reverse=True, key=sort_on)

  message(book_path, words_count, sorted_dictionary)

def message(book_path, words_count, sorted_dictionary):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}")
  print("----------- Word Count ----------")
  print(f"There are {words_count} words in {book_path}")
  print("--------- Character Count -------")
  for item in sorted_dictionary:
    print(item, sorted_dictionary[item])
  print("============= END ===============")
  

main(path)
