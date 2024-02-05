def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

input_str = input()
reversed_sentence = reverse_words(input_str)
print(reversed_sentence) 