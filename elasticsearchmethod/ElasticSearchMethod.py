# coding=gbk
import requests
import json

def query(agentid, channel, orderid):
    uri = "http://47.97.23.193:9200/_search?pretty"
    param = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"channel": channel}}
                    # {"match": {"failMsg": "车票预订页，。"}}
                    # {"match": {"agentID": agentid}},
                    # {"match": {"orderID": orderid}},
                    # {"range": {
                    #     "createOrderStartTimeSel": {
                    #         "gte": 201805250000000
                    #     }
                    # }},
                    # {"range": {
                    #     "createOrderFinishTimeSel": {
                    #         "lte": 201806110000000
                    #     }
                    # }}
                ]
            }
        },
        "size": 20
    }
    result = requests.post(url=uri, json=param)
    print(str(result.content.decode("utf-8")))


def deleteByQuery():
    uri = "http://47.97.23.193:9200/shijialeitest/doc/_delete_by_query?pretty"
    param = {
        "query": {
            "match": {"channel": 2}
        }
    }
    result = requests.post(url=uri, json = param)
    print(result)

def update(index, type, id, key, val):
    uri = "http://47.97.23.193:9200/" + index + "/" + type + "/" + id + "/_update?pretty"
    print(uri)
    param = {
        "doc": {
            key: val
        }
    }
    result = requests.post(url=uri, json=param)
    print(result.content)


def insert(index, id):
    uri = "http://47.97.23.193:9200/" + index + "/doc/" + str(id) + "/_create?pretty"
    print(uri)
    param = {
        "agentID": 47,
        "channel": 2,
        "createOrderChannel": 1,
        "createOrderDepletionTime": 20534,
        "createOrderFinishTime": "2018-05-31 15:29",
        "createOrderFinishTimeSel": 201805311529091,
        "createOrderMode": 1,
        "createOrderStartTime": "2018-05-31 15:29",
        "createOrderStartTimeSel": 201805311529557,
        "createOrderType": 1,
        "cycleCount": 2,
        "cycleStepsInfo": '',
        "failMsg": "SUCCESS-E727176746。",
        "orderID": 124562425
    }
    result = requests.post(url=uri, json=param)
    print(str(result.content.decode("utf-8")))

def insertByStr(param, isds):
    uri = "http://47.97.23.193:9200/shijialeitest/doc/" + str(isds) + "/_create?pretty"
    try:
        requests.post(url=uri, json=json.loads(param))
    except:
        pass
    print(uri)


def readFileInsert():
    file = open('C:\\Users\\Administrator\\Desktop\\log\\CreateOrderDepltionTimeInfo.log','r')
    isds = 3832
    for i in file.readlines():
        insertByStr(i, isds)
        isds += 1


if __name__ == '__main__':
    readFileInsert()
    # deleteByQuery()
    # query(47, 2, 124562425)
    # update('redis-log-2018.05.30', 'doc', 'yld9r2MB2DshvOJGeBvP', 'channel', 2)
    # insert('shijialeitest',124562425)
