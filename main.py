import requests
from bs4 import BeautifulSoup

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 7.1; Xperia V Build/NDE63X) AppleWebKit/600.3 (KHTML, like Gecko)  Chrome/55.0.2635.298 Mobile Safari/533.5',
}
for i in range(1,4):
    print(f'Parsing {i} page')
    url = f'https://www.olx.kz/list/q-%D0%B5%D0%BB%D0%BA%D0%B8/'  
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    cards = soup.find_all("div",class_='css-qfzx1y')

    for card in cards:
        card_url = card.a['href']
        url = f'https://www.olx.kz{card_url}.html'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text,'lxml')
        description = soup.find('div', 'css-1t507yq.er34gjf0')
        print(description.text)       
    
