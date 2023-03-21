# OpenAI 電子信件產生器

這是一個簡單的 Flask 應用程式，使用 OpenAI 的 GPT-3 語言模型生成信件內容。

使用者可以輸入寄件人、收件人和信件主題，應用程式會使用這些輸入生成信件內容。

## 需求
1. Python 3
2. Flask
3. OpenAI API 套件
4. OpenAI API keys

## 使用方法

1. Clone專案到本地：

    `git clone https://github.com/eeasonsun/emailtempv3.git`

2. 進入專案目錄： 

    `cd emailtempv3`

3. 安裝依賴項： 

    `pip install -r requirements.txt`

4. 創建 .env 檔案並將 OpenAI API 金鑰存入其中：

    `OPENAI_API_KEY=<your-openai-api-key>`

5. 運行 Flask 應用程式： 

    `python app.py`

6. 在網頁瀏覽器中訪問應用程式： 

    http://localhost:5000/


## 工作原理

Flask 應用程式創建了一個表單，**用戶可以在其中輸入寄件人、收件人和信件主題**。

提交後，應用程式會向 OpenAI API 發送一個請求，其中包括輸入值的提示。**API 會回覆一個生成的文本**，然後在網頁上顯示該文本。

在運行應用程式之前，OpenAI API 金鑰應設置為環境變量。

可以至 OpenAI 網站（https://platform.openai.com） 申請Paid Account獲取API keys。


## 其他

此應用程式生成的信件內容**不全然符合條件**，仍需要進行編輯或審查才能適合實際使用。或是可以自行調整max_token、n、temperatures參數。

此專案的code實驗由GPT-4建立，並由作者進行微調。有任何錯誤或建議歡迎給予指正！