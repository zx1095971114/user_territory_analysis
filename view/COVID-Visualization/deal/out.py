from flask import Blueprint, jsonify
import glob
import json

bprint = Blueprint("", __name__, template_folder="templates")

rel_papers = {}
uid_filter = {}
def main(rel_papers_path):
    extra_files = []
    for f in glob.glob(rel_papers_path + "/*"):
        extra_files.append(f)
        name, typ = f.split("/")[-1].split(".")
        if typ == "json":
            name = name.split("\\")[-1]
            rel_papers[name] = json.load(open(f,encoding='utf-8'))

    
    uid_filter["origin_papers"] = {}
    for paper_id, p in rel_papers["origin_papers"].items():
        uid_filter["origin_papers"][paper_id] = p

    
    bprint.rel_papers = rel_papers
    bprint.uid_filter = uid_filter

    return extra_files


def extract_list_field(v, key):
    value = v.get(key, "")
    if isinstance(value, list):
        return value
    if value.find("|") != -1:
        return value.split("|")
    else:
        return value.split(",")

def format_paper(v):
    list_keys = ["authors"]
    list_fields = {}
    for key in list_keys:
        list_fields[key] = extract_list_field(v, key)

    return {
        "id": v["uid"],
        "title": v["title"],
        "authors": list_fields["authors"],
        "UID": v["uid"],
        "location": v["location"],
        "hotPoint": v["abstract"] 
    }


@bprint.route("/origin_papers.json")
def paper_json():
    json = []
    for v in rel_papers["origin_papers"].items():
        json.append(format_paper(v[1]))
    return jsonify(json)


@bprint.route("/proje_papers.json")
def save():
    return jsonify(rel_papers["proje_papers"])

# @bprint.route("/picList.json")
# def words():
#     return jsonify(rel_papers["picList"])

rel_papers_path = "data"
extra_files = main(rel_papers_path)
