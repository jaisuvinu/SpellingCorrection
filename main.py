from textblob import TextBlob
def Convert (string):
    li = list(string.split())
    return li
str1 = input("Enter words to check spelling : ")
words = Convert(str1)
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Word to be corrected :", words)
print("Corrected words are : ")
for i in corrected_words:
    print(i.correct(), end=" ")

