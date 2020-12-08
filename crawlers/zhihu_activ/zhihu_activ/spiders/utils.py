import json
'''utils class for text and json processing in zhihu feed.'''
def get_id_and_action_from_actions_feed(act):
    res = {}
    for key in act:
        article_id = act[key].get("target")["id"]
        action = act[key]['actionText']
        createdTime = act[key]['createdTime']
        res[key] = {"article_id":article_id,"action":action,"createdTime":createdTime}
    return res

def join_action_feed_with_articles():
    pass




