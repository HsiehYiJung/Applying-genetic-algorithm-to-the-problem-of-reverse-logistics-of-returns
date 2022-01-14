
# Applying-genetic-algorithm-to-the-problem-of-reverse-logistics-of-returns

Introduction
網購盛行，許多業者都無實體店面，因此在售後服務方面皆仰賴物流。
產品退貨被視為開展業務不可避免的成本，透過產品退貨的最佳處理可以成為競爭優勢，因為公司可以節省大量與產品退貨相關的運輸、庫存和倉儲成本

Key paper 研究貢獻：
本文建立了一個數學模型及其求解過程，可以優化，創建連接初始收集點、集中退貨中心和製造的逆向物流網絡設施。以往維修都需親自送回供應商，此論文討論利用中間服務中心結合售後服務，減少人力跟資源的浪費。
檢視以下三點：
1.運用在現有/新設施最佳位置/分配
2.用於翻新和再製造的退貨產品的分配
3.將現有工廠和倉庫的容量擴展，以促進再製造和維修服務
問題簡化：
•	將key paper 中的限制式設定為非線性、離散的問題
•	以整體成本最小化、退貨中心選址為首要目標

目標函數為整體最小成本
限制式考慮產品分發、產能限制、倉庫容量等，考慮潛在場址位置、成本等，最佳化後產生最佳解。

基因演算法
GA演算法的基本步驟如下：

Step 1. 種群初始化。選擇一種編碼方案然後在解空間內通過隨機生成的方式初始化一定數量的個體構成GA的種群。
Step 2. 評估種群。利用啟發式演算法對種群中的個體（矩形件的排入順序）生成排樣圖並依此計算個體的適應函式值（利用率），然後儲存當前種群中的最優個體作為搜尋到的最優解。
Step 3. 選擇操作。根據種群中個體的適應度的大小，通過輪盤賭或者期望值方法，將適應度高的個體從當前種群中選擇出來。
Step 4. 交叉操作。將上一步驟選擇的個體，用一定的概率閥值Pc控制是否利用單點交叉、多點交叉或者其他交叉方式生成新的交叉個體。
Step 5. 變異操作。用一定的概率閥值Pm控制是否對個體的部分基因執行單點變異或多點變異。
Step 6. 終止判斷。若滿足終止條件，則終止演算法，否則返回Step 2。

一條染色體代表每個解解決方案的初始解決方案集（總體）。的大小人口取決於手頭問題的規模和性質。染色體通過交叉進化算子和變異算子來產生孩子，改進當前的解決方案集。染色體然後通過適應度函數評估種群中的染色體，並將不太適合的染色體替換為更好的染色體


Model design
本研究要解決的問題是：
1. 以這種方式定位初始收集點在哪裡?從現有和潛在的旅行時間（或距離）
客戶到收集點是否最小化？
2.集中退貨中心在哪裡設置方式，最初收集之間的轉運費用點和製造（或維修設施）的位置是最小化？
3、如何構建逆向物流網絡，可以在初始時間之間進行及時取件
收集點和集中退貨中心？考慮到服務時間規定，初始收集點應在特定小時內
從最近的集中返回中心的行駛時間。
4. 初次收集時退回產品的頻率點應合併以最小化運輸成本，同時避免了退貨過程中的延誤？
5、初始收款點多少，集中歸還需要中心來最大限度地減少與產品退貨相關的客戶麻煩，同時最大限度地降低成本處理退貨？

![圖片1](https://user-images.githubusercontent.com/97608894/149436577-989a8709-0002-472b-961e-f5de9007f51a.png)

![圖片2](https://user-images.githubusercontent.com/97608894/149436791-05118265-1dac-48b0-8532-7d04d3d3976c.png)

![圖片4](https://user-images.githubusercontent.com/97608894/149436918-10fc31db-db29-43f5-9280-0a272ce1cad8.png)

![圖片3](https://user-images.githubusercontent.com/97608894/149436933-e3d3993c-7f64-4beb-952f-18b0c83750e6.png)

