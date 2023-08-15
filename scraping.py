import requests
from bs4 import BeautifulSoup
import csv

def scrape_flipkart_search_results(search_url):
    all_products = []

    while search_url:
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        for product in soup.find_all('div', class_='_1AtVbE'):
            title_element = product.find('a', class_='IRpwTa')
            price_element = product.find('div', class_='_30jeq3')

            if title_element and price_element:
                title = title_element.text
                price = price_element.text
                product_url = 'https://www.flipkart.com' + title_element['href']

                product_data = scrape_product_details(product_url)
                clothing_tags = extract_clothing_tags(product_data)

                all_products.append({'title': title, 'price': price, 'tags': clothing_tags})

        next_page = soup.find('a', {'rel': 'next'})
        if next_page:
            search_url = 'https://www.flipkart.com' + next_page['href']
        else:
            search_url = None

    return all_products


def scrape_product_details(product_url):
    response = requests.get(product_url)
    return response.content

def extract_clothing_tags(product_data):
    # Implement logic to extract relevant clothing tags from product details
    # This could involve using NLP techniques or pattern matching
    # For demonstration purposes, let's assume some sample tags
    tags = ['pants', 'shirts', 'young', 'women']
    return tags

def save_to_csv(data):
    with open('fashion_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price', 'tags'])
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    search_url = 'https://www.flipkart.com/search?q=clothing&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    product_data = scrape_flipkart_search_results(search_url)
    save_to_csv(product_data)
