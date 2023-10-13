#! news-api-email\venv\Scripts\python.exe
import requests
import datetime
from functions import send_email

today_date = datetime.date.today().isoformat()
yesterday = datetime.date.today() - datetime.timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")
print(yesterday_str)
topic = 'ai'
# url = f"https://newsapi.org/v2/everything?q={topic}&from={today_date}&"\
#       "apiKey=8c95c9a745c14bcfbece40161e9694ed"

url = f"https://newsapi.org/v2/everything?q=ai&from={yesterday_str}&language=en&"\
    "apiKey=8c95c9a745c14bcfbece40161e9694ed"
    
my_api_key = "8c95c9a745c14bcfbece40161e9694ed"
FILEPATH = './report.txt'

# Make a request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
titles = []
descriptions = []
links = []

for article in content["articles"][:12]:
    titles.append(article["title"])
    descriptions.append(article["description"])
    links.append(article["url"])

articles = list(zip(titles, descriptions, links))

with open(FILEPATH,'w') as file:
    article_number = 1
    for article in articles:
        header = f"{str(article_number)}. Title: {article[0]}"
        description = f"Description: {article[1]}..."
        url = f"Read more: {article[2]}"
        file.write(header + 2*"\n" + description  + "\n" + url + 2*"\n")
        article_number += 1
        
with open(FILEPATH,'r') as report:
    articles_report = report.read()

complete_message = f"""\
Subject: Top 20 AI News from today! 🤖📰

Hello, I'm here just to make sure you know everything you care about :)
Most relevant AI news from today 🗓️
Here you have the list:

{articles_report}

Keep up the good work! ✌️
"""
encoded_message = complete_message.encode('utf-8')
send_email(encoded_message)
