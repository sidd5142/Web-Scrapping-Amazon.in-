# from requests_html import HTMLSession
# from bs4 import BeautifulSoup

# s=HTMLSession()
# url = 'https://www.amazon.in/s	?k=dslr&crid'

# def getdata(url):
#     r=s.get(url)
#     soup = BeautifulSoup(r.text, "html.parser")
#     # print(soup.prettify)
#     return soup.prettify

# print(getdata(url))

# import requests
# from bs4 import BeautifulSoup

# def search_amazon_in_product(query):
#     base_url = "https://www.amazon.in/s"
    
#     params = {
#         "k": query 
#     }

#     # Send a GET request to Amazon India
#     response = requests.get(base_url, params=params)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')

#         product_titles = soup.find('div', class_='a-section a-spacing-small a-spacing-top-small')

#         # for title in product_titles:
#         #     print(title.text)
            

#         if product_titles:
#             print("First Product Title:", product_titles.text.strip())
#         else:
#             print("No product title found on the page.")

#     else:
#         print("Failed to retrieve Amazon India search results.")

# if __name__ == "__main__":
#     search_query = input("Enter the product you want to search for on Amazon.in: ")
#     search_amazon_in_product(search_query)


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

        first_product_image = soup.find('img', class_='s-image')

        if first_product_image and 'alt' in first_product_image.attrs:
            product_title = first_product_image['alt']
            print("First Product Title:", product_title)
        else:
            print("No product title found on the page.")

    else:
        print("Failed to retrieve Amazon India search results.")

if __name__ == "__main__":
    search_query = input("Enter the product you want to search for on Amazon.in: ")
    search_amazon_in_product(search_query)

