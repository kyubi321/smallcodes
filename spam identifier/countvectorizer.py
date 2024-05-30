from sklearn.feature_extraction.text import CountVectorizer
document = ["One Geek helps Two Geeks",
"Two Geeks help Four Geeks",
"Each Geek helps many other Geeks at GeeksforGeeks"]
cv = CountVectorizer()
cv.fit(document)
print(f'vocabulary: {cv.vocabulary_}')
vector = cv.transform(document).toarray()
print(f': {vector}')


