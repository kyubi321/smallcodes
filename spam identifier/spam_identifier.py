def spam_identifier(email):
    # importing the necessary packages

    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.naive_bayes import MultinomialNB

    # fetch the data using pandas and group by category and describe it

    data = pd.read_csv('spam.csv')
    # print(data.groupby('Category').describe())

    # now we create a new colum in the data set where we provide a 0 or 1 value to the spam /ham mails
    # for this we use the apply function in pandas and lambda function

    data['identifier'] = data['Category'].apply(lambda x: 1 if x == 'spam' else 0)
    # print(data)

    # now we create train test split
    x_train, x_test, y_train, y_test = train_test_split(data.Message, data.identifier, test_size=0.25)

    # now we need to find the no of words and store it as matrix
    # to do that we use the CountVectorizer

    # creating a countvectorizer object
    cv = CountVectorizer()
    # now we need to count the words
    x_train_count = cv.fit_transform(x_train.values)

    # result = x_train_count.toarray()
    # print(result)

    # now we train the model
    model = MultinomialNB()
    model.fit(x_train_count, y_train)

    # now we test our data
    x_test_count = cv.transform(x_test)
    print(f'The models accuracy is : {model.score(x_test_count, y_test)}')

    obj = [str(email)]
    val = cv.transform(obj)
    x = model.predict(val)
    if x == 0:
        return 0
    else:
        return 1


email = input("enter the mail you want to check : ")
fun_result = spam_identifier(email)
if fun_result == 1:
    print("This is a spam mail")
else:
    print("This is a legit mail")


