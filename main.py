def get_book_text(pathfile):
    with open(pathfile) as f:
        file_content=f.read()
    return file_content.split()

def main():
    filepath = "bookbot/books/frankenstein.txt"
    num_words=len(get_book_text(filepath))
    print(f"{num_words} words found in the document")

main()