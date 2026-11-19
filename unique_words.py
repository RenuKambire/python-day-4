def unique_words(sentence):
    words = sentence.split()
    unique_words = set(words)
    return unique_words


sentence = input("Enter a sentence: ")

result = unique_words(sentence)

print("Unique words:", result)