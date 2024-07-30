## ActionChains

- **點擊滑鼠右鍵**: `context_click()`
- **雙擊滑鼠左鍵**: `double_click()`
- **按著滑鼠左鍵不放**: `click_and_hold()`
- **放開滑鼠左鍵**: `release()`
- **拖曳到某個元素後放開**: `drag_and_drop(source, target)`
- **拖曳到某個座標後放開**: `drag_and_drop_by_offset(source, xoffset, yoffset)`
- **按下鍵盤上某個按鍵**: `key_down(value)`
- **放開鍵盤上某個按鍵**: `key_up(value)`
- **滑鼠指標從當前位置移動到某個座標**: `move_by_offset(xoffset, yoffset)`
- **滑鼠指標移動到某個元素**: `move_to_element(to_element)`
- **移動到某元素附近座標位置**: `move_to_element_with_offset(to_element, xoffset, yoffset)`
- **執行當前這個 ActionChain 的動作**: `perform()`
- **在元素上輸入值 (例如: input)**: `send_keys(value)`
- **在指定的元素上輸入值**: `send_keys_to_element(element, value)`

## CSS 

| 選擇器類型 | 語法 | 說明 |
|------------|------|------|
| 標籤（TAG） | `div` | 選擇所有 `<div>` 元素 |
| ID | `#myId` | 選擇 ID 為 "myId" 的元素 |
| Class | `.myClass` | 選擇所有 class 為 "myClass" 的元素 |
| 屬性（attribute） | `input[name='username']` | 選擇 name 屬性為 'username' 的 input 元素 |
| 組合用法 | `input[name='username']` | 同上，選擇 name 屬性為 'username' 的 input 元素 |
| 子元素 | `div > p` | 選擇作為 `<div>` 直接子元素的所有 `<p>` 元素 |
| 後代元素 | `div p` | 選擇所有在 `<div>` 內的 `<p>` 元素，不論層級 |

## XPath

| XPath 類型 | 語法 | 說明 |
|------------|------|------|
| 絕對路徑 | `/html/body/div` | 從文檔根選擇特定路徑的元素 |
| 相對路徑 | `//div` | 選擇文檔中所有的 `<div>` 元素 |
| 包含文本 | `//button[text()='Click me']` | 選擇文本為 'Click me' 的按鈕 |
| 包含屬性 | `//input[@name='username']` | 選擇 name 屬性為 'username' 的 input 元素 |
| 包含類 | `//*[contains(@class, 'submit-button')]` | 選擇 class 包含 'submit-button' 的所有元素 |
| 組合條件 | `//button[@type='submit' and @name='login']` | 選擇 type 為 'submit' 且 name 為 'login' 的按鈕 |