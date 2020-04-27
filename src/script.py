
from bs4 import BeautifulSoup

with open("index.html", "r") as f:
    
    contents = f.read()
    data = {
        'titles': [],
        'descriptions': [],
        'urls': [],
        'dates': [],
        'wims': []
    }
    soup = BeautifulSoup(contents, 'html.parser')
    styles = soup.find_all('a', {'style':"color:#34495e; text-decoration:none;"})
    for title in styles:
        data['titles'].append(title.get_text())

    styles = soup.find_all('a', {'style':"color:#010101;text-decoration:none;"})
    for description in styles:
        data['descriptions'].append(description.get_text())
    
    styles = soup.find_all('a', {'style':"color:#c3c3c3;text-decoration:none;"})
    for dateOrUrl in styles:
        text = dateOrUrl.get_text()
        if'.' in text: 
            data['urls']. append(text)
        else:
            data['dates'].append(text)
    
    styles = soup.find_all('div', {'style':" overflow: hidden; text-overflow: ellipsis; word-wrap: break-word;width:318px"})
    for wim in styles:
        data['wims'].append(wim.get_text())