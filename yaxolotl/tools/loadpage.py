#!/usr/bin/env python3
import httplib2
from bs4 import BeautifulSoup as bs
import sys
import re
import colorama
import os
import shutil
from . import arxiv
from .steal import steal_bib
BLUE=colorama.Fore.BLUE
RESET=colorama.Style.RESET_ALL
BOLD = '\033[1m'
RED=colorama.Fore.RED
GREEN=colorama.Fore.GREEN
CYAN=colorama.Fore.CYAN
YELLOW=colorama.Fore.LIGHTYELLOW_EX
MAGENTA=colorama.Fore.MAGENTA
dateline_pattern=r'\D*\d+(\D+)(\d+)'
title_pattern=r'<h1 class="title mathjax"><span class="descriptor">Title\:</span>(\D*)<'
authors_pattern=r'Authors:(\D*)'
linkstr_pattern=r'^https?://arxiv.org/abs/\D*/?(\d+.\d+)$'
h=httplib2.Http('pages/.cache')
base=os.getcwd()
diacritic_dict={
    'á':'a',
    "ä":"a",
    "é":"e",
    "ě":"e",
    "í":"i",
    "ó":"o",
    "ô":"o",
    "ú":"u",
    "ü":"u",
    "ľ":"l",
    "ĺ":"l",
    "ŕ":"r",
    "ř":"r",
    "ñ":"n",
    "ň":"n",
    "ů":"u",
    "ö":"o",
    "ë":"e",
    "û":"u",
    "č":"c",
    "ť":"t",
    "ď":"d",
    "ž":"z",
    "ý":"y",
    "ï":"i",
    "ł":"l",
}

def loadpage(link):
    os.chdir(f'{base}/pages')
    linkmatch=re.search(linkstr_pattern,link)
    id=linkmatch.groups()[0]
    page=arxiv.ArXivPage(id)
    print(f'{BOLD}Start of informative output{RESET}')
    print(page.title)
    print(page.month,page.year)
    print(page.strauthors)
    print(page.abstract)
    print(f'{BOLD}End of informative output{RESET}')
    print('__________________________________________________')
    print(f'{GREEN}Writing page.md{RESET}')
    authorname=page.authors[0].split(' ')[-1].lower()
    authorname=''.join([diacritic_dict[char] if char in diacritic_dict else char for char in authorname ])
    thingname=page.title.split(' ')[0].lower().replace(',','')
    word=1
    while len(thingname)<7:
        thingname+=page.title.split(' ')[word].lower().replace(',','')
        word+=1
    name=''.join([authorname,str(page.year),thingname])
    print(f'{YELLOW}Directory name:{name}{RESET}')
    try:
        os.mkdir(name)
        os.chdir(name)
    except FileExistsError as err:
        print(f'{RED}dir {name} already exists.Skipping.{RESET}')
        os.chdir(base)
        return {'status':'error','response':{'message':str(err),'type':'FileExistsError'}}
    linkmatch=re.search(linkstr_pattern,link)
    linkid=linkmatch.groups()[0]
    print(linkid)
    print('{YELLOW}Stealing BibTex...{RESET}')
    bibtex=steal_bib(linkid,name)

    linkstr=f'<a href="https://arxiv.org/abs/{linkid})">In ArXiv</a>'
    pagestring=f'<html><head><title>{name}</title></head><body><h1>Reference</h1>\n\n\t{(", ").join(page.authors)};{page.title};{page.jrefs};{page.month}\b{page.year};\n\n<h1>Abstract</h1> \n{page.abstract}\n\n{linkstr}</body></html>'
    print(f'{name}/page.md:\n\n{CYAN}{pagestring}{RESET}')
    print(os.getcwd())
    with open('page.html','w')as f:
        f.write(pagestring)
    with open('bib.bib','w')as f:
        f.write(bibtex)
    if 'Anna Jenčová' in page.authors  or 'Anna Jencova' in page.authors:
        mypath='myown'
    else:
        mypath='notmyown'
    cmypath=f'{GREEN}myown{RESET}'if mypath == 'myown' else f'{YELLOW}notmyown{RESET}'
    print(f'page {name} should go to {cmypath}')
    writein=True
    os.chdir('..')
    if writein:
        print(f'{MAGENTA}Writing in {cmypath}/{CYAN}page.md{RESET}')
        print('__________________________________________________')
        os.chdir(mypath)
        if mypath=='myown':
            with open('page.md','a')as f:
                mylinkstr=f'1. [{name}]({name})\n'

                f.write(mylinkstr)
            if '-v' in sys.argv:
                with open('page.md')as f:
                    print(f.read())
        else:
            mylinkstr=f'[{name}]({name}),\n'

            with open('page.md','r')as f:
                lines=list(f.readlines())
            alphabetindex=lines.index(f'### {name[0].upper()}\n')+1
            lines.insert(alphabetindex,mylinkstr)
            with open('page.md','w')as f:
                f.writelines(lines)
            if '-v' in sys.argv:
                print(*lines)
        print(f'{GREEN}Done{RESET}')
        os.chdir(base)
        return {'status':'OK','response':{'message':'OK'}}
   
