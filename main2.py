#http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/

import pandas
from bs4 import BeautifulSoup
import requests
import numpy as np

price=[]
bed =[]
bath =[]
address = []
hood=[]
Neighborhood=[]
area=[]
borough=[]

urlbase = "https://www.renthop.com/search/nyc?max_price=50000&min_price=0&sort=hopscore&q=&search=0&page="

for i in range(1,1000):

    r = requests.get(urlbase+str(i))
    c=r.content
    soup = BeautifulSoup(c,"html.parser")
    listing = soup.find_all("div",{"class":"search-listing font-size-10 my-3 my-md-0 py-0 py-md-4"})

    for list in listing:
        #each inner listing box
        inner = list.find("div",{"class":"search-info pr-4 pl-4 pr-md-0 pl-md-4 py-2 py-md-0"})

        #address info
        try:
            address.append(inner.find("a").text)
        except:
            address.append('')
        #div with the Neighborhood
        try:
            hood.append(inner.find("div",{"class","font-size-9 overflow-ellipsis"}).text[1:-1])
        except:
            hood.append('')
        #table for price, bed, Baths

        table = inner.find_all("td")

        #handle an extra space?
        try:
            try:
                price.append(float(table[0].text[2:-1].replace(',','')))
            except:
                if '$' in table[0].text[2:-1].replace(',',''):
                    price.append(float(table[0].text[2:-1].replace(',','').replace('$','').strip()))
        except:
            price.append(np.nan)

        #handle studios as 0 bedrooms

        try:
            try:
                bed.append(int(table[1].text[2:3]))
            except:
                bed.append(0)
        except:
            bed.append(0)

        try:
            bath.append(float(table[2].text[1:2]))
        except:
            bath.append(0)
        #break out Neighborhoods into hood, area, borough

        temp = hood[-1]
        try:
            Neighborhood.append(temp.partition(',')[0].strip())
        except:
            Neighborhood.append('')

        try:
            area.append(temp.partition(',')[2].strip().partition(',')[0].strip())
        except:
            area.append('')
        #need to do this conditional to account for random listings having more than 1 area...


        if "Brooklyn" in temp:
            borough.append("Brooklyn")
        elif "Manhattan" in temp:
            borough.append("Manhattan")
        elif "Queens" in temp:
            borough.append("Queens")
        elif "Bronx" in temp:
            borough.append("Bronx")
        elif "Staten Island" in temp:
            borough.append("Staten Island")
        elif "Essex" in temp:
            borough.append("Manhattan")
        else:
            borough.append('')

print(len(address))
print(len(hood))
print(len(Neighborhood))
print(len(area))
print(len(borough))
print(len(price))
print(len(bath))
print(len(bed))

data = {'Address':address,'Full Location':hood,'Neighborhood':Neighborhood,'Area':area,'Borough':borough,'Price':price,'Baths':bath,'Beds':bed}

df = pandas.DataFrame(data,columns = ['Address','Full Location','Neighborhood','Area','Borough','Price','Baths','Beds'])

df.to_csv("NYC_Apts_Rental_Listing.csv")
