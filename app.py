from flask import Flask,  render_template, jsonify, request
from flask_cors import CORS

from spiderData import search_info
from search.es.esquery import search_douban
app = Flask(__name__)
CORS(app)

import sys
sys.path.append('')

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def hello_world():
    return render_template('/index.html')


@app.route('/search',methods=["POST","GET"])
def search():
    keyword = request.args.get('wd')
    print(keyword)
    result = search_douban(keyword)
    # print(result)
    # print(jsonify(result))
    # return jsonify(result)
    # print(len(result))
    hits =  result['hits']['hits']
    print(result)
    return render_template('/index.html',data = hits,num = len(result))



if __name__ == '__main__':
    app.run(debug=True)
