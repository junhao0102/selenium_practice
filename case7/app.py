from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# 創建 WebDriver 對象，並安裝最新的 ChromeDriver
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 設置隱性等待時間
wd.implicitly_wait(10)

# 打開指定的網頁
wd.get("https://cdn2.byhy.net/files/selenium/test4.html")

# 點擊觸發 alert 的按鈕
element = wd.find_element(By.ID, "b1")
element.click() 

# 處理 alert 框
print(wd.switch_to.alert.text)
wd.switch_to.alert.accept()

# 點擊觸發 confirm 的按鈕
element = wd.find_element(By.ID, "b2")
element.click()

# 處理 confirm 框
print(wd.switch_to.alert.text)
wd.switch_to.alert.dismiss()

# 點擊觸發 prompt 的按鈕
element = wd.find_element(By.ID, "b3")
element.click()

# 使用顯式等待確保 prompt 框已經出現
WebDriverWait(wd, 10).until(EC.alert_is_present())

# 處理 prompt 框
alert = wd.switch_to.alert
print(alert.text)

# 輸入文本並提交
alert.send_keys("Hello World!")
alert.accept()

# 等待用戶輸入，以便查看操作結果
input("Press any key to quit...")

# 退出 WebDriver，關閉所有窗口
wd.quit()
