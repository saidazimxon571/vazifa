n = int(input("Nechta so'z kiritasiz: "))

words = []

for i in range(n):
    word = input()
    words.append(word)

unique_words = set(words)

print(len(unique_words))