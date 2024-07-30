from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 創建 WebDriver 對象，並安裝最新的 ChromeDriver
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 設置隱性等待時間，直到找到元素或超過設定時間（全域設定）
wd.implicitly_wait(10)

# 打開指定的網頁
wd.get("https://cdn2.byhy.net/files/selenium/test2.html")

# 確保找到具有指定 ID 的下拉選單元素
select_element = wd.find_element(By.ID, "ss_multi")

# 創建 Select 對象，用於操作下拉選單
select = Select(select_element)

# 清除下拉選單中的所有選項選擇（適用於多選下拉選單）
select.deselect_all()

# 根據顯示的文本選擇下拉選單中的選項
select.select_by_visible_text("小江老师")
select.select_by_visible_text("小雷老师")

# 等待用戶輸入，以便查看操作結果
input("Press any key to quit...")

# 退出 WebDriver，關閉所有窗口
wd.quit()
