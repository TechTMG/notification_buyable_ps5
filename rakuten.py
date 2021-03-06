from selenium import webdriver
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
RAKUTEN_URL = config_ini['SiteURL']['rakuten']  # PS5商品ページ


def is_rakuten_buyable():
    """
    楽天の商品扱い状況をcheckする

    Returns:
        [str]: 商品があれば'buyable!'、なければ空文字
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver_rakuten = webdriver.Chrome(options=options)

    driver_rakuten.get(RAKUTEN_URL)

    # 商品取扱状況をテキスト取得
    buyable_status = driver_rakuten.find_element_by_id('purchaseBox').text

    # '買い物かごに入れる'ボタンが配置されているとき'buyable', その他のとき空文字
    if "買い物かごに入れる" in buyable_status:
        is_buyable = "buyable!"
    else:
        is_buyable = ""

    driver_rakuten.close()
    driver_rakuten.quit()
    return is_buyable


if __name__ == '__main__':
    is_rakuten_buyable()
