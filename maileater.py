#!/usr/bin/python3
import re, requests, sys,time, threading
from bs4 import BeautifulSoup
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/51.0.2704.103 Safari/537.36'
    }

def checkstatus(data):
  if data.status_code == 404:
    print("[*] Page not found, leaving")
    sys.exit(1)

def urlsearchv2(url):
  go=[];lista=[];global header;listan=[]
  data = requests.get(url,headers=header)
  checkstatus(data)
  page = data.text  
  soup = BeautifulSoup(page, 'html.parser')
  links = soup.find_all('a')
  go.insert(0,url)
  for link in links:
    if str(link.get('href')).startswith('http://') or str(link.get('href')).startswith('https://') or str(link.get('href')).startswith('www'):
      go.append(str(link.get('href')))
      print('[*] Crawlink at:', link.get('href'))
    else:
      continue
  for urele in go:
    try:
      data=requests.get(urele,headers=header)
      checkstatus(data)
      print("[*] Searching emails at",urele)
      lista.append(emailfinder(urele,data.text))
      for i in lista:
        if i:
          for vai in i:
            listan.append(vai)
    except:
      pass
  lista=set(listan)
  print(lista)

def emailfinder(link,data):
  mailfer = re.findall(r'[\w-]+@[\w-]+\.[\w\.-]+', data)
  if mailfer:
    return(mailfer)

if len(sys.argv) < 1:
  site=input('URL: ')
else:
  site=sys.argv[1]
if site.startswith('http://'):
  pass
else:
  site='http://'+site
urlsearchv2(site)
