def word_generator(text):
    parts = text.split()
    for word in parts:
        yield word

text = "the quick brown fox the lazy dog"
word_counts = {}

for word in word_generator(text):
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

text1 = "the quick brown fox jumps over the lazy dog"
text2 = "the lazy cat sleeps under the warm sun"

word1 = set(word_generator(text1))
word2 = set(word_generator(text2))

common_words = word1 & word2
print(common_words)




    






