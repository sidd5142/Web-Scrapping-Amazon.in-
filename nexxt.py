import requests
from bs4 import BeautifulSoup

def search_amazon_in_product(query):
   
        
    base_url = "https://www.amazon.in/s"
    
    params = {
        "k": query 
    }

    response = requests.get(base_url, params=params)        

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        product_name = soup.find('span', {'class': 'a-size-base-plus a-color-base'})
        if product_name:
            product_name = product_name.get_text(strip=True)
        else:
            product_name = "Product Name not found"
        
        product_price = soup.find('span', {'id': 'priceblock_ourprice'})
        if product_price:
            product_price = product_price.get_text(strip=True)
        else:
            product_price = "Product Price not found"
        
        product_rating = soup.find('span', {'class': 'a-icon-alt'})
        if product_rating:
            product_rating = product_rating.get_text(strip=True)
        else:
            product_rating = "Product Rating not found"
        
        product_reviews = soup.find('span', {'id': 'acrCustomerReviewText'})
        if product_reviews:
            product_reviews = product_reviews.get_text(strip=True)
        else:
            product_reviews = "Product Reviews not found"
        
        product_availability = soup.find('div', {'id': 'availability'})
        if product_availability:
            product_availability = product_availability.get_text(strip=True)
        else:
            product_availability = "Product Availability not found"
        
        product_data = {
            'Product Name': product_name,
            'Product Price': product_price,
            'Product Rating': product_rating,
            'Product Reviews': product_reviews,
            'Product Availability': product_availability
        }
        
        return product_data
    else:
       print("Failed to retrieve Amazon India search results.")
    

if __name__ == '__main__':
    # Provide the Amazon product URL you want to scrape
    search_query = input("Enter the product you want to search for on Amazon.in: ")
    search_amazon_in_product(search_query)    

    base_url = "https://www.amazon.in/s"

    # Call the function to scrape product details
    product_info = search_amazon_in_product(base_url)
    
    # Display the scraped data
    for key, value in product_info.items():
        print(f"{key}: {value}")
