from . import loadpage,remove,search,steal
def add(id):
    return loadpage.loadpage(f'https://arxiv.org/abs/{id}')
def rm(name):
    remove.rm(name)
def search_arxiv(query,fields='all'):
    return search.search(query,fields)
def steal_bib(arxivid,name):
    return steal.steal_bib(arxivid,name)
