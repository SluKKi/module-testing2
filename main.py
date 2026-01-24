from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.python.org")
main_window = driver.current_window_handle
print("main window", main_window)
driver.execute_script("window.open('https://google.com', '_blank'); ")
all_win = driver.window_handles
print("все вкладки", all_win)
print("kol-vo", len(all_win))
new_win = all_win[-1]
driver.switch_to.window(new_win)
print("now we are here", driver.current_url)
print("name of second win", driver.title)
driver.close()
driver.switch_to.window(main_window)
driver.quit()

