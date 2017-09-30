#!/usr/bin/python3
import re, requests, sys,time, threading
from bs4 import BeautifulSoup
header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
		'AppleWebKit/537.36 (KHTML, like Gecko)'
		'Chrome/51.0.2704.103 Safari/537.36'
		}
def urlsearchv2(url):
	go=[];lista=[];global header;listan=[]
	page = (requests.get(url,headers=header)).text	
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
			lista.append(emailfinder(urele,data.text))
			for i in lista:
				if i:
					for vai in i:
						listan.append(vai)
		except:
			pass
	lista=set(listan)
	print(lista)
def urlsearch(url):
	lista=[];listan=[]
	page = (requests.get(url, headers=header)).text
	urlfinder = re.findall(r'href=[\'\"](https?://[\w:/\.\'\"]+)', page)
	urlfinder.insert(0,url)
	urlfinderuniq=set(urlfinder)
	for i in urlfinderuniq:
		print('Crawling: ',i)
		try:
			data = requests.get(i)
			lista.append(emailfinder(i,data.text))
			for go in lista:
				if go:
					for agoravai in go:
						listan.append(agoravai)
		except Exception as error:
			print('Error: ', error)
			continue
	birl=set(listan)
	print(birl)

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
#urlsearch(site)
#print('\n\n\n')
urlsearchv2(site)
