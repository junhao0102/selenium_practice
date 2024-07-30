from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 創建 WebDriver 對象，並安裝最新的 ChromeDriver
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 設置隱性等待時間
wd.implicitly_wait(10)

# 打開指定的網頁
wd.get("https://www.baidu.com/")

# 創建 ActionChains 對象
ac = ActionChains(wd)

# 使用顯式等待確保元素可見
element = WebDriverWait(wd, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[name="tj_briicon"]'))
)

# 使用 ActionChains 將滑鼠懸停在目標元素上
ac.move_to_element(element).perform()

# 等待用戶輸入，以便查看操作結果
input("Press any key to quit...")

# 退出 WebDriver，關閉所有窗口
wd.quit()
