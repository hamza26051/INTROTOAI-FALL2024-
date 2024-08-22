word= input("enter a word")
newword=''
for i in range (len(word)):
    newword+=word[len(word)-1-i]

print(newword)