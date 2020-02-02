import numpy
import scipy
import pandas as pd
import sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import pickle

#extracting data from csv file to a data frame
df = pd.read_csv("/home/simona/PycharmProjects/PRACTICA/export_dataframe.csv")
#print(df.tail(10))
#print(df['Category'].unique())

#converting categories into numbers
le = LabelEncoder()
df["Category"] = le.fit_transform(df["Category"])
inv = le.inverse_transform([0,1,2,3,4,5])
with open("/home/simona/PycharmProjects/PRACTICA/encoder_inverse.pk","wb") as f:
    pickle.dump(inv,f)

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
            tfidf = tfidf.fit(df["Keywords"])
            with open("/home/simona/PycharmProjects/PRACTICA/vectorizer_fit.pk", "wb") as f:
                pickle.dump(tfidf, f)
            x = tfidf.transform(df["Keywords"]).toarray()
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
x = converter(n)
y = df["Category"]
with open("/home/simona/PycharmProjects/PRACTICA/vectorizer.pk","wb") as f:
    pickle.dump(x,f)
f.close()
with open("/home/simona/PycharmProjects/PRACTICA/encoder.pk","wb") as f:
    pickle.dump(y,f)
f.close()
#export_csv_new = df.to_csv (r"/home/simona/PycharmProjects/PRACTICA/export_dataframe_new.csv",index = None,header = True)