word = input("Enter a word: ")
letterCount = len(word)
vowelCount = word.count("A")+word.count("a")+word.count("E")+word.count("e")+word.count("I")+word.count("i")+word.count("O")+word.count("o")+word.count("U")+word.count("u")
vowelPct =  (vowelCount / letterCount)*100

print(f"Letter: {letterCount}")
print(f"Vowels: {vowelCount}")
print(f"Percentage of vowels: {vowelPct}")
