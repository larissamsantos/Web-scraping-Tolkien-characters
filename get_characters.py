import bs4
import urllib.request as urllib_request
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

characters_category_url = 'https://lotr.fandom.com/wiki/Category:Characters'
response = urlopen(characters_category_url)
characters_category_html = response.read()
soup = BeautifulSoup(characters_category_html, 'html.parser')

links_list = []
categories = []
character_list = []

for item in soup.findAll('a', class_="category-page__member-link"): 
    href = item.get('href')
    if 'Category' in href:
        links_list.append('https://lotr.fandom.com'+item.get('href'))
for link in links_list:
    category_index = link.find('Category:')
    category_name = link[category_index+9:]
    categories.append({'category name': category_name, 'category url': link})
for category in categories:
    response = urlopen(category['category url'])
    category_html = response.read().decode('ISO-8859-1')
    soup = BeautifulSoup(category_html, 'html.parser')
    for item in soup.findAll('a', class_='category-page__member-link'): 
        href = item.get('href')
        if 'Category' in href:
            category_index = href.find('Category:')
            category_name = href[category_index+9:]
            category_name_url = {'category name': category_name, 'category url': 'https://lotr.fandom.com'+href}
            category_name_url_copy = category_name_url.copy()
            if category_name_url_copy not in categories:
                categories.append(category_name_url_copy)
        else:
            wiki_index = href.find('wiki/')
            character_name = href[wiki_index+5:]
            category_name = category['category name']
            category_character = {'category': category_name, 'character name': character_name}
            character_list.append(category_character)
            
character_df = pd.DataFrame(character_list)
character_df = character_df[character_df['category'].str.contains('Images_of')==False]
character_df.to_csv('characters.csv')