from collections import Counter

words = set()
fileAdress = input("write the .txt file adress : ")
with open(fileAdress, encoding="UTF-8") as text:
    texte = text.read()
    wordsintext = texte.split()
    for word in wordsintext:
        cleanword = "".join(filter(str.isalpha, word))
        if cleanword != "":
            words.add(cleanword.lower())

wordcount = len(words)



# If you want to count the frequency of each word, you can use Counter:
word_frequency = Counter(words)
print("Word frequency:", word_frequency)

print("The text contains", wordcount, "different words.")