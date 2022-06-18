from flask import request
from flask import Flask, render_template, jsonify
from flask import url_for
from flask import redirect
from config import *
import database_utils.get_data as get_data
from deal.out import bprint as out
from deal.data import bprint_data

app = Flask(__name__)

deals = [out,bprint_data]
for deal in deals:
    app.register_blueprint(deal)

@app.route('/', methods=['GET','POST'])
def handle():
    if request.method == "GET":
        return render_template('main.html')
    if request.method =="POST":
        addr = request.form.get("saddr")
        if addr == "词云图":
            return redirect(url_for('picturehtml'))
        elif addr!=None:
            data = get_data.get_comments(addr)
            return render_template('search.html', data=data)
        else:
            return redirect(url_for('paperhtml'))

@app.route("/c2",methods=['GET'])
def c2_handle():
    if request.method=="GET":
        hot_point = request.args.get("params")
        data = get_data.get_c2_data(hot_point)
        res = []
        for tup in data:
            res.append({"name": tup[0], "value": int(tup[1])})
        return jsonify({'data': res})
    else:
        return "error"

@app.route("/r1")
def r1_handle():
    data = get_data.get_r1_data()#需要两个参数(热搜名，地址）
    return data


@app.route('/r2')
def r2_handle():
    res = get_data.get_r2_data()#需要一个参数(社交平台)
    data = [['hotPoint', 'num']]
    for i in res:
        data.append([i[0],i[1]])
    print(data)
    return jsonify({"data":data})

@app.route('/paper')
def paperhtml():
    return render_template('papers_vis.html')

@app.route('/picture')
def picturehtml():
    return render_template('picture.html')

if __name__ == "__main__":
    # 网页缓存会阻碍debug => 使用随机端口
    import random
    # app.run(host=HOST,
            # port=PORT + int(random.random() * random.random() * 10000))
    app.run(host=HOST,port=8848)
