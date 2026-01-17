from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
edge_options = Options()
driver = webdriver.Edge(options=edge_options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
try:
    driver.get("https://yandex.ru")
    print("Заголовок страницы: ", driver.title)
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "text"))
    )
    search_box.clear()
    search_box.send_keys("Selenium Edge Python/n")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".serp-item"))
    )
    print("Поиск успешно выполнен")
except Exception as e:
    print("0: ", str(e))
    driver.save_screenshot("error.png")
    print("Ошибка сохранена в скриншоте")
    driver.quit()
finally:
    driver.quit()