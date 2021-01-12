print("Hello world")
def capitalise_first_word(sentence):
    sentence = sentence.split()
    sentence[0] = sentence[0].upper()
    sentence = " ".join(sentence)
    return (sentence)

