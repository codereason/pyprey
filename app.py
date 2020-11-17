from flask import Flask,  render_template
from spiderData import search_info
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('/index.html')


@app.route('/search')
def search():
    keyword = request.args.get('wd')
    print(keyword)
    result = search_info(keyword)
    print(result)
    return render_template('/result.html',data = result,num = len(result))



if __name__ == '__main__':
    app.run()
