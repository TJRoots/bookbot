import sys
from stats import count_words, count_characters, sorted_character_count

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
word_count = count_words(sys.argv[1])
character_count = count_characters(sys.argv[1])

print("============ BOOKBOT ============\nAnalyzing book found at "+str(sys.argv[1])+"...\n----------- Word Count ----------")
print("Found " + str(word_count) + " total words")
#print(character_count)
print("--------- Character Count -------")
for char, count in sorted_character_count(sys.argv[1]):
    if char.isalpha():
        print(char + ": " + str(count))
print("============= END ===============")