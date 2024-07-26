from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 創建 WebDriver 對象，並安裝最新的 ChromeDriver
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 隱性等待，直到找到元素或超過設定時間（全域設定）
wd.implicitly_wait(10)

# 打開指定的網頁
wd.get("https://www.byhy.net/_files/stock1.html")

# 根據 ID 找到輸入框元素
input_element = wd.find_element(By.ID, "kw")

# 在輸入框中輸入文字
input_element.send_keys("航空")

# 獲取輸入框中的文字
input_value = input_element.get_attribute("value")
print(input_value)

# 根據 ID 找到搜尋按鈕元素
search_button = wd.find_element(By.ID, "go")

# 點擊搜尋按鈕
search_button.click()

# 根據 CLASS_NAME 找到所有符合條件的結果項目
result_elements = wd.find_elements(By.CLASS_NAME, "result-item")

# 遍歷每個結果項目並打印 p 標籤中的文本內容
for result in result_elements:
    title_element = result.find_element(By.TAG_NAME, "p")
    print(title_element.text)

# 清空輸入框中的文字
input_element.clear()

# 在輸入框中輸入新的文字
input_element.send_keys("科技")

# 點擊搜尋按鈕
search_button.click()

# 根據 CSS 選擇器找到所有符合條件的結果項目 
result_elements = wd.find_elements(By.CSS_SELECTOR, ".search-result>div")

# 遍歷每個結果項目並打印 p 標籤中的文本內容
for results in result_elements:
    print(results.find_element(By.TAG_NAME, "p").text)
        
# 退出 WebDriver，關閉所有窗口
wd.quit()
