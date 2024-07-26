from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import os
import requests

# 設置下載目錄
download_dir = os.path.join(os.getcwd(), "download")

# 確保下載目錄存在
os.makedirs(download_dir, exist_ok=True) 

# # 設置 Chrome 選項以處理下載
chrome_options = Options()
chrome_options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": download_dir,  # 設置下載目錄
        "download.prompt_for_download": False,  # 禁用下載提示
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
)
# 創建 WebDriver 對象，並安裝最新的 ChromeDriver
wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 設置隱性等待時間，直到找到元素或超過設定時間
wd.implicitly_wait(10)

# 打開指定的網頁
wd.get("https://www.google.com/")

# 根據 ID 找到圖片元素
element = wd.find_element(By.ID, "hplogo")

# 獲取圖片的 URL
image_url = element.get_attribute("src")

# 獲取圖片名字
image_name = element.get_attribute("alt")

# 使用 requests 下載圖片
response = requests.get(image_url, stream=True)

# 設定圖片儲存的路徑
image_path = os.path.join(download_dir, f"{image_name}.gif")

# 保存圖片到指定路徑
with open(image_path, "wb") as file:
    for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)

# 退出 WebDriver，關閉所有窗口
wd.quit()
