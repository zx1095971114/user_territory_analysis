from abc import abstractclassmethod
import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold, datasets
import json
import csv
import collections
import psycopg2
from sklearn.feature_extraction.text import CountVectorizer
 
uids = []
abstract_data = []
uname = []
comment_user_location = []
hot_point_name = []

conn=psycopg2.connect(database="weiboComments",user="postgres",password="247rgzrc",host="localhost",port="5432")
cur=conn.cursor() 
cur.execute('SELECT distinct comment_user_content,comment_user_id,comment_user_name,comment_user_location,hot_point_name FROM comments where length(comment_user_content) > 25' )
results=cur.fetchall()  #获取所有数据
for row in results:
    uids.append(row[1])
    abstract_data.append(row[0])
    uname.append(row[2])
    comment_user_location.append(row[3])
    hot_point_name.append(row[4])
print (results[0])
conn.commit()
cur.close()
conn.close()


print(abstract_data)

# with open('../data/origin_data.csv','r',encoding='utf8') as fp:
#     csv_data = csv.reader(fp)
#     isFirst = True
#     for value in csv_data:
#         if isFirst:
#             isFirst = False
#             continue
#         uids.append(value[0]) 
#         abstract_data.append(value[1])

'''词频统计'''
cv = CountVectorizer(min_df=1, ngram_range=(1,1))
vector = cv.fit_transform(abstract_data)
vector = vector.todense()
# print(vector)
# print(cv.vocabulary_)



'''t-SNE'''
tsne = manifold.TSNE(n_components=2, init='pca', random_state=501)
abstract_tsne = tsne.fit_transform(vector)
print(abstract_tsne)

print("Org data dimension is {}. Embedded data dimension is {}".format(vector.shape[-1], abstract_tsne.shape[-1]))
# res = []
res = {}
projeRes = []
for i in range(abstract_tsne.shape[0]):
    projeRes_dict = {}
    projeRes_dict["id"] = uids[i]
    projeRes_dict["pos"] = abstract_tsne[i].tolist()
    res_dict = {}
    res_dict["uid"] = uids[i]
    res_dict["authors"] = [uname[i]]
    res_dict["location"] = comment_user_location[i]
    res_dict["abstract"] = hot_point_name[i]
    res_dict["title"] = abstract_data[i]
    res[uids[i]] = res_dict
    projeRes.append(projeRes_dict)
        
with open('../data/origin_papers.json','w', encoding='utf8') as fp:
    json.dump(res,fp,ensure_ascii=False)

with open('../data/proje_papers.json','w', encoding='utf8') as fp:
    json.dump(projeRes,fp,ensure_ascii=False)

# '''嵌入空间可视化'''
x_min, x_max = abstract_tsne.min(0), abstract_tsne.max(0)
X_norm = (abstract_tsne - x_min) / (x_max - x_min)  # 归一化
plt.figure(figsize=(8, 8))
for i in range(X_norm.shape[0]):
    plt.plot(X_norm[i][0], X_norm[i][1], 'r.')
plt.xticks([])
plt.yticks([])
plt.show()