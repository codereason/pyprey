import json
# with open('/home/hy/get.json') as json_file:
#     data = json.load(json_file)
# print(data)

import requests as req
init_url = "https://www.zhihu.com/people/lian-shang-tian-kong-lan"

headers ={"User-agent":"Googlebot"}
resp = req.get(init_url,headers=headers)


print(resp.content)