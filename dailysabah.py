from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

urlrequest = requests.get("https://www.dailysabah.com/")
soup = BeautifulSoup(urlrequest.content, 'html5lib')

all_headings = soup.find_all('h3')

all_headings = all_headings[0:-1] 

dailysabah_news = []

for ds in all_headings:
    dailysabah_news.append(ds.text)
    
    
def index(request):
    return render(request, 'index.html', {'dailysabah_news':dailysabah_news })
