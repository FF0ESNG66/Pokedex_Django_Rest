from algoliasearch_django import algolia_engine

# · · · Initializing the client and index · · · # 

def get_client():
    return algolia_engine.client

def get_index(index_name='Pokedex_pkdx'):    # <- "pkdx" is the index_suffix we set in settings.py
    client = get_client()
    index = client.init_index(index_name)
    return index



def perform_search(query, **kwargs):
    index = get_index()
    results = index.search(query)
    filtered_results = []
    for hit in results['hits']:
        filtered_hit = {
            "pokedex_num": hit["pokedex_num"],
            "name": hit["name"],
            "description": hit["description"],
            "abilities": hit["abilities"],
            "types": hit["types"],
            "location": hit["location"],
            "total_locations": hit["total_locations"],
            "base_stats": hit["base_stats"]
        }
        filtered_results.append(filtered_hit)
    return filtered_results