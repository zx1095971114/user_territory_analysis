from flask import Blueprint, jsonify
import glob
import json

bprint_data = Blueprint("html", __name__, template_folder="templates", url_prefix="/data")

@bprint_data.route("/words.json")
def words():
    with open('data/words.json','r',encoding='utf8') as fp:
        json_data = json.load(fp)
    return jsonify(json_data)

