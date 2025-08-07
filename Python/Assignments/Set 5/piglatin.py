"""
A Pig Latin word is a word that begins with consonant sound; all letters before the initial
   vowel are placed at the end of the word sequence. Then, "ay" is added, as in the following
   examples:  
   "pig" "igpay"
   â€œbanana"  "ananabay"
   "trash" "ashtray"
   Input a word and generate its Pig Latin

"""




#main
word = input("Enter word : ")
piglatin_word = ""
for i in range(len(word)):
    if word[i].upper()=='A' or word[i].upper()=='E' or word[i].upper()=='I' or word[i].upper()=='O' or word[i].upper()=='U':
        piglatin_word+=word[i:]+word[0:i]+"ay"
        break
print("pig-latin : ",piglatin_word)     