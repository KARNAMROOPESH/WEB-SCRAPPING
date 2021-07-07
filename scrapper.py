import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

DATAURL = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'

browser = webdriver.Chrome("chromedriver")
browser.get(DATAURL)

time.sleep(10)

def scrap():
    headers = ["name","ligth_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]

    planetdata = [ ]

    for i in range(1,444):
        soup = BeautifulSoup(browser.page_source , "html.parser")

        for ultag in soup.find_all("ul" , attrs={"class","exoplanet"}):
            litags = ultag.find_all("li")
            temp=[ ]
            for index,litag in enumerate(litags):
                if index == 0:
                    temp.append(litag.find_all("a")[0].contents[0])
                else :
                    try:
                        temp.append(litag.contents[0])
                    except:
                        temp.append(" ")
                    
            planetdata.append(temp)

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

    with open("data.csv","w")as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(planetdata)


scrap()

    



