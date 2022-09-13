word=input("Enter a String\t")
Word=word.upper()
revWord=""
i=len(word)-1
while i>=0:
    revWord=revWord+Word[i]
    i-=1
if revWord==Word:
    print("Entered String is a palindrome")
else:
    print("Entered String is not a palindrome")
