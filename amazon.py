from selenium import webdriver

AMAZON = "https://www.amazon.co.jp/dp/B08GGF7M7B/?th=1"


driver = webdriver.Chrome("./chromedriver")
driver.get(AMAZON)

a = driver.find_element_by_class_name('a-button-input').text
print(a)

driver.close()
driver.quit()