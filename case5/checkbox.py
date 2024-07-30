from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 創建 WebDriver 對象，並安裝最新的 ChromeDriver
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 設置隱性等待時間，直到找到元素或超過設定時間（全域設定）
wd.implicitly_wait(10)

# 打開指定的網頁
wd.get("https://cdn2.byhy.net/files/selenium/test2.html")

# 使用 CSS 選擇器找到所有預設選中的複選框元素
elements = wd.find_elements(By.CSS_SELECTOR, "input[type='checkbox'][checked='checked']")

# 迭代每個選中的複選框元素
for element in elements:
    print(f"當前的值 : {element.get_attribute('value')}")
    
    # 點擊該複選框以取消選中
    element.click()

# 使用 CSS 選擇器找到特定值的複選框元素
element = wd.find_element(By.CSS_SELECTOR, "#s_checkbox input[value='小雷老师']")

# 點擊該複選框以選中
element.click()

# 等待用戶輸入，以便查看操作結果
input("Press any key to quit...")

# 退出 WebDriver，關閉所有窗口
wd.quit()
