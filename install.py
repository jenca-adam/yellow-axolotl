#!/usr/bin/env python
import os
import pip
version='dev'
print(f'Running YellowAxolotlInstaller version {version}')
print(f'Homepage: yellowaxolotl.xyz')
print('Installing packages')
pip.main(['install','flask','bs4','jinja2'])

try:
    os.mkdir(f'{os.path.expanduser("~")}/yaxolotl')

    new=True
except FileExistsError:
    print('Dir yaxolotl already exists. Rewriting data')
    new=False
os.system('cp -r ./yaxolotl ~/yaxolotl')
