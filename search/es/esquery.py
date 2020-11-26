"""
elasticsearch

"""

from elasticsearch import Elasticsearch

es = Elasticsearch()


def search_douban(query: str):
    dsl = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["name", "genre", "country", "director", "describe"]
            }
        },
        "highlight": {
            "boundary_scanner_locale":"zh_CN",
            "boundary_scanner":"sentence",
            "pre_tags": ["<mark>"],
            "post_tags": ["</mark>"],
            "fields": {
                "name": {},
                "genre": {},
                "country": {},
                "director": {},
                "describe": {}
            }
        }
    }

    result = es.search(index='douban', docvalue_fields=['movies'], body=dsl, size=20)
    return result
