


text = open("list.txt","r")
#print(text.read())
text1=""


for word in text.read().split():
        #print(word)
        text1=text1 + "<learn>" + word + "</learn>" + "\n"


print(text1)

text.close()
