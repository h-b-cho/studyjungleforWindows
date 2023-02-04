from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://test:test@52.78.173.17',27017)
db = client.exam

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=['POST'])
def post_article():
    title_receive = request.form['title_give']
    text_receive = request.form['text_give']

    article = {'title': title_receive, 'comment': text_receive}
    
    db.hbmemo.insert_one(article)

    return jsonify({'result': 'success'})

@app.route('/memo', methods=['GET'])
def read_articles():
    result = list(db.hbmemo.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'articles': result})

@app.route('/update', methods=['POST'])
def edit_memo():
    title_receive = request.form['title_give']
    mod_title_receive = request.form['mod_title_give']
    mod_text_receive = request.form['mod_text_give']
    
    db.hbmemo.update_one({'title': title_receive}, {'$set': {'title': mod_title_receive , 'comment': mod_text_receive}})

    return jsonify({'result': 'success'})

@app.route('/delete', methods=['POST'])
def del_memo():
    title_receive = request.form['title_give']
    db.hbmemo.delete_one({'title': title_receive})
    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)