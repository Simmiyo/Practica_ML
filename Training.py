import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score
import pickle

#splitting into training and testing sets
'''df = pd.read_csv("/home/simona/PycharmProjects/PRACTICA/export_dataframe_new.csv")
print(df.head())
x = list(df["Keywords"])
y = list(df["Category"])
print(x)
print(y)'''
#x = x.array.reshape(-1, 1)
f = open("/home/simona/PycharmProjects/PRACTICA/vectorizer.pk","rb")
x = pickle.load(f)
f.close()
f = open("/home/simona/PycharmProjects/PRACTICA/encoder.pk","rb")
y = pickle.load(f)
f.close()
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)
#print(x_train.shape)
#y_train.shape()

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

#notice that SVM method returns the most accurate classifier
message = input("Would you like to save this classifier?[y/n] ")
if message is "y":
    with open("/home/simona/PycharmProjects/PRACTICA/classifier.pk","wb") as f:
        pickle.dump(training,f)