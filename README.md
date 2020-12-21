# AIoT 期末報告
## 說明
- dataset\solar_data_202003_202007.csv 為 <strong>新竹市北區海濱路240號</stong> 新竹市環保局掩埋場復育地太陽能案場中在 <strong>3月至7月</strong> 其中一個inverter(逆變器)的太陽能發電資料

將資料集(dataset)內的 solar_data_202003_202007.csv 的太陽能案場發電資料做為訓練資料集訓練你的預測模型，預測 2020年一月、二月、八月、九月、十月的 <strong>發電度數</strong> 。

訓練完後需將模型做成 restful API 按照以下格式接收並回傳資料，restful API 需開啟對外連線的功能，可自行架設或直接使用 ngrok。

#### [作業網址: http://aiotfinal.ddns.net:8000/ ](http://aiotfinal.ddns.net:8000/)