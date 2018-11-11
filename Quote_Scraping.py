import requests
from bs4 import BeautifulSoup
from time import sleep
all_quotes = []  
#Blank list for further use"""
url1 = "http://quotes.toscrape.com/"
url2 = "/page/1/"


while url2:
 response = requests.get(f"{url1}{url2}")
 print(f"Scraping {url1}{url2}......")
 soup = BeautifulSoup(response.text, "html.parser")
 quotes = soup.find_all(class_="quote")

#loop through quote
#build a list containg dictionary of text and authors"""	
 for quote in quotes:
    all_quotes.append({
    	"text": quote.find(class_="text").get_text(),
    	"authors": quote.find(class_="author").get_text(),
    	"links": quote.find("a")["href"]

    })
 next_button = soup.find(class_="next")
 url2 = next_button.find("a")["href"] if next_button else None 
 #sleep(2)	
 #uncomment sleep(2) to slow down scraping
print(all_quotes)    