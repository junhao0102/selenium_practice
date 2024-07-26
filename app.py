from selenium import webdriver
## BY: 也就是依照條件尋找元素中XPATH、CLASS NAME、ID、CSS選擇器等都會用到的Library
from selenium.webdriver.common.by import By
## keys: 鍵盤相關的Library
from selenium.webdriver.common.keys import Keys
## Select: 下拉選單相關支援，但前端框架UI工具不適用(ex: Quasar、ElementUI、Bootstrap)
from selenium.webdriver.support.ui import Select
## WebDriverWait: 等待頁面加載完成的顯性等待機制Library
from selenium.webdriver.support.ui import WebDriverWait
## ActionChains: 滑鼠事件相關
from selenium.webdriver.common.action_chains import ActionChains
## expected_conditions: 條件相關
from selenium.webdriver.support import expected_conditions as EC
## BeautifulReport: 產生自動測試報告套件
from BeautifulReport import BeautifulReport
## Chrome WebDriver 需要DRIVER Manager的支援
from webdriver_manager.chrome import ChromeDriverManager
## 延遲時間相關
import time
## 單元測試模組，線性測試用不到
import unittest



## 這串設定是防止瀏覽器上頭顯示「Chrome正受自動控制」
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

## 關閉自動記住密碼的提示彈窗
options.add_experimental_option("prefs", {
                                "profile.password_manager_enabled": False, "credentials_enable_service": False
                                })



class Test(unittest.TestCase):
    @classmethod
    ## setUpClass這邊的設定是，可以讓所有Case進行過程中只開啟一次瀏覽器
    ## 執行時會依照這個順序循環一次 setUpClass > test > teardown
    ## self則是作為我們的區域參數來定義作用域
    def setUpClass(self):
        ## 定義WebDriver以及ActionsChain的變數便於後頭應用        
        self.driver = webdriver.Chrome(chrome_options=options)
        self.action = ActionChains(self.driver)
        ## 開啟Chrome新視窗，前往Youtube網址並最大化視窗
        self.URL = "https://youtube.com"
        self.driver.get(self.URL)
        self.driver.maximize_window()
    
    @classmethod
    def tearDownClass(self):
        ## 所有case跑完後就退出瀏覽器
        self.driver.quit()
        
    ## Test Case 的命名方式務必以「test_01_* ~ test_99_*」為主，讓爬蟲依照順序走
    ## """裡面的註解就是報表產生後的CASE描述文字。
    def test_01_search(self):
        """
        前往Youtube網站後，搜尋Gura的影片
        """
        time.sleep(2)
        ## 等待頁面中的HTML，ID = 'search'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='search']"))
            )
        finally:
            time.sleep(2)
        ## 找到搜尋框的XPATH並且輸入'Gawr Gura 熟肉' 熟肉就是經過別人得到版權方同意，翻譯上傳過後的剪輯
        ## 寫法上也通driver.find_element(By.XPATH, '//xxx')
        input_search = self.driver.find_element_by_xpath("//input[@id='search']")
        input_search.send_keys("Gawr Gura 熟肉")
        ## 找到搜尋按鈕後按下
        button_search = self.driver.find_element_by_id("search-icon-legacy")
        button_search.click()
    
    def test_02_open_target(self):
        """
        在搜尋結果找到特定的影片並點進去
        """
        time.sleep(5)
        ## 滾動網頁往下拉
        self.driver.execute_script("window.scrollBy(0,1200)")
        time.sleep(2)

        ## 隨便找一個影片的連結，利用XPATH找路徑
        youtube_target = self.driver.find_element_by_xpath("//a[@href='/watch?v=9SfsF_6fY9c']")
        youtube_target.click()
        time.sleep(5)
        
    def test_03_back_to_list(self):
        """
        回上頁列表，重新整理網頁後，切換另一則影片，五秒後回到首頁
        """
        self.driver.back()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(3)
        ## 注意，youtube可能因為你所在位置而針對搜尋結果作排序
        ## 如果你發現突然跳出case導致失敗，很有可能是因為搜尋列表找不到影片
        ## 將影片的 /watch?v=xxxxx替換成該搜尋結果中的任一連結即可
        youtube_target = self.driver.find_element_by_xpath("//a[@href='/watch?v=MhVh01k_Wg0']")
        youtube_target.click()
        time.sleep(5)
        logo = self.driver.find_element_by_id("logo-icon")
        logo.click()
        time.sleep(5)
    
    
