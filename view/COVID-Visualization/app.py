from flask import Flask, render_template, jsonify

from config import *
import database_utils.get_data as get_data

app = Flask(__name__)


@app.route('/')
def handle():
    return render_template('main.html')


@app.route("/c2")
def c2_handle():
    res = []
    for tup in get_data.get_c2_data():#需要一个参数（热搜名）
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({'data': res})


@app.route("/r1")
def r1_handle():
    data = get_data.get_r1_data()#需要两个参数(热搜名，地址）
    return 0


@app.route('/r2')
def r2_handle():
    data = get_data.get_r2_data()#需要一个参数(社交平台)
    return 0


if __name__ == "__main__":
    # 网页缓存会阻碍debug => 使用随机端口
    import random
    # app.run(host=HOST,
            # port=PORT + int(random.random() * random.random() * 10000))
    app.run(host=HOST,port=8848)
