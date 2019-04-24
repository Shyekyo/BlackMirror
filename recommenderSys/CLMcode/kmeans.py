#-*-coding-*-
"""
author:xiaofan
"""
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn import metrics

# X = np.array([[1, 2], [1, 4], [1, 0],
#               [10, 2], [10, 4], [10, 0]])
# kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
# print(kmeans.labels_)
path = "../data/ml-100k/u1.base"
#用户对电影的评分 = x
#用户对未来电影的评分 = y
# user_id | item_id | rating | timestamp
x = []
y = []
with open(path,"r") as f:
    for line  in f.readlines():
        #print(line.strip())
        ls = line.strip().split("\t")
        #y = int(ls[2])
        x.append([int(ls[0]),int(ls[1]),int(ls[3])])
        y.append(int(ls[2]))
print(x[0])
print(y[0])
kmeans = KMeans(n_clusters=5, random_state=0).fit(x,y)
df_test = pd.read_csv("../data/ml-100k/u1.test",header=None,sep="\t")
df_test.columns=["u","i","s","t"]
test = df_test[["u","i","t"]]
y_hat = kmeans.predict(test)+1
print(metrics.adjusted_rand_score(df_test["s"],y_hat))
#df = pd.read_csv(path,sep="\t",header=None,index_col=1)
#wf =  open("../data/filename.txt", 'w')
#print(df.loc[0:10])
# for i in set(df.index): #这里使用集合读出不重复的index值
#     nums=df.loc[i, 0].size
#     ItemDegree=nums
#     string = str(i) + "\t" + str(ItemDegree)+"\n"
#     wf.write(string)
# wf.close()
# d =pd.read_csv("../data/filename.txt",sep="\t",header=None)
# print(d[1].mean())
# print(d[1].max())
# print(d[1].min())