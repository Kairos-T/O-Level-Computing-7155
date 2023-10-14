letters = ["a", "e", "i", "o", "u"]
vowel_index = [0, 0, 0, 0, 0]
count = 0

word = input("Enter a word of phrase: ")
for char in word:
    if char in letters:
        index = letters.index(char)
        vowel_index[index] = vowel_index[index] + 1
        count += 1

print(vowel_index)

#print("There are {} letter 'a''s in the word/phrase".format(count))