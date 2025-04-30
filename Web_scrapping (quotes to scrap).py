import requests
from bs4 import BeautifulSoup


base_url = "http://quotes.toscrape.com/page/{}/"

def scrape_page(page_number):
    url = base_url.format(page_number)
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_number}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    page_quotes = []
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = [tag.text for tag in quote.find_all("a", class_="tag")]

        page_quotes.append({"quote": text, "author": author, "tags": tags})
    
    return page_quotes

def display_quotes(max_pages=5):
    all_quotes = []
    
    
    for page in range(1, max_pages + 1):
        print(f"Scraping page {page}...")
        quotes_on_page = scrape_page(page)
        if not quotes_on_page:
            break
        all_quotes.extend(quotes_on_page)

    
    for quote in all_quotes:
        print(f"\nQuote: {quote['quote']}\n")
        print(f"Author: {quote['author']}\n")
        print(f"Tags: {', '.join(quote['tags'])}\n\n")
        
        user_input = input("Do you want to see the next quote? (yes/no): ").strip().lower()
        if user_input != "yes":
            
            print("Thank You For Reading!")
            break

# Display the quotes
display_quotes(max_pages=5)
