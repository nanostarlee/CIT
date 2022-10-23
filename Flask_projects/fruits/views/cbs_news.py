import json
from flask import Blueprint, request, redirect, render_template
from bs4 import BeautifulSoup
import requests
from fruits.models import CbsNews

cbsviews = Blueprint('cbsviews', __name__)

def get_cbs_news():
    url = "https://www.cbsnews.com/latest/rss/main"
    response = requests.get(url)

    data = []

    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.find_all('tr', class_ = 'athing')

    for row in rows:
            # extract title
        image = row.find('span', class_ = 'titleline').find('a').string
        title = row.find('span', class_ = 'titleline').find('a').text
        description = row.find('span', class_ = 'titleline').find('a').text
        link = row.find('span', class_ = 'titleline').find('a')['href']
        
        data.append({
            'image': image,
            'title': title,
            'description': description,
            'link': link,            

        })

    return data

@cbsviews.route('/cbs_news', methods=['GET', 'POST'])
def cbs_news():
    if request.method == 'POST':
        return redirect('/')

# new data from cbs news
    data = get_cbs_news()

    # existing data from the database
    cbsnews = CbsNews.get_all_news()

    # loop through data
    for news in data:
        # check if news already exists in database
        if news.get('title').lower() not in [cbsn.title.lower() for cbsn in cbsnews]:
            cbsnew = CbsNews(image=news['image'],title=news['title'], link=news['link'],\
                description=news['description'] )
            cbsnew.save()
        else:
            continue

    return render_template('cbs_news.html', data=cbsnews)