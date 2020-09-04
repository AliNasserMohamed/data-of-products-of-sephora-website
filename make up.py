from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
option = Options()
csv_file=open("makeup.csv","w",encoding="utf-8")
writer=csv.writer(csv_file)
writer.writerow(["brand","product","price","image of the product"])
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(chrome_options=option, executable_path=path)
driver.get("https://www.sephora.com/shop/makeup-cosmetics")
time.sleep(10)
sections=driver.find_elements_by_class_name("css-1ms0vuh.e65zztl0")
for section in sections:
    section.click()
    print("section is clicked")

    soup = BeautifulSoup(driver.page_source, "lxml")
    elements = soup.findAll("div", class_="css-1tayj8e")
    if len(elements)>0:

        for element in elements:
            row=[]
            brand = element.find("span", class_="css-182j26q").text
            product = element.find("span", class_="css-pelz90").text
            price = element.find("span", class_="css-5fq4jh")
            img=element.find("img")
            if price is None:
                price=element.find("span", class_="css-0")
            print(brand)
            row.append(brand)
            row.append(product)
            row.append(price.text)
            if img:
              row.append(("https://www.sephora.com"+img["src"]))
            writer.writerow(row)
    else:continue

