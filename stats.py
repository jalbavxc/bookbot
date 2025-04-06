def get_num_words():
    filepath = "bookbot/books/frankenstein.txt"
    num_words=len(get_book_text(filepath.split()))
    print(f"{num_words} words found in the document")