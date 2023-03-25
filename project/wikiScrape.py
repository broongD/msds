import bs4
from bs4 import BeautifulSoup
import re
import wikipedia
import requests

def scrapeClean(inputText):

    #choose the topic
    def wikiChoose(inp):
        search = wikipedia.search(inp, results=1, suggestion=False)[0]
        choice = re.sub(r' ','_',search)
        return 'https://en.wikipedia.org/wiki/'+choice

    url=wikiChoose(inputText)

    #fetch and scrape url
    data = requests.get(url)
    soup = BeautifulSoup(data.text,'html.parser')

    #fetch paragraph content from soup
    paras = soup.find_all('p')

    #clean paragraphs into readable text string
    textstr = ''''''''
    for para in paras:
        para = para.text
        para = re.sub(r'\[.*?\]', '', para)
        para = re.sub(r'\n',' ',para)
        textstr = textstr + para

    return textstr
