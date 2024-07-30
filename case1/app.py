from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 創建 WebDriver 對象，並安裝最新的 ChromeDriver
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打開指定的網頁
wd.get("https://ithelp.ithome.com.tw/m/questions/")

# 根據 CLASS_NAME 找到所有具有 'qa-list' 類名的元素
elements = wd.find_elements(By.CLASS_NAME, 'qa-list')

# 遍歷所有找到的 'qa-list' 元素
for element in elements:
    # 在每個 'qa-list' 元素內找到所有 h3 標籤
    h3_elements = element.find_elements(By.TAG_NAME, 'h3')
    
    # 遍歷所有找到的 h3 標籤，並打印其文本內容
    for h3 in h3_elements:
        print(h3.text)

# 退出 WebDriver（程式結束後可選擇取消註解）
wd.quit()
