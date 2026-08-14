import requests
query="America and Iran crisis"
api="pub_265547de125e4a44ac7f6cecd59cf9d9" # My API key fpr NewsAPI website
url=f"https://newsdata.io/api/1/latest?apikey={api}&q={query}"
print(url)
r=requests.get(url)
data=r.json()  # The file is in JSON format so hence it is written r.json
 # Means the articles variable is storing the article from the data.
print(data)
articles=data["results"]# This will give the index number to the every result inside the data.
seen=set()
count=1
for index,article in enumerate(articles):
    key=(index+1,article["title"],article["link"])# Never give the key inside the bracket as url but give key as link
    # remember one thing that we have assigned the tuple to be a storage for the list of dictionaries
    if key not in seen:
        seen.add(key)
        print(count,article["title"])
        print(article["link"])
        print()
        count+=1


# For making use of the api key for getting the Indian news just visit the newAPI website get the url ad jus tgo on searching the news from yur api key
# import requests

# url = "https://newsdata.io/api/1/latest?" 
# apikey="pub_265547de125e4a44ac7f6cecd59cf9d9"
# response = requests.get(url)
# data = response.json()
# print(data)