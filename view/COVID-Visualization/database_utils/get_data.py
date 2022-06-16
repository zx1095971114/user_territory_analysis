#本文件用于实现数据库连接，并搜索数据
import psycopg2
# 返回各省数据

def get_c2_data(hot_point):
    conn = psycopg2.connect(database='weiboComments', user="postgres", password="247rgzrc", host="localhost",
                            port="5432")
    cur = conn.cursor()
    if(hot_point=="all"):
        cur.execute("select comment_user_location ,count(distinct comment_user_content) AS nums from comments group by comment_user_location;")
        results = cur.fetchall()
        results.sort(key=lambda x: x[1], reverse=True)
        return results
    else:
        cur.execute(
            'select comment_user_location ,count(distinct comment_user_content) AS nums from comments where hot_point_name=\'{0}\' group by comment_user_location;'.format(hot_point))
        results = cur.fetchall()
        results.sort(key=lambda x: x[1], reverse=True)
        return results
# 返回某地区的发言
def get_comments(addr):
    conn = psycopg2.connect(database='weiboComments', user="postgres", password="247rgzrc", host="localhost",
                            port="5432")
    cur = conn.cursor()
    cur.execute(
        'select distinct comment_user_content from comments where comment_user_location = \'{0}\';'.format(addr))
    results = cur.fetchall()
    return results

# 返回10条热搜
def get_r2_data():
    conn = psycopg2.connect(database='weiboComments', user="postgres", password="247rgzrc", host="localhost",
                            port="5432")
    cur = conn.cursor()
    cur.execute("select hot_point_name ,count(distinct comment_user_content) AS nums from comments group by hot_point_name;")
    results = cur.fetchall()
    results.sort(key=lambda x:x[1],reverse=False)
    return results
