import requests
from bs4 import BeautifulSoup
import re
import io

import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
req = requests.get('https://comment.bilibili.com/'+sys.argv[1]+'.xml')
req.encoding = req.apparent_encoding
soup = BeautifulSoup(req.text, 'html.parser').find_all(name='d')
result = ""
for i in soup:
    s = re.sub('<(.*?)>', '', str(i))
    index = 0
    if(len(sys.argv[2])>0):
        index = s.find(str(sys.argv[2]))
    if(index!=-1):
        result+=str(i).split(",")[6]+"*-*+*"+s+"*-*+*"+str(i).split(",")[4]+"*-*+*"+str(i).split(",")[0].split('"')[1]+"*-*+*"
print(result)