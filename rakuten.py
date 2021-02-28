from selenium import webdriver
from time import sleep
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
RAKUTEN_URL = config_ini['SiteURL']['rakuten'] # PS5商品ページ

def is_rakuten_buyable():
    """
    楽天の商品扱い状況をcheckする

    確認中の商品扱い状況
        在庫あり, 予約受付中
        ご注文できない商品, 予約受付終了
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)


    driver.get(RAKUTEN_URL)

    # 商品取扱状況をテキスト取得
    buyable_status = driver.find_element_by_id('purchaseBox').text

    # '在庫あり'のとき'buyable', その他のとき空文字
    if "在庫あり" in buyable_status:
        is_buyable = "buyable"
    else:
        is_buyable = ""

    driver.close()
    driver.quit()
    return is_buyable

if __name__ == '__main__':
    is_rakuten_buyable()
