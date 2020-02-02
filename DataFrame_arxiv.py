import pandas as pd
from sklearn.utils import shuffle

#loading data to a data frame and storing it in a csv file (comma separated values)
cat = ['astro-ph.GA','math.DG','quant-ph','stat.ML','cs.CL','q-bio.NC']
lot = [] #list of tuples
for c in cat:
    for i in range(1,5001):
        f = open("/home/simona/PycharmProjects/PRACTICA/modified_" + c + "/art_{0}.txt".format(i), "r")
        text = f.read()
        f.close()
        lot.append((text,c))
df = pd.DataFrame(lot, columns = ["Keywords","Category"], index = list(range(1,len(lot) + 1)))
df = shuffle(df)
print(df.head(10))
export_csv = df.to_csv (r"/home/simona/PycharmProjects/PRACTICA/export_dataframe.csv",index = None,header = True)
