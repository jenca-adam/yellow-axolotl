from httplib2 import Http
from bs4 import BeautifulSoup as bs
import re
h=Http()
pattern=r'(\d+.\d+)'
def search(query,fields='all'):
    resp,content=h.request(f'https://arxiv.org/search?query={query}&searchtype={fields}')
    soup=bs(content,'html.parser')
    results=soup.find_all('li',class_='arxiv-result')
    detail_results=[[res.find('p', class_='title is-5 mathjax').text,res.find('p',class_='authors').text,re.search(pattern,res.find('p',class_='list-title is-inline-block').find('a').text).groups()[0]]for res in results]
    return detail_results
