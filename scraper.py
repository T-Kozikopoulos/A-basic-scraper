import requests
from bs4 import BeautifulSoup


page_number = 1
# There are 30 results per page.
how_many_pages = 5

for page_number in range(how_many_pages):
    # Looking for coffee shops in LA.
    url = "https://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=lost%20angeles&page={}".format(page_number)

    # Get the page's source code.
    r = requests.get(url)

    # Make a soup object so we can use the soup methods.
    soup = BeautifulSoup(r.content, 'html.parser')
    data = soup.findAll('div', {'class': 'info'})

    for item in data:
        # Specify even further with .findAll again.
        try:
            # Print out the name of the store.
            print(item.contents[0].findAll('span', {'itemprop': 'name'})[0].text)
        except Exception as e:
            print(e)
        try:
            # Print out the address of the store.
            print("Address: " + item.contents[1].findAll('span', {'class': 'street-address'})[0].text)
        except Exception as e:
            print(e)
        try:
            # Print out the phone number of the store.
            print("Phone: " + item.contents[1].findAll('div', {'class': 'phones phone primary'})[0].text)
        except Exception as e:
            print(e)
    # Move on to the next page of results.
    page_number += 1
