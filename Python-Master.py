from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.walmart.ca/en/n-11+31+32?icid=home%20page_CT_WMS_HP-RollbackClearance_20181018_E_CategoryTile_Standard"

uClient = uReq(my_url)

# opens a connection with the webpage
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#grabs each coupon
containers = page_soup.findAll("div", {"id": "shelf-thumbs"})

len(containers)

print(containers)
