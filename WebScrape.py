from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.ca/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7708"

uClient = uReq(my_url)

# opens a connection with the webpage
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#grabs each coupon
containers = page_soup.findAll("div", {"class": "item-container"})

len(containers)

print(containers)
