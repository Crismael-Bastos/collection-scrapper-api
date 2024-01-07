import requests
import pprint


def get_magic_eden_collection_top_sales(time: str = "10m", sales_minimum: str="30") -> list:
    """ time options: 10m, 1h.
        sales minimum: at least 30 to get good results.
    """
    url = f"https://stats-mainnet.magiceden.io/collection_stats/search/solana?window={time}&limit=50&offset=0&sort=sales&direction=desc&filter=%7B%22timeWindow%22:%22{time}%22,%22collectionType%22:%22all%22,%22sortColumn%22:%22sales%22,%22sortDirection%22:%22desc%22,%22sales%22:%7B%22minimum%22:{sales_minimum},%22maximum%22:5000%7D%7D"

    data = requests.get(url=url)
    if data.status_code == 200:
        return data.json()

def get_tensor_collection_info(url: str, collection_name: str, ):
    api_key = 'DOCUMENT_SEARCH_ONLY_KEY'
    headers = {
    'Content-Type': 'application/json',
    'X-Typesense-Api-Key': api_key
    }
    payload = {
        "searches": [   
            {
                "collection": "nft_collections",
                "q": collection_name,
                "query_by": "name,slugDisplay,acronym"
            }
        ]
    }
    data = requests.post(url=url, json=payload, headers=headers)
    if data.status_code == 200:
        return data.json().get('results')[0].get("hits")


if __name__ == "__main__":
    data =  get_magic_eden_collection_top_sales()
    pprint.pprint(data)

    # info = get_collection_info(url_2, payload)
    # pprint.pprint(info)
    # for collection in info:
    #     collection_name = collection.get('document').get("name")
    #     pprint.pprint(str(collection_name).replace(" ", "_").lower())
    # collection_name  = "Froganas"
    # url_2 = "https://search.tensor.trade/multi_search?sort_by=statsV2.volume24h:desc&infix=fallback,off,off&page=1&per_page=20&split_join_tokens=off&exhaustive_search=true&prioritize_exact_match=true"
    # info = get_tensor_collection_info(url_2, collection_name=collection_name)
    # pprint.pprint(info[0])
