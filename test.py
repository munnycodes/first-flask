print("Hello world")
print("This is a test, please work for the love of goodness.")
def capitalise_first_word(sentence):
    sentence = sentence.split()
    sentence[0] = sentence[0].upper()
    sentence = " ".join(sentence)
    return (sentence)

print(capitalise_first_word("hello everybody good people"))

