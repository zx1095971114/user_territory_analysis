#本文件用于实现数据库连接，并搜索数据
import psycopg2
# 返回各省数据

def get_c2_data():
    return 0

# 返回某地区的发言
def get_r1_data(resou,addr):
    return 0

# 返回10条热搜
def get_r2_data():
    conn = psycopg2.connect(database='weiboComments', user="postgres", password="lrj2000118", host="localhost",
                            port="5432")
    cur = conn.cursor()
    cur.execute("select hot_point_name ,count(comment_user_content) AS nums from comments group by hot_point_name;")
    results = cur.fetchall()
    results.sort(key=lambda x:x[1],reverse=True)
    return results
