import requests

def randomwiki():
    api_url = "https://en.wikipedia.org/w/api.php?action=query&format=json&list=random&rnnamespace=0&rnlimit=1"
    response = requests.get(api_url)
    if response.status_code != 200:
        print("There has been an error.")
    else:
        print("Your random Wikipedia Article is: " + response.json()['query']['random'][0]['title'])

        if input("Would you like to read it? (y/n) ") == 'y':
            id = response.json()['query']['random'][0]['id']
            article_url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&list=&export=1&pageids="+ str(id) +"&exchars=1200&explaintext=1&exsectionformat=plain"
            article_response = requests.get(article_url)
            print(article_response.json()['query']['pages'][str(id)]['extract'])
            return True
        
        else:
            return True
more = True
while more:
    randomwiki()
    if input("Would you like another one? (y/n)") != 'y':
        more = False
        break