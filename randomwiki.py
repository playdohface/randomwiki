import requests

api_url = "https://en.wikipedia.org/w/api.php?action=query&format=json&list=random&rnnamespace=0&rnlimit=1"
response = requests.get(api_url)
print(response.json()['query']['random'][0]['title']) 


id = response.json()['query']['random'][0]['id']
article_url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&list=&export=1&pageids="+ str(id) +"&exchars=1200&explaintext=1&exsectionformat=plain"
article_response = requests.get(article_url)
print(article_response.json()['query']['pages'][str(id)]['extract'])