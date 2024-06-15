import requests
from bs4 import BeautifulSoup

url = 'https://biblusi.ge/products?category=291&page=1'
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, 'html.parser')
books_soup = soup.find('div', class_='row')
# all_books = books_soup.find_all('article')

print(books_soup)
for i in books_soup:
    print(i)

# file = open('data.txt', 'w', encoding='UTF-8')

# for book in all_books:
#     book_descr = book.find('div', class_='span10')
#     title = book_descr.a.text
#     author = book_descr.b.a.text
#     price = book_descr.button.text.strip()
#     print(title,author, price)
#     file.write(title+', '+author+', '+price+'\n')
# file.close()