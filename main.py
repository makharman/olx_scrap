import requests
from bs4 import BeautifulSoup
# HEADER выдает ошибку, без Header код запускается
for i in range(1,4):
    print(f'Parsing {i} page')
    url = f'https://www.olx.kz/list/q-%D0%B5%D0%BB%D0%BA%D0%B8/?page={i}'  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    cards = soup.find_all("div",class_='css-1sw7q4x')

    for card in cards:
        card_url = card.a['href']
        url = f'https://www.olx.kz{card_url}'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text,'lxml')
        description = soup.find("div", 'css-1t507yq er34gjf0')
        print(description.text)       
    
