word = input()
reverse_word = ""
for w in range(len(word)-1, -1, -1):
    reverse_word += word[w]

print(reverse_word)

