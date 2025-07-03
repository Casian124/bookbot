def count_words(text):
    split_word = text.split()
    counted_words = len(split_word)
    print(f"{counted_words} words found in the document")
    return counted_words

def count_chars(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char]+= 1
        else:
            counts[char]= 1
    return counts

def sort_char_counts(char_counts):
    char_list = [{"char": c, "num": n} for c, n in char_counts.items()]
    
    char_list.sort(key=lambda x: x["num"], reverse = True)

    return char_list
