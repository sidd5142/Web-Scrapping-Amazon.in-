from bs4 import BeautifulSoup
import requests

def get_title(soup):
	
	try:
		title = soup.find("span", attrs={"id":'productTitle'})

		title_value = title.string

		title_string = title_value.strip()

	

	except AttributeError:
		title_string = ""	

	return title_string

def get_beforeprice(soup):

	try:
		price = soup.find("span", attrs={'class':'a-size-small a-color-secondary aok-align-center basisPrice'}).find("span", attrs={'class':'a-offscreen'}).text
		

	except AttributeError:
		price = ""	

	return price


def get_price(soup):

	try:
		price = soup.find("span", attrs={'class':'a-price aok-align-center reinventPricePriceToPayMargin priceToPay'}).find("span", attrs={'class':'a-offscreen'}).text
		

	except AttributeError:
		price = ""	

	return price

def get_rating(soup):

	try:
		rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
		
	except AttributeError:
		
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
		except:
			rating = ""	

	return rating

def get_review_count(soup):
	try:
		review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
		
	except AttributeError:
		review_count = ""	

	return review_count

def get_availability(soup):
	try:
		available = soup.find("div", attrs={'id':'availability'})
		available = available.find("span").string.strip()

	except AttributeError:
		available = ""	

	return available	

if __name__ == '__main__':

	HEADERS = ({'User-Agent':
	            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
	            'Accept-Language': 'en-US, en;q=0.5'})

	URL = "https://www.amazon.in/Lenovo-35-56cm-400Nits-Warranty-82QE0060IN/dp/B0B7RZCXS9/"

	webpage = requests.get(URL, headers=HEADERS)

	soup = BeautifulSoup(webpage.content, "lxml")

	print("Product Title =", get_title(soup))
	print("Product Price Before Offer =", get_beforeprice(soup))
	print("Product Price After Offer =", get_price(soup))
	print("Product Rating =", get_rating(soup))
	print("Number of Product Reviews =", get_review_count(soup))
	print("Availability =", get_availability(soup))
	print()
	print()