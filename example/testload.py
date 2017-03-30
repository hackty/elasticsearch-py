# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch
from elasticsearch.addon.settings import es_host

es = Elasticsearch(es_host,
                   sniff_on_start=True,
                   sniff_on_connection_fail=True,
                   sniffer_timeout=60)

index = "bdoctestindex"
type = "bdoctesttype"


body = {
    'url':"aaaaa",
    'title':"bbbbb",
    'content':"ccccc"
}
es.index(index, type, body,"docid11111")