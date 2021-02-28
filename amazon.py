from selenium import webdriver
from time import sleep

# PS5商品ページ
AMAZON = "https://www.amazon.co.jp/dp/B08GGF7M7B/?th=1"
# テスト用商品ページ
# AMAZON = "https://www.amazon.co.jp/dp/B08GGGBKRQ/?th=1"


def is_buyable():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)


    driver.get(AMAZON)
    # デジタルエディション版のボタンをクリック
    driver.find_element_by_id("a-autoid-9-announce").click()
    sleep(1)
    a = driver.find_element_by_class_name('a-button-input').get_attribute("value")
    print(a)

    driver.close()
    driver.quit()

if __name__ == '__main__':
    is_buyable()
