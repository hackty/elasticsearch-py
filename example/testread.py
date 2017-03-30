# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch
from elasticsearch.addon.settings import es_host

es = Elasticsearch(es_host,
                   sniff_on_start=True,
                   sniff_on_connection_fail=True,
                   sniffer_timeout=60)

index = "bdoctestindex"
type = "bdoctesttype"


keyword = "aaaaa"

body = {
            "query":{
                "bool":{
                    "should":[
                        {"match":{"url":keyword}},
                        {"match":{"title":keyword}},
                        {"match":{"content":keyword}},
                    ]
                }
            }
        }

result = es.search(index, type, body)

count = result["hits"]["total"]

print "keyword:" + keyword
print "count:" + str(count)

for row in result["hits"]["hits"]:
    print row