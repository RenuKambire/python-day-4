sentence = input("enter a sentence:")
words = sentence.split()
if words:
    longest = words[0]
    for word in words:
        if len(word)> len(longest):
            longest = word
    print("longest word:", longest)
else:
    print("no words entered:")    