from flask import Flask,  render_template, jsonify, request
from flask_cors import CORS

from crawler.spiderData import search_info
from search.es.esquery import search_douban
from ranking. import *
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
    '''

    '''
    query = request.args.get('wd') or ""
    print(query)
    if query == "":
        '''
        不搜索展示默认页
        默认页展示最新最热数据
        '''
        return render_template('/index.html')
    result = search_douban(query)
    # print(result)
    # print(jsonify(result))
    # return jsonify(result)
    # print(len(result))
    hits =  result['hits']['hits']
    # print(result)
    for i in range(len(hits)):
        if hits[i].get('highlight'):
            hl = hits[i].get('highlight')
            hl_keys = hl.keys()
            for key in list(hl_keys):
                hits[i]['_source'][key] = hl[key][0]
    print(hits)
    
    #rerank

    return render_template('/search.html',data = hits,num = len(hits))



if __name__ == '__main__':
    app.run(debug=True)
