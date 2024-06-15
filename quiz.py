import requests, time, csv
from bs4 import BeautifulSoup

csv_data = []

for i in range(1, 6):
    url = f"https://biblusi.ge/products?category=291&page={i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find("div", class_="row")

    for book in books:
        title = book.find("acronym").text
        price = book.find(
            "div", attrs={"data-v-6cbcf536": ""}, class_="text-primary font-weight-700"
        ).text.strip()

        print(title, price)
        csv_data.append([title, price])

    print("\n")
    time.sleep(5)


f = open("books.csv", "w", encoding="utf-8_sig")
writer_obj = csv.writer(f)
writer_obj.writerow(["title", "price"])
for i in csv_data:
    writer_obj.writerow(i)
f.close()