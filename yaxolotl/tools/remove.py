import shutil
import os
def rm(name):
    base=os.getcwd()
    os.chdir('/home/anna/work/awiki/pages/myown')
    with open('page.md')as f:
        lines=list(f.readlines())
    if f'1. [{name}]({name})\n' in lines:
        lines.remove(f'1. [{name}]({name})\n')
        myown=True
    else:
        myown=False
    print(myown)
    os.chdir('..')
    shutil.rmtree(name)
    if myown:
        os.chdir('myown')
        with open('page.md','w')as f:
            f.writelines(lines)
    else:
        os.chdir('notmyown')
        with open('page.md')as f:
            cont=f.read()
        cont=cont.replace(f'[{name}]({name}),' ,'')
        with open('page.md','w')as f:
            f.write(cont)
    os.chdir(base)
            
