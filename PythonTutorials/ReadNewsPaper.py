from win32com.client import Dispatch
import requests
import json

## Read NewsPaper

def speak(str):
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)

if __name__ == '__main__':
    speak('News of today..lets begin')
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=2f6b44dee0bc411fa156da2403d5f9f5'
    news = requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict['articles'])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak('And the next news is ..')
