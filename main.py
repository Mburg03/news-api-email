#! news-api-email\venv\Scripts\python.exe
import requests

url = "https://newsapi.org/v2/everything?q=tesla&from=2023-09-06&sortBy=publishedAt&apiKey=8c95c9a745c14bcfbece40161e9694ed"
my_api_key = "8c95c9a745c14bcfbece40161e9694ed"

request = requests.get(url)
content = request.text
print(content)
