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
