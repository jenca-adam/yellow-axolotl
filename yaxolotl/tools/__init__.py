from . import loadpage,remove,search,steal
def add(id,authorname,path):
    return loadpage.loadpage(f'https://arxiv.org/abs/{id}',authorname,path)
def rm(name):
    remove.rm(name)
def search_arxiv(query,fields='all'):
    return search.search(query,fields)
def steal_bib(arxivid,name):
    return steal.steal_bib(arxivid,name)
