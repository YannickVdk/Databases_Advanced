from bs4 import BeautifulSoup
import requests
import pymongo
import redis
import json

bitcoin_list = []
all_transactions_list = []
bitcoin_time = ""
index = 0
redisjson = {"transactions":[]}

#Mongo
client = pymongo.MongoClient("mongodb://localhost:27017")
dba_database = client["database"]

collections = dba_database["Transactie_per_minuut"]

#Redis
r = redis.Redis(port = 6379, charset = "utf-8", decode_responses = True)
redis_data = {"data": []}
r.set("data", json.dumps(redis_data))


while True:
    url ='https://www.blockchain.com/btc/unconfirmed-transactions'
    req = requests.get(url)
    unconfirmed_transaction = BeautifulSoup(req.text, features = "lxml") 
    data = unconfirmed_transaction.find_all('div',{ "class" : "sc-1g6z4xm-0 hXyplo" })
    data.reverse()

    for tags in data:
        tag = tags.get_text().replace("Hash" , "").replace("Time","  ").replace("Amount (BTC)" , "  ").replace("Amount (USD)", "  ").split("  ")
        if index == 0:
            bitcoin_time = tag[1]
            index += 1

        if tag[1] > bitcoin_time:
            allminutedata = json.loads(r.get("data"))
            highesttransaction = max(allminutedata['data'], key=lambda ev: ev['Bitcoin value'])     
            print(highesttransaction)
            collections.insert_one(highesttransaction)
            r.set("data", json.dumps(redis_data))
            
            cache = json.loads(r.get("data"))
            cache["data"].append({
                "Bitcoinhash" : tag[0],
                "Time" : tag[1],
                "Bitcoin value" : float(tag[2].replace(" BTC", "")),
                "USD value" : tag[3]
            })
            r.set("data", json.dumps(cache))
            bitcoin_time = tag[1]
            
        elif tag[1] == bitcoin_time:
            all_transactions_list.append(tag)
            cache = json.loads(r.get("data"))
            cache["data"].append({
                "Bitcoinhash" : tag[0],
                "Time" : tag[1],
                "Bitcoin value" : float(tag[2].replace(" BTC", "")),
                "USD value" : tag[3]
            })            
            r.set("data", json.dumps(cache))