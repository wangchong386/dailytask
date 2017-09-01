#!/usr/bin/env python
# coding=utf-8

import json

fileInputs = {    
    'item_list': '/data/item_list_all.jl',
    'item_store': '/data/item_storeInfo_all.jl',
    'item_feedback': '/data/item_feedbak_all.jl'
}

def parseItemList():
    with open(fileInputs['item_list']) as f:
        with open(fileInputs['item_list'] + '.txt', 'a') as parsed:
            for line in f:
                new_line = ""
                fieldDelimiter = '\007'
                data = json.loads(line)
                new_line += str(data['item_code'])
                new_line += fieldDelimiter
                new_line += str(data['item_name'])
                new_line += fieldDelimiter
                new_line += str(data['item_cate'])
                new_line += fieldDelimiter
                new_line += str(data['order_num'])
                new_line += fieldDelimiter
                new_line += str(data['price'])
                new_line += fieldDelimiter
                new_line += str(data['ori_price'])
                new_line += fieldDelimiter
                new_line += str(data['rate_star'])
                new_line += fieldDelimiter
                new_line += str(data['current_page'])
                new_line += fieldDelimiter
                new_line += str(data['url'])
                new_line += fieldDelimiter
                new_line += str(data['store_url'])
                new_line += fieldDelimiter
                new_line += str(data['store_feed_url'])
                new_line += fieldDelimiter
                new_line += str(data['crawl_time'])
                parsed.write(new_line + '\n')

def parseItemStore():
    with open(fileInputs['item_store']) as f:
        with open(fileInputs['item_store'] + '.txt', 'a') as parsed:
            for line in f:
                data = json.loads(line)
                new_line = ""
                fieldDelimiter = '\007'
                new_line += str(data['store_num'])
                new_line += fieldDelimiter
                new_line += str(data['store_name'])
                new_line += fieldDelimiter
                new_line += str(data['store_time'])
                new_line += fieldDelimiter
                new_line += str(data['crawl_time'])
                new_line += fieldDelimiter
                new_line += str(data['store_url'])
                new_line += '\n'
                parsed.write(new_line)

def parseItemFeedback():
    with open(fileInputs['item_feedback']) as f:
        with open(fileInputs['item_feedback'] + '.txt', 'a') as parsed:
            for line in f:
                data = json.loads(line)
                records = data['records']
                for i in records:
                    new_line = ""
                    fieldDelimiter = '\007'
                    new_line += (data['item_code'].encode('utf-8')
                                 if 'item_code' in data else '')
                    new_line += fieldDelimiter
                    new_line += (data['current_page'].encode('utf-8')
                                 if 'current_page' in data else '')
                    new_line += fieldDelimiter
                    new_line += (data['total_page'].encode('utf-8')
                                 if 'total_page' in data else '')
                    new_line += fieldDelimiter
                    new_line += (i['hasDigg'].encode('utf-8')
                                 if 'hasDigg' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['canDigg'].encode('utf-8')
                                 if 'canDigg' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['countryCode'].encode('utf-8')
                                 if 'countryCode' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['rank'].encode('utf-8')
                                 if 'rank' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['buyerFeedback'].encode('utf-8')
                                 if 'buyerFeedback' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['id'].encode('utf-8')
                                 if 'id' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['unit'].encode('utf-8')
                                 if 'unit' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['buyerReply'].encode('utf-8')
                                 if 'buyerReply' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['diggDown'].encode('utf-8')
                                 if 'diggDown' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['supplierReply'].encode('utf-8')
                                 if 'supplierReply' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['star'].encode('utf-8')
                                 if 'star' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['option'].encode('utf-8')
                                 if 'option' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['price'].encode('utf-8')
                                 if 'price' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['memberid'].encode('utf-8')
                                 if 'memberid' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['countryName'].encode('utf-8')
                                 if 'countryName' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['date'].encode('utf-8')
                                 if 'date' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['name'].encode('utf-8')
                                 if 'name' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['evaluationId'].encode('utf-8')
                                 if 'evaluationId' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['buyerAccountPointLeval'].encode('utf-8')
                                 if 'buyerAccountPointLeval' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['diggUp'].encode('utf-8')
                                 if 'diggUp' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['lotNum'].encode('utf-8')
                                 if 'lotNum' in i else '')
                    new_line += fieldDelimiter
                    new_line += (i['quantity'].encode('utf-8')
                                 if 'quantity' in i else '')
                    new_line += '\n'
                    parsed.write(new_line)

if __name__ == "__main__":
    parseItemList()
    parseItemStore()
    parseItemFeedback()
