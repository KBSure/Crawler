from bs4 import BeautifulSoup
import re
source = open('melon.html', 'rt').read()
soup = BeautifulSoup(source)

result = []
for tr in soup.find_all('tr', class_='lst50'):
    rank = tr.find('span', class_ = 'rank').text
    title = tr.find('div', class_='rank01').find('a').text
    artist = tr.find('div', class_='rank02').find('a').text
    album = tr.find('div', class_='rank03').find('a').text
    url_img_cover = tr.find('a', class_='image_typeAll').find('img').get('src')
    p = re.compile(r'(.*\..*?)/')
    url_img_cover = re.search(p, url_img_cover).group(1)

    result.append({
        'rank': rank,
        'title': title,
        'url_img_coer': url_img_cover,
        'artist': artist,
        'album': album,
    })

print(result)
