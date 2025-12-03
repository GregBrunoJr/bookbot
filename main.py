import sys
from stats import (
  get_num_words,
  get_chars_dict,
  chars_dict_to_sorted_list
)

def main():

  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]

  content = get_book_text(book_path)
  wordCount = get_num_words(content)
  letterDicts = get_chars_dict(content)
  letterList = chars_dict_to_sorted_list(letterDicts)
  print_report(book_path,wordCount,letterList)

def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()

def print_report(book_path, wordCount, letterList):

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")

  print("----------- Word Count ----------")
  print(f"Found {wordCount} total words")

  print("--------- Character Count -------")
  for item in letterList:
    char = item["char"]
    count = item["count"]
    print(f"{char}: {count}")


main()
