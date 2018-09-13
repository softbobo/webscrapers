#rebuild from python webscrapingtutorial at https://youtu.be/XQgXKtPSzUI
#softbobo on 13/09/2018

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#opening up connection, grabbing the page
uClient = uReq(my_url)

#load cintent into variable
page_html = uClient.read()

#close page
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")


#find all the containers, holding the info for each gfx card
containers = page_soup.findAll('div', {'class':'item-container'})

#output to .csv file
filename = 'products.csv'
#'w' to write into file
f  = open(filename, 'w')
#headers of .csv, \n makes a newline
headers = 'brands, product_name, shipping\n'

f.write(headers)

#iterate through all the containers to grab brands of cards
for container in containers:
    brands = container.div.div.a.img["title"]
    #iterate through the titles of the cards
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    #iterate through shipping cost of each item; strip gives back just text string and removes all white spaces before and after 
    shipping_container = container.findAll('li', {'class':'price-ship'})
    shipping = shipping_container[0].text.strip()
    
    print(brands)
    print(product_name)    
    print(shipping)

    #write results to .csv, 'replace' replaces one item in a string with another
    f.write(brands + ',' + product_name.replace(',', '|') + ',' + shipping + '\n')

f.close()    