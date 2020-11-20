from flask import Flask,  render_template
from spiderData import search_info
from flask import request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def hello_world():
    return render_template('/index.html')


@app.route('/search',methods=["POST","GET"])
def search():
    keyword = request.args.get('wd')
    print(keyword)
    result = search_info(keyword)
    # print(result)
    return render_template('/index.html',data = result,num = len(result))



if __name__ == '__main__':
    app.run(debug=True)
