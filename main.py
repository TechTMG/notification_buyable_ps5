from selenium import webdriver
from time import sleep
from store import is_store_buyable
from discord import notify_discord


def determine_and_notify_if_ps5_is_available_for_purchase_at_each_site():
    if(check_is_buyable("amazon"):
        notify_discord('amazon')

    if(check_is_buyable("rakuten"):
        notify_discord('rakuten')

def check_is_buyable(store_name):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    is_buyable = is_store_buyable(driver, store_name)

    driver.close()
    driver.quit()
    return is_buyable

if __name__ == '__main__':
    determine_and_notify_if_ps5_is_available_for_purchase_at_each_site()
