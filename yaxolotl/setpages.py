#!/usr/bin/env python
import pickle
import os
name=input('Enter your name:')
with open('meta/meta.pickle','wb')as f:
    pickle.dump({'name':name,'yaxpath':os.getcwd()},f)
os.chdir('pages')
os.chdir('index')
with open('page.html','w')as f:
    f.write(f'''<html>
<head>
<title>Homepage of {name}</title>
</head>
<body>
<div id="content">
<h1>Homepage of {name}</h1>
_____________________________________________________
<h2>My work</h2>
<div id="links">
<a href="/view/referee/">My referees</a>
<a href="/view/my/">My own works</a>
<a href="/view/notmy">Not my own works</a>
<a href="/view/students">My students</a>
</div>

</div>
<footer><i>Powered by:YellowAxolotl Web Engine</i></footer>
</body>

</html>''')
    
