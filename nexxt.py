# import requests
# from bs4 import BeautifulSoup

# def search_amazon_in(query):
#     try:
#         headers = ({
#                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
#                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#                    'Accept-Language': 'en-US,en;q=0.5',
#         })

#         params = {
#             "k": query
#         }

#         response = requests.get('https://www.amazon.in/s', headers=headers, params=params)

#         soup = BeautifulSoup(response.content, 'html.parser')

#         first_result = soup.find('div', class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16')

#         print(first_result.prettify)
        
#         if first_result:
#             first_product_url = first_result.find('a', class_='a-link-normal')['href']
#         else:
#             return None

#         return first_product_url

#     except Exception as e:
#         print(f"An error occurred while searching: {str(e)}")
#         return None


# def scrape_amazon_product(url):
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
#         }

#         response = requests.get(url, headers=headers)

#         soup = BeautifulSoup(response.content, 'html.parser')

#         product_name = soup.find("h2", attrs={"class": 'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}).find("span", attrs={"class":'a-size-medium a-color-base a-text-normal'})
#         if product_name:
#             product_name = product_name.text(strip=True)
#         else:
#             product_name = "Product Name not found"

#         product_before_price = soup.find("span", attrs={'class': 'a-size-small a-color-secondary aok-align-center basisPrice'}).find("span", attrs={'class': 'a-offscreen'})
#         if product_before_price:
#             product_before_price = product_before_price.text.strip()
#         else:
#             product_before_price = "Product Price Before Offer not found"

#         product_price = soup.find("span", attrs={'class': 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'}).find("span", attrs={'class': 'a-offscreen'})
#         if product_price:
#             product_price = product_price.text.strip()
#         else:
#             product_price = "Product Price After Offer not found"

#         product_rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'})
#         if product_rating:
#             product_rating = product_rating.string.strip()
#         else:
#             product_rating = "Product Rating not found"

#         product_reviews = soup.find("span", attrs={'id': 'acrCustomerReviewText'})
#         if product_reviews:
#             product_reviews = product_reviews.string.strip()
#         else:
#             product_reviews = "Number of Product Reviews not found"

#         product_availability = soup.find("div", attrs={'id': 'availability'})
#         if product_availability:
#             product_availability = product_availability.find("span").string.strip()
#         else:
#             product_availability = "Product Availability not found"

#         product_data = {
#             'Product Title': product_name,
#             'Product Price Before Offer': product_before_price,
#             'Product Price After Offer': product_price,
#             'Product Rating': product_rating,
#             'Number of Product Reviews': product_reviews,
#             'Availability': product_availability
#         }

#         return product_data

#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
#         return {}

# if __name__ == '__main__':
#     search_query = input("Enter the product you want to search for on Amazon.in: ")

#     product_url = search_amazon_in(search_query)

#     if product_url:
#         full_product_url = 'https://www.amazon.in' + product_url
#         product_info = scrape_amazon_product(full_product_url)

#         for key, value in product_info.items():
#             print(f"{key}: {value}")
#     else:
#         print("No search results found.")

import requests
from bs4 import BeautifulSoup

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
            first_product_url = "https://www.amazon.in" + product_links[0]['href']
        else:
            return None

        return first_product_url

    except Exception as e:
        print(f"An error occurred while searching: {str(e)}")
        return None

def scrape_amazon_product(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }

        response = requests.get(url, headers=headers)

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

        product_rating = soup.find("i", {"class": "a-icon a-icon-star-small a-star-small-3-5 aok-align-bottom"})
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
            'Product Price': product_price,
            'Product Before Price' : product_beforeprice,
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

    product_url = search_amazon_in(search_query)

    if product_url:
        product_info = scrape_amazon_product(product_url)

        for key, value in product_info.items():
            print(f"{key}: {value}")
    else:
        print("No search results found.")

