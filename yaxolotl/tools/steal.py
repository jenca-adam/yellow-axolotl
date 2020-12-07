from bs4 import BeautifulSoup as bs
import requests
import os
import ssl
import pickle

def steal_bib(arxivid,name):
    cont=requests.get('https://api.semanticscholar.org/arXiv:'+arxivid).text
    semantic_soup=bs(cont,'html.parser')
    print(cont)
    bib_cite=semantic_soup.find('textarea',class_="export-textarea form-control").text
    if not bib_cite:
        bib_cite='@article{'+name+','+'\n'+'}'
    return(bib_cite)
