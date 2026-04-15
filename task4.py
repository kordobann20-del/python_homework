import requests
from bs4 import BeautifulSoup
import csv

def get_books_data():
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    books_list = []
    page_number = 1

    print("--- Початок збору даних з books.toscrape.com ---")

    while True:
        url = base_url.format(page_number)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Обробка завершена. Оброблено сторінок: {page_number - 1}")
            break

        soup = BeautifulSoup(response.text, 'lxml')
        
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            title = book.h3.a['title']
          
            price = book.find('p', class_='price_color').text
            
            availability = book.find('p', class_='instock availability').text.strip()
          
            rating_classes = book.find('p', class_='star_rating')['class']
            rating = rating_classes[1]  

            books_list.append({
                'Title': title,
                'Price': price,
                'Availability': availability,
                'Rating': rating
            })

        print(f"Оброблено сторінку: {page_number}")
        page_number += 1

    return books_list

def save_to_csv(data, filename="books_data.csv"):
    if not data:
        return
    
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-16') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print(f"Дані успішно збережено у файл: {filename}")

if __name__ == "__main__":
    all_books = get_books_data()
    
    save_to_csv(all_books)
    
    print("\nПриклад зібраних даних (перші 5 книг):")
    for b in all_books[:5]:
        print(f"- {b['Title']} | {b['Price']} | {b['Rating']}")
