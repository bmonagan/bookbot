from stats import get_num_words,letter_count,analyze
def main():
    def get_book_text(filepath):
        with open(filepath) as f:
            file_contents = f.read()
        return file_contents

    current_book = "books/frankenstein.txt"
    book_text = get_book_text(current_book)
    
    # letter_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {current_book}...")
    get_num_words(book_text)
    analyze(book_text)
    print("============= END ===============")



if __name__ == "__main__":
    main()
