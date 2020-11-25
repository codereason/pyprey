# coding=utf-8
import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")
import sys

sys.path.append('')
from crawler.spiderData import search_info
from search.es.esquery import search_douban
# from ranking import *
from loggers import build_timed_logger


@app.get("/", response_class=HTMLResponse)
def hello_world(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})


@app.get('/search/')
async def search(request: Request):
    query = request.query_params['wd'] or ""
    print(query)
    if query == "":
        '''
        不搜索展示默认页
        默认页展示最新最热数据
        '''
        return templates.TemplateResponse('search.html', {"request": request})
    result = search_douban(query)
    hits = result['hits']['hits']
    # print(result)
    for i in range(len(hits)):
        if hits[i].get('highlight'):
            hl = hits[i].get('highlight')
            hl_keys = hl.keys()
            for key in list(hl_keys):
                hits[i]['_source'][key] = hl[key][0]
    print(hits)

    # rerank
    # vectorization ann matching
    # candids = 
    # rank = 
    # rank_results = 
    return templates.TemplateResponse('search.html', {"request": request, "data": hits, "num": len(hits)})
    # return {"1":request.query_params['wd']}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True, reload=True)
