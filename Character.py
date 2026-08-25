word=input("Enter your word here ")
letter=input("Enter your character here:")
i=0
count=0
while i<len(word):
    if word[i]==letter:
        count=count+1
    i=i+1
else:
    print(letter, "does not appear in", word ,".")
exit()
print("The number of times", letter ,"appeared in", word ,"Is", count ,".")