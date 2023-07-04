#Sorting any word in alphabetical order
word = input("Enter a word")
word = word.split(' ')[0]
word.lower()
word = list(word)
for i in range(len(word)):
    for j in range(len(word[i-1:])-1):
        n1 = ord(word[j])
        n2 = ord(word[j+1])
        if n1<=n2:
            temp=n1
            n1=n2
            n2=temp
        word[j]=chr(n2)
        word[j+1]=chr(n1)
print("After sorting:\t",word)
