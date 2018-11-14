import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
  
#Blank list for further use"""
url1 = "http://quotes.toscrape.com/"


def scrap_quotes():

    url2 = "/page/1/"
    all_quotes = []
    while url2:

        response = requests.get(f"{url1}{url2}")
        print(f"Scraping {url1}{url2}......")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")

#loop through quote and build a list containg dictionary of text and authors	
        for quote in quotes:
	        all_quotes.append({"text": quote.find(class_="text").get_text(), "authors": quote.find(class_="author").get_text(),"links": quote.find("a")["href"]})
        next_button = soup.find(class_="next")
        url2 = next_button.find("a")["href"] if next_button else None 
    return all_quotes	 
#sleep(2)	
#uncomment sleep(2) to slow down scraping
#Adding game logic
def start_game(scrapeQuotes):
    quote = choice(scrapeQuotes)
    print(f"\n>>>Here's the Quote:\n{quote['text']} ")
    print(quote["authors"])
    guess = ''
    Remaining_Guesses = 4
    while guess.lower() != quote["authors"].lower() and Remaining_Guesses > 0:
	    guess = input(f"Who is author of this QUOTE ? \n Guesses Remaining: {Remaining_Guesses}\n")
	    Remaining_Guesses -= 1
	    if guess == quote["authors"]:
	        print("Your guess is right!  !")
	        break  
        if Remaining_Guesses == 3:
          	print(f"Hint No. 1, author was born in {Date_of_birth} {Place_of_birth}.")
            res = requests.get(f"{url1}{quote['links']}")
            soup = BeautifulSoup(res.text, "html.parser")
            Date_of_birth = soup.find(class_="author-born-date").get_text()
            Place_of_birth = soup.find(class_ = "author-born-location").get_text()
            print(f"Hint No. 1, author was born in {Date_of_birth} {Place_of_birth}.")
        elif Remaining_Guesses == 2:
            First_initial = quote["authors"][0]
            print(f"Hint No. 2, author's first name initial is: {First_initial}")
        elif Remaining_Guesses == 1:
            Last_initial = quote["authors"].split(" ")
            print(f"Hint No. 3, author's last name initial is: {Last_initial[1][0]}")   
        else :
            print(f"Sorry all the guesses were wrong!!!\nAnswer is: {quote['authors']}")   	
    print("out") 
    Play_again = ''
    while Play_again.lower() not in ('y', 'yes', 'n', 'no'):

        Play_again= input("Do you want to play again ?{y/n}")
        if Play_again.lower() in ('y', 'yes'):
            return start_game(scrapeQuotes)
        else:
            print("GOODBYE!!")


scrapeQuotes = scrap_quotes() 
start_game(scrapeQuotes)
 

print("out of loop")	