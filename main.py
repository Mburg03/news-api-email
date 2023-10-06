#! news-api-email\venv\Scripts\python.exe
import requests

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=8c95c9a745c14bcfbece40161e9694ed"
my_api_key = "8c95c9a745c14bcfbece40161e9694ed"

# Make a request
request = requests.get(url)
# Get a dictionary with data
content = request.json()

# Acces the article, titles and description
for index, article in enumerate(content["articles"],1):
    print(f"{index}- Title: {article['title']}")
    print(f"Description: {article['description']}")