import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url_form = "https://forms.gle/H9zLDp9qZKYStr7XA"
zillow_clone_url = "https://appbrewery.github.io/Zillow-Clone"

zillow_clone_web = requests.get(zillow_clone_url).text
soup = BeautifulSoup(zillow_clone_web, "html.parser")
links = [link.get("href") for link in
         soup.select(selector="a.property-card-link")]
prices = [link.getText().split()[0].replace("+", "").replace("/mo", "")
          for link in soup.select(selector="div.PropertyCardWrapper span")]
addresses = [link.getText().replace(" | ", " ").strip()
             for link in soup.select(selector="a.StyledPropertyCardDataArea-anchor address")]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for i in range(len(links)):
    driver.get(url_form)
    sleep(2)
    path_address = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    address_input = driver.find_element(By.XPATH, value=path_address)
    address_input.send_keys(addresses[i])
    path_price = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    price_input = driver.find_element(By.XPATH, value=path_price)
    price_input.send_keys(prices[i])
    path_link = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    link_input = driver.find_element(By.XPATH, value=path_link)
    link_input.send_keys(links[i])
    path_button_send = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    button_send = driver.find_element(By.XPATH, value=path_button_send)
    button_send.click()

driver.quit()
