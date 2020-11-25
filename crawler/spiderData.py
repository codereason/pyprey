# coding:utf-8

import requests
import re
import json
import urllib
from lxml import etree
from flask import render_template


def search_info(keyword):
    results_list = []
    # 这里可以研究得出关键是后面变化的关键词
    url = 'https://www.baidu.com/s?word={}'.format(keyword)
    # print '----------------{}'.format(url)
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400',
        'cookie':'BAIDUID=9EA61EA9B50B8588E37DBEEA5F5AADB6:FG=1; BIDUPSID=9EA61EA9B50B8588E37DBEEA5F5AADB6; PSTM=1579917402; BD_UPN=12314753; BDUSS=lBLNEdtMUQ2VGVyMnYzU2I0NkpiMkpaQlo1SFNrODFWSmJnLXVCWkRqUjJ1UVZmSVFBQUFBJCQAAAAAAAAAAAEAAADI0zgFtdpfwflfuNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHYs3l52LN5eV; H_PS_PSSID=; H_PS_645EC=5c0b%2FNMmpW1MFdhWHti%2BEMIhUi2rq%2Bt8O0TJQFUh5WpbGuzm%2B2nx0adIsqd2yrfggp38xw; BDSVRTM=121; BDORZ=FFFB88E999055A3F8A630C64834BD6D0',

    }

    response = requests.get(url,headers = headers)
    response.encoding = 'utf-8'
    #打印出得到的结果
    # print(response.text)
    source = etree.HTML(response.text)
    results =  source.xpath('//*[@id]/@data-tools')
    for r in results:
        try:
            # 这里需要对 xpath取取的结果进行转码：<type 'lxml.etree._ElementUnicodeResult'> 转成str
            # 然后再把字符串转换成json，再取值
            str = json.loads(r.encode('utf-8'))
            results_list.append(str)
            # print str['title'],str['url']
        except Exception as e:
            continue
    return results_list

if __name__ == "__main__":
    print(search_info("你好"))
    from flask import jsonify

    # print(jsonify(search_info("12")))