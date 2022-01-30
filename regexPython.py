#!/usr/bin/env python
#!python



import re
from sys import *


file = open("regex.txt","r")
text = file.read()
regex = r".+(?=View)"


for search in re.finditer(regex, text):
    print search.group()



exit()