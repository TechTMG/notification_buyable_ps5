from selenium import webdriver
from time import sleep
import configparser


config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

buyable = "buyable"
un_buyable = ""
diff_page = ""

def is_store_buyable(driver, store_name):
    """
    該当商品のページを開いているかcheckする
    開いていた場合に注文可能かcheckする

    Returns:
        [str]:  商品がある buyable
                商品がない un_buyable
                開いているページが該当商品ではない diff_page
    """

    STORE_ITEM = config_ini['StoreItem'][store_name]
    STORE_URL = config_ini['SiteURL'][store_name]
    STORE_ELEMENT = config_ini['OrderElement'][store_name]
    STORE_WORD = config_ini['OrderWord'][store_name]
    
    driver.get(STORE_URL)

    page_title = "".join(driver.title.split())
    
    if STORE_ITEM not in page_title:
        is_buyable = diff_page
    else:
        order_html = driver.find_element_by_id(STORE_ELEMENT).text
        if STORE_WORD in order_html:
            is_buyable = buyable
        else:
            is_buyable = un_buyable
    return is_buyable

if __name__ == '__main__':
    is_amazon_buyable()
