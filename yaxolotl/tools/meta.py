
import os,pickle

def reconfig(path,author):
    os.chdir(path)
    os.chdir('pages')
    files=os.listdir()
    print(*files)
    for i in files:
        os.chdir(path)
        os.chdir('pages')

        if i not in ['myown', 'notmyown', 'students', 'index', 'refs','.cache']:
            os.chdir(i)
            with open('meta.pickle','rb')as f:
                filedict=pickle.load(f)
            os.chdir('..')
            if author in filedict['authors']:
                os.chdir('myown')
            else:
                os.chdir('notmyown')
            with open('page.html','r')as f:
                page=f.readlines()
            if f'<li><a href="/view/{i}">{i}</a></li>\n' not in page:
                last=[page.pop()]
                last.insert(0,page.pop())
                last.insert(0,page.pop())
                page.append(f'<li><a href="/view/{i}">{i}</a></li>\n')
                page.extend(last)
            with open('page.html','w') as f:
                f.writelines(page)
        os.chdir(path)
                                        

