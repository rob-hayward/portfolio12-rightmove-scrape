import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=POSTCODE%5E1384006&insId=1&radius=1.0&minPrice=550000&maxPrice=1000000&minBedrooms=3&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false#prop133677107'


def scrape_property_listings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    property_listings = []

    for listing in soup.find_all("div", class_="propertyCard"):
        try:
            title = listing.find("h2", class_="propertyCard-title").text.strip()
            address = listing.find("address", class_="propertyCard-address").text.strip()
            price = listing.find("div", class_="propertyCard-price").text.strip()
            property_listings.append((title, address, price))
        except AttributeError:
            continue

    return property_listings


property_listings = scrape_property_listings(url)


with open("property_listings.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Address", "Price"])
    writer.writerows(property_listings)
