import jieba
import collections
import json
import psycopg2
def  getdata():
    #创建连接对象
    conn=psycopg2.connect(database="weiboComments",user="postgres",password="247rgzrc",host="localhost",port="5432")
    cur=conn.cursor() #创建游标对象
    cur.execute('SELECT comment_user_content FROM comments where length(comment_user_content) > 25' )
    results=cur.fetchall()  #获取所有数据
    x = []
    for row  in results:
         x.append(row[0])    #row[1]每行的第1项数据 姓名  下标从0开始的 0是序号

    x = ''.join(x)
    ls = jieba.lcut(x)
    newls = []
    for i in ls:
        if len(i)>1:
            newls.append(i)

    #统计词频
    counts = collections.Counter(newls) 
    picList = []
    for cou in counts.most_common(800):
        projeRes_dict = {}
        projeRes_dict["name"] = cou[0]
        projeRes_dict["value"] = cou[1]
        picList.append(projeRes_dict)

    with open('../data/picList.json','w', encoding='utf8') as fp:
        json.dump(picList,fp,ensure_ascii=False)

    print(picList)
    # print(counts.most_common(10)[0],counts.most_common(10)[1])      
    # print(counts.most_common(1000))
    conn.commit()
    cur.close()
    conn.close()

getdata()

