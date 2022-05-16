from bs4 import BeautifulSoup
import requests
import pymongo

bitcoin_list = []
all_transactions_list = []
bitcoin_time = ""
index = 0

client = pymongo.MongoClient("mongodb://localhost:27017")
dba_database = client["database"]

collections = dba_database["Transactie_per_minuut"]


while True:
    url ='https://www.blockchain.com/btc/unconfirmed-transactions'
    r = requests.get(url)
    unconfirmed_transaction = BeautifulSoup(r.text, features = "lxml") 
    data = unconfirmed_transaction.find_all('div',{ "class" : "sc-1g6z4xm-0 hXyplo" })
    data.reverse()

    for tags in data:
        tag = tags.get_text().replace("Hash" , "").replace("Time","  ").replace("Amount (BTC)" , "  ").replace("Amount (USD)", "  ").split("  ")
        if index == 0:
            bitcoin_time = tag[1]
            index += 1

        if tag[1] > bitcoin_time:
            for bitcoin_transaction in all_transactions_list:
                if bitcoin_transaction[2] == max(bitcoin_list):
                    print("Bitcoinhash:" , bitcoin_transaction[0],
                          "- Time:", bitcoin_transaction[1],
                          "- Bitcoin value:", bitcoin_transaction[2],
                          "- USD value:", bitcoin_transaction[3])
                    logfile = open(r"logfile.txt", "a")
                    logfile.write("Bitcoinhash: " + str(bitcoin_transaction[0]) + " - Time:" + str(bitcoin_transaction[1]) + " - Bitcoin value:" + str(bitcoin_transaction[2]) + " - USD value:" + str(bitcoin_transaction[3]))
                    logfile.close()
                    Highest_transactions_JSON = {
                        "Bitcoinhash" : bitcoin_transaction[0],
                        "Time" : bitcoin_transaction[1], 
                        "Bitcoin value" : bitcoin_transaction[2], 
                        "USD value" : bitcoin_transaction[3]
                    }
                    collections.insert_one(Highest_transactions_JSON)
                    break
            bitcoin_list.clear()
            all_transactions_list.clear()
            bitcoin_time = tag[1]
            all_transactions_list.append(tag)
            bitcoin_data = tag[2]
            bitcoin_list.append(bitcoin_data)
            
        elif tag[1] == bitcoin_time:
            all_transactions_list.append(tag)
            bitcoin_data = tag[2]
            bitcoin_list.append(bitcoin_data)