#! news-api-email\venv\Scripts\python.exe
import requests
from functions import send_email

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=8c95c9a"\
      "745c14bcfbece40161e9694ed"
my_api_key = "8c95c9a745c14bcfbece40161e9694ed"
FILEPATH = './text-files/report.txt'

# Make a request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
titles = []
descriptions = []

for article in content["articles"]:
    titles.append(article["title"])
    descriptions.append(article["description"])

articles = list(zip(titles, descriptions))

with open(FILEPATH,'w') as file:
    article_number = 1
    for article in articles:
        header = f"{str(article_number)} - Title: {article[0]}"
        description = f"Description: {article[1]}"
        file.write(header + "\n" + description  + "\n" + "\n")
        article_number += 1
        
with open(FILEPATH,'r') as report:
    articles_report = report.read()

complete_message = f"""\
Subject: Tech Crunch News

{articles_report}
"""
encoded_message = complete_message.encode('utf-8')
send_email(encoded_message)
