# reverse a string
n=str(input("Enter a string ="))
print("Reverse =",n[::-1])


# check palindrome 
n=str(input("Enter a string ="))
if n==n[::-1]:
    print("String in palindrome")
else:
    print("String is not palindrome")
print("====================")

# vowels and consonants
s=str(input("Enter a string ="))
vowels="aeiouAEIOU"
v_counts=sum(1 for char in s if char in vowels)
c_counts=sum(1 for char in s if char.isalpha() and char not in vowels)
print(f"Vowels ={v_counts} and Consonants ={c_counts}")
print("=====================")


# frequency of each character in a string
from collections import Counter 
string=str(input("Enter a string ="))
freq =Counter(string)
print("Frequency of each char =",dict(freq))
print("==================")


# remove duplicate from a string
s=str(input("Enter a string ="))
new="".join(dict.fromkeys(s))
print(new)
print("====================")


# count a word in a string
sentence =str(input("Enter a sentence ="))
word_count=len(sentence.split())
print("Words Count =",word_count)
print("==================")

# longest word in a sentence
sentence =str(input("Enter a sentence ="))
word=sentence.split()
longest=max(word,key=len)
print("Longest word is =",longest)
print("================")


# Uppercase,Lowercase,Digits aur Special Characters Count

s=str(input("Enter a sentence ="))

upper=sum(1 for c in s if c.isupper())
lower=sum(1 for c in s if c.islower())
digits=sum(1 for c in s if c.isdigit())
special=sum(1 for c in s if not c.isalnum() and not c.isspace())

print(f"Lower ={lower} ,Upper ={upper} ,Digits ={digits} ,Special ={special}")
print("================")


# check anagrams
def is_anagram(str1,str2):
    return sorted(str1.lower().replace(" ","")) ==sorted(str2.lower().replace(" ",""))
print(is_anagram("listen","silent"))
print("======================")


# reversed of python is easy
s="python is easy"
reversed_sentence=" ".join(s.split()[::-1])
print(reversed_sentence)