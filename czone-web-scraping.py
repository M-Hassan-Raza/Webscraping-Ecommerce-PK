from bs4 import BeautifulSoup
import requests
import time


url = ""
max_price = 0


with open('Scraping_Info.txt', 'r') as f:
    url = f.readline().strip('\n')
    max_price = float(f.readline().strip('\n'))
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "lxml")

if(url.find("czone") != -1):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "lxml")

    availabilty = doc.find('span', class_="product-data",
                           id="spnStockStatus").string
    product_name = doc.find('h1', class_="product-title",
                            id="spnProductName").string

    if(availabilty == "In Stock"):
        final_price = doc.find(
            'span', class_="price-sales", id="spnCurrentPrice")
        final_price_string = final_price.string
        remove_currency = final_price_string.replace("Rs.", "")
        remove_comma = remove_currency.replace(",", "")
        final_price_float = float(remove_comma)

        if(final_price_float <= max_price):
            print(f"{product_name} is up for grabs!!!")
            time.sleep(5)
            quit()
        else:
            print(f"{product_name} NOT available at the selected Price Range")
            time.sleep(2)
            quit()

    elif(availabilty == "Out of Stock"):
        print(f"{product_name} is out of stock :(")
        time.sleep(2)
        quit()

    else:
        print("Error while loading the wabpage, try again and hope it works :)")
        time.sleep(2)
        quit()
else:
    print("Invalid Link. Please ensure that the link inside Scraping_Info.txt is valid.")
    time.sleep(2)
    quit()
