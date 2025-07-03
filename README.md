# BookBot - Text Analysis Tool

A simple Python tool that analyzes any text file to show word counts and character frequencies. Perfect for studying literature or exploring writing patterns.

! What It Does

- Counts total words in your text
- Shows which letters appear most frequently  
- Displays everything in a clean, readable format

! Quick Start

1. **Get some books** - Download free text files from [Project Gutenberg](https://www.gutenberg.org/)
2. **Put them in a `books/` folder**
3. **Run the script**:

python3 main.py books/frankenstein.txt


 Sample Output


============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...

----------- Word Count ----------
Found 75,767 total words

--------- Character Count -------
e: 44,538
t: 29,493
a: 25,894
...

============= END ===============


! How It Works

- **main.py** - Handles input and displays results
- **stats.py** - Does the actual counting and sorting

! Try Different Books


python3 main.py books/mobydick.txt
python3 main.py books/prideandprejudice.txt


Compare how different authors use language!

! Requirements

- Python 3.x
- No external libraries needed
