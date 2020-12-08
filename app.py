# coding=utf-8
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import configparser
app = FastAPI()
templates = Jinja2Templates(directory="templates")
import sys

sys.path.append('')
from search.es.esquery import search_douban
# from ranking import *
from loggers import build_timed_logger
from conf.config import Config 

@app.get("/", response_class=HTMLResponse)
def hello_world(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})


@app.get('/search/')
async def serve_and_search(request: Request):
    query = request.query_params['wd'] if request.query_params.get('wd') else ""
    print(query)
    if query == "":
        '''
        不搜索展示默认页
        默认页展示最新最热数据
        '''
        return templates.TemplateResponse('search.html', {"request": request, "num": 0})
    result = search_douban(query)
    hits = result['hits']['hits']
    # print(result)
    if hits != []:
        for i in range(len(hits)):
            if hits[i].get('highlight'):
                hl = hits[i].get('highlight')
                hl_keys = hl.keys()
                for key in list(hl_keys):
                    hits[i]['_source'][key] = hl[key][0]
        print(hits)
        print(query)

    # vectorization ann matching
    # candids = 
    # rank = 
    # scoring =
    # rank_results = 
    return templates.TemplateResponse('search.html',
                                      {"request": request, "data": hits, "num": len(hits), "query": query})


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True, reload=True)
