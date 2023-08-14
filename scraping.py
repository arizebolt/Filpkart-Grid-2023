import requests
from bs4 import BeautifulSoup
import csv

def scrape_flipkart_products():
    url = 'https://www.flipkart.com/clothing-and-accessories/topwear/tshirts/pr?sid=clo'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for product in soup.find_all('div', class_='IIdQZO _1SSAGr'):
        title = product.find('a', class_='IRpwTa').text
        price = product.find('div', class_='_30jeq3').text
        products.append({'title': title, 'price': price})

    return products

def save_to_csv(data):
    with open('product_data.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price'])
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    product_data = scrape_flipkart_products()
    save_to_csv(product_data)
