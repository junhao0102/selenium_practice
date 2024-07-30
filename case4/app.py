from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 創建 WebDriver 對象，並安裝最新的 ChromeDriver
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 設置隱性等待時間，直到找到元素或超過設定時間（全域設定）
wd.implicitly_wait(10)

# 打開指定的網頁
wd.get(
    "https://www.google.com/search?gs_ssp=eJzj4tVP1zc0LCmqNLaosigyYPTif75gy9PF856vanw2uevlrC4AzAAPOg&q=%E7%A0%B4%E5%A3%9E%E7%AA%81%E6%93%8A%E9%9A%8A&rlz=1C1GCEU_zh-TWTW1097TW1098&oq=&gs_lcrp=EgZjaHJvbWUqCQgDEC4YJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQLhgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQkyMDQ3ajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8"
)

# 儲存當前窗口的句柄
mainWindow = wd.current_window_handle

try:
    # 使用 CSS 選擇器找到包含特定 href 的連結元素
    element = wd.find_element(
        By.CSS_SELECTOR, 'a[href="https://forum.gamer.com.tw/B.php?bsn=76786"]'
    )
    
    # 獲取 href 屬性值
    link = element.get_attribute("href")

    # 使用 JavaScript 在新標籤頁中打開連結
    wd.execute_script(f"window.open('{link}', '_blank');")

    # 切換到新標籤頁，-1 表示最後一個標籤頁
    wd.switch_to.window(wd.window_handles[-1])

    # 等待2秒
    time.sleep(2)

    print("成功點擊連結")
except Exception as e:
    print("找不到連結", e)

# 切換回主窗口
wd.switch_to.window(mainWindow)

# 等待2秒
time.sleep(2)

# 等待用戶輸入，以便查看操作結果
input("Press any key to quit...")

# 退出 WebDriver，關閉所有窗口
wd.quit()
