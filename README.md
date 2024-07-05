績效指標公式參考：https://www.binance.com/en/support/faq/portfolio-performance-indicators-in-binance-futures-copy-trading-54aa6d3b43bc4f6eb4a3a6e3aea40acd

程式碼使用發法：
1.把要分析的檔案下載並放置於跟程式碼相同的資料夾以使用
例如本次檔案trades.json由github網站下載後放置於後端題目.py所在的資料夾

2.更改程式碼裡面的filenames為檔案的名稱
例如檔案名為trades.json則以這個做為新filenames

3.如果檔案格式不是json，則可將最上面的import改為相對應的檔案格式
	例如檔案格式是csv則可改為import csv

4.如果需要更改顯示的結果為小數點第n位則可更改最下面的print statement
	例如想要ROI結果為小數點後第三位，則可以把ROI print statement改為roi:.3f即可
