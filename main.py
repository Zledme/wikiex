import requests

from fastapi import FastAPI,HTTPException
import wikipedia
from collections import Counter

import json

app = FastAPI()

@app.get('/topic')
async def top_n_words_in_topicwiki(topic:str, n:int):
    #get the correct topic of page, we need to get the correct for of topic, eg pokemon is wrong, Pokémon is the correct version
    
    search_results = wikipedia.search(topic.lower(), results=1)
    
    if not search_results:
        raise HTTPException(status_code=404, detail="Requested topic not found")
    
    wikitopic = search_results[0]
    
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": f'{wikitopic}',
        "prop": "extracts",
        "explaintext": True
    }

    # Make the API request
    response = requests.get(api_url, params=params)
    data = response.json()

    # Extract the page content and get the n most frequent letters
    page_id = list(data["query"]["pages"].keys())[0]
    content = data["query"]["pages"][page_id]["extract"].lower()
    words = content.split()
    word_counts = Counter(words)
    top_n_words = word_counts.most_common(n)
    
    # Save the most common word to a file
    with open('savewiki.json', 'a') as file:
        json.dump({topic: top_n_words}, file)
        file.write('\n')
    return {'most_common_words': top_n_words}
    
@app.get('/history')
async def history():
    dict_list = []

    try:    
        with open('savewiki.json', 'r') as file:
            for line in file:
                dictionary = json.loads(line)
                dict_list.append(dictionary)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'history': []}
            
    return {'history': dict_list}
