import requests
import json

def list_cards():
    url = 'https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid=583950&norender=1&count=500&start='
    card_list = []

    un = 0

    while un != 237:
        for i in range(0, 3):
            req_url = url + str(i*100)
            r = requests.get(req_url)
            r_json = r.json()
            for result in r_json['results']:
                resulting_obj = {}
                resulting_obj['name'] = result['name']
                resulting_obj['market_hash_name'] = result['asset_description']['market_hash_name']
                resulting_obj['type'] = result['asset_description']['type']
                card_list.append(resulting_obj)

        un = len({v['market_hash_name']:v for v in card_list}.values())

    return {v['market_hash_name']:v for v in card_list}.values()
