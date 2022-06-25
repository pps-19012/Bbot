import bs4
import lxml
import requests
import random
from bs4 import BeautifulSoup

num = 0
html_text = requests.get('https://www.quotes.net/movies/silicon_valley_106290').text
#print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
paragraphs = soup.find_all('div', class_ = "disp-mquote-ext clearfix")

def svquote():
  i = random.randint(0, 86)
  paragraph = paragraphs[i]
  persons = paragraph.find_all('p')
  quote = ""
  for person in persons:
    quote += str(person.text)+ "\n"
  return quote

def ramquote():
  html_text = requests.get('https://everydaypower.com/rick-and-morty-quotes/').text
    #print(html_text)
  soup = BeautifulSoup(html_text, 'lxml')
  content = soup.find('div', id = "mvp-content-main")
  paragraphs = content.find_all('p')
  num = 1
  finallist = []
  for paragraph in paragraphs:
    sentence = paragraph.text
    if(num<10):
      if(sentence[0] == str(num)):
        finallist.append(sentence[3:])
        num += 1
    if(num>=10):
      if(sentence[0:2] == str(num)):
        finallist.append(sentence[4:])
        num += 1
  i = random.randint(0, 60)
  return finallist[i]
