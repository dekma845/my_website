from bs4 import BeautifulSoup
import requests

def extract_links(soup):
    links = []
    
    for link in soup.find_all('a', class_='wdp-playlist-video-card-module__title'):
        if link.has_attr('href'):
            full_link = link['href']
            # Извлекаем ID между '/video/' и '?playlist'
            id_start = full_link.find('/video/') + len('/video/')
            id_end = full_link.find('?', id_start)
            video_id = full_link[id_start:id_end]
            
            # Формируем полную ссылку
            full_rutube_url = f"https://rutube.ru/play/embed/{video_id}"
            print(full_rutube_url)
            links.append(full_rutube_url)
    
    return links

def get_url(url = 'https://rutube.ru/plst/721032/'):
    # Получаем HTML-код страницы
    response = requests.get(url)
    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Вызываем функцию для извлечения ссылок
    return extract_links(soup)

