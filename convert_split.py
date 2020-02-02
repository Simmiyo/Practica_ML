import numpy
import scipy
import pandas as pd
import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import sklearn.model_selection
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score

#extracting data from csv file to a data frame
df = pd.read_csv("/home/simona/PycharmProjects/PRACTICA/export_dataframe.csv")
#print(df.tail(10))
#print(df['Category'].unique())

#converting categories into numbers
le = LabelEncoder()

#print(df.head(10))
#print(df['Category'].unique())

#converting keywords into numbers
def converter(n):
    try:
        if n is 1:
            vect = CountVectorizer(max_features = 2000, min_df = 5, max_df = 0.7)
            x = vect.fit_transform(df["Keywords"]).toarray()
            # print(df.head(10))
            # print(df.tail(10))
            tfidf = TfidfTransformer()
            x = tfidf.fit_transform(x).toarray()
            return x
        elif n is 2:
            tfidf = TfidfVectorizer(max_features = 2000, min_df = 5, max_df = 0.7)
            x = tfidf.fit_transform(df["Keywords"]).toarray()
            return x
        else:
            raise ValueError
    except ValueError:
        n = int(input("Press 1 or 2! "))
        converter(n)

print("Converting Methods:")
print("1 = Bag of Words")
print("2 = TFIDF")
n = int(input("Choose the convertion method: "))
x_train, x_test, y_train, y_test = train_test_split(converter(n),le.fit_transform(df["Category"],test_size = 1000,random_state = 0)
#print(df.head(10))
#print(df.tail(10))

#export_csv_new = df.to_csv (r"/home/simona/PycharmProjects/PRACTICA/export_dataframe_new.csv",index = None,header = True)

#training the machine
def choose_train(n):
    try:
        if n is "1":
            classifier = RandomForestClassifier(n_estimators = 1000,random_state = 0)
            classifier.fit(x_train, y_train)
            return classifier
        elif n is "2":
            classifier = GaussianNB()
            classifier.fit(x_train, y_train)
            return classifier
        elif n is "3":
            classifier = SVC(kernel='linear')
            classifier.fit(x_train, y_train)
            return classifier
        elif n is "4":
            classifier = LogisticRegression()
            classifier.fit(x_train, y_train)
            return classifier
        else:
            raise ValueError
    except ValueError:
        n = input("Press one of the following numbers: 1, 2, 3, 4! ")
        return choose_train(n)

print("Classification Models:")
print("1 = Random Forest")
print("2 = Naive Bayer")
print("3 = SVM")
print("4 = Logistic Regression")
n = input("Choose the classification model: ")
training = choose_train(n)
y_guess = training.predict(x_test)
print(confusion_matrix(y_test,y_guess))
print(classification_report(y_test,y_guess))
print(accuracy_score(y_test,y_guess))