import requests
from bs4 import BeautifulSoup

# Function to scrape product details
def scrape_amazon_product(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
            
        
        # Send an HTTP GET request to the Amazon product page
        response = requests.get(url, headers=headers)
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract product name
        product_name = soup.find('span', {'id': 'productTitle'})
        if product_name:
            product_name = product_name.get_text(strip=True)
        else:
            product_name = "Product Name not found"
        
        # Extract product price
        product_price = soup.find('span', {'id': 'priceblock_ourprice'})
        if product_price:
            product_price = product_price.get_text(strip=True)
        else:
            product_price = "Product Price not found"
        
        # Extract product rating (if available)
        product_rating = soup.find('span', {'class': 'a-icon-alt'})
        if product_rating:
            product_rating = product_rating.get_text(strip=True)
        else:
            product_rating = "Product Rating not found"
        
        # Extract number of product reviews (if available)
        product_reviews = soup.find('span', {'id': 'acrCustomerReviewText'})
        if product_reviews:
            product_reviews = product_reviews.get_text(strip=True)
        else:
            product_reviews = "Product Reviews not found"
        
        # Extract product availability
        product_availability = soup.find('div', {'id': 'availability'})
        if product_availability:
            product_availability = product_availability.get_text(strip=True)
        else:
            product_availability = "Product Availability not found"
        
        # Return the scraped data as a dictionary
        product_data = {
            'Product Name': product_name,
            'Product Price': product_price,
            'Product Rating': product_rating,
            'Product Reviews': product_reviews,
            'Product Availability': product_availability
        }
        
        return product_data
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {}

if __name__ == '__main__':
    # Provide the Amazon product URL you want to scrape
    amazon_url = 'https://www.amazon.in/s'
    
    # Call the function to scrape product details
    product_info = scrape_amazon_product(amazon_url)
    
    # Display the scraped data
    for key, value in product_info.items():
        print(f"{key}: {value}")
