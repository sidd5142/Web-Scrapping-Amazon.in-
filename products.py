import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def search_amazon_in(query):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        params = {
            "k": query
        }

        response = requests.get('https://www.amazon.in/s', headers=headers, params=params)

        soup = BeautifulSoup(response.content, 'html.parser')

        product_links = soup.select('div.s-result-item a.a-link-normal.s-no-outline')

        if product_links:
            product_urls = ["https://www.amazon.in" + link['href'] for link in product_links]
            return product_urls
        else:
            return None

    except Exception as e:
        print(f"An error occurred while searching: {str(e)}")
        return None

def scrape_amazon_product(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }

        response = requests.get(url, headers=headers)

        driver = webdriver.Chrome()

        driver.get(url)
        wait = WebDriverWait(driver,10)
        print("Enter any key to quit:")
        driver.quit()

        soup = BeautifulSoup(response.content, 'html.parser')

        product_name = soup.find("span", {"id": "productTitle"})
        if product_name:
            product_name = product_name.text.strip()
        else:
            product_name = "Product Name not found"

        product_price = soup.find("span", {"class": "a-offscreen"})
        if product_price:
            product_price = product_price.text.strip()
        else:
            product_price = "Product Price not found"

        product_beforeprice = soup.find("span", {"class": "a-price a-text-price"}).find("span", {"class": "a-offscreen"})
        if product_beforeprice:
            product_beforeprice = product_beforeprice.text.strip()
        else:
            product_price = "Product Price not found"

        product_rating = soup.find("span", {"class": "a-icon-alt"})
        if product_rating:
            product_rating = product_rating.text.strip()
        else:
            product_rating = "Product Rating not found"

        product_reviews = soup.find("span", {"id": "acrCustomerReviewText"})
        if product_reviews:
            product_reviews = product_reviews.text.strip()
        else:
            product_reviews = "Number of Product Reviews not found"

        product_availability = soup.find("div", {"id": "availability"})
        if product_availability:
            product_availability = product_availability.text.strip()
        else:
            product_availability = "Product Availability not found"

        product_data = {
            'Product Title': product_name,
            'Product Price After Offer': product_price,
            'Product Price Before Offer': product_beforeprice,
            'Product Rating': product_rating,
            'Number of Product Reviews': product_reviews,
            'Availability': product_availability
        }

        return product_data

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {}

if __name__ == '__main__':
    search_query = input("Enter the product you want to search for on Amazon.in: ")

    product_urls = search_amazon_in(search_query)

    if product_urls:
        for product_url in product_urls:
            product_info = scrape_amazon_product(product_url)
            print("Product Details:")
            for key, value in product_info.items():
                print(f"{key}: {value}")
            print("\n")
    else:
        print("No search results found.")






