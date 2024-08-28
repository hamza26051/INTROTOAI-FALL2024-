word=input("enter a word")

length=len(word)

if(word[length-1]=='a' or word[length-1]=='e' or word[length-1]=='i' or word[length-1]=='o' or word[length-1]=='u'):
    print("it is a vowel")
else:
    print("it is a consonant")