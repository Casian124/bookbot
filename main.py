import sys
from stats import count_words
from stats import count_chars
from stats import sort_char_counts

def get_book_text(filepath):
    with open(filepath, 'r' ) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) !=2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]


    text = get_book_text(book_path)
    counts_w = count_words(text)
    counts_c = count_chars(text)
    counts_s = sort_char_counts(counts_c)
     
    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {counts_w} total words
--------- Character Count -------
""")


    for item in counts_s:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    
    print("============= END ===============")

    return counts_w, counts_c , counts_s

if __name__ == "__main__":
    main()


