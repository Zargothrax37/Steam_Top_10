from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup()

website = requests.get("https://store.steampowered.com/search/?category1=998&os=win&supportedlang=english&hidef2p=1&filter=topsellers&ndl=1").text

# Gets the Title, price and link to the top 50 games and adds them to a list

game_title = []
game_link = []
game_price = []
game_link_cleaned = game_link[0:50]

soup = BeautifulSoup(website, "html.parser")
title_results = soup.find_all(class_="title")
links_results = soup.find_all(id="search_result_container")
price_result = soup.find_all(class_="discount_final_price")

for name in range(len(title_results)):
    game_title.append(title_results[name].getText())

for link in links_results[0].find_all("a"):
    game_link.append(link.get("href"))

for price in range(len(price_result)):
    game_price.append(price_result[price].getText())

# Opens google forms and allows us to fill in the information from beatifullsoup


for i in range(10):

    driver = webdriver.Chrome()
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSezJquoAXH3gjOIrw4R-N4bzNzCrp2RUNBT3tjvyE2qq-RTVw/viewform?usp=sf_link")

    name = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    driver.set_script_timeout(time_to_wait=1)
    name.click()
    name.send_keys(game_title[i])

    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    driver.set_script_timeout(time_to_wait=1)
    price.click()
    price.send_keys(game_price[i])

    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    driver.set_script_timeout(time_to_wait=1)
    link.click()
    link.send_keys(game_link[i])

    send = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    send.click()