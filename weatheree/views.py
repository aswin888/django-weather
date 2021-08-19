from bs4 import BeautifulSoup
from django.shortcuts import render

# Create your views here.

txt = "DATA NOT ATTAINABLE"  # GLOBAL


def index(request):
    if 'city' in request.GET:
        city = request.GET['city']
        data = scraper(city)
        print(data)
        context = {"city": city, "temp": data[0], "sky": data[1],
                   "time": data[2], "pos": data[3]}
        return render(request, 'weatheree/index.html', context)

    else:
        city = ''
        context = {"city": txt, "temp": txt, "sky": txt,
                   "time": txt, "pos": txt}
        return render(request, 'weatheree/index.html', context)


def scraper(city):
    import requests
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    if(soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}) is None):
        return(txt, txt, txt, txt)
    else:
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        data = str.split('\n')
        time = data[0]
        sky = data[1]
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        strd = listdiv[5].text
        pos = strd.find('Wind')
        return(temp, sky, time, pos)
