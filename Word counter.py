def checkDouble(array,string):
    word = 0
    for i in array:
        if i == string:
            word +=1
    if word >= 1:
        return True
    else:
        return False
words = []
wordcount = 0
fileAdress = input("write the .txt file adress : ")
with open (fileAdress, encoding="UTF-8") as text:
    texte = text.read()
    wordsintext = texte.split()
    for i in wordsintext:
        cleanword = "".join(filter(str.isalpha, i))
        if checkDouble(words,cleanword.lower()) == False and cleanword != "":
            words.append(cleanword.lower())
for i in words:
    wordcount += 1
words_dict = {}
for n in words:
    words_dicts = {n}
print("The text contain", wordcount, "different words.")