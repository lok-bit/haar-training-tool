# 開啟 info.txt，讀取原始的標註資料（正樣本）
fp = open('Haar-Training_carPlate/training/positive/info.txt', 'r')
line = fp.readline()

rettext = ''  # 用來儲存轉換後的所有標註資訊
print('開始轉換圖框! ')

# 一行一行讀取標註檔
while line:
    data = line.split(' ')  # 拆解欄位：檔名、物件數、x y w h ...
    n = data[1]             # 這行的物件數量（通常為 1）

    # 建立新的標註格式：圖檔名 + 物件數量
    rettext += data[0] + ' ' + n + ' '

    # 對每個標註框做處理
    for i in range(int(n)):
        x = float(data[2 + i*4])  # 原始 x 座標
        y = float(data[3 + i*4])  # 原始 y 座標
        w = float(data[4 + i*4])  # 原始寬度
        h = float(data[5 + i*4])  # 原始高度

        # 如果寬高比小於 3.5（太窄），就調整寬度讓車牌比例變成 3.5（長型）
        if (w / h) < 3.5:
            newW = h * 3.5                 # 計算新的寬度
            x -= int((newW - w) / 2)      # 向左延伸一點讓車牌在中間
            if x <= 0:
                x = 0                     # 避免 x 小於 0
            w = int(newW)                 # 更新寬度為新值

        # 加入轉換後的 x, y, w, h 到結果文字中（y 與 h 沒變，所以直接用原始值）
        rettext += str(int(x)) + ' ' + data[3 + i*4] + ' ' + str(int(w)) + ' ' + data[5 + i*4]

    line = fp.readline()  # 讀取下一行

fp.close()

# 把轉換後的文字寫回 info.txt（覆蓋原始檔案）
fp = open('Haar-Training_carPlate/training/positive/info.txt', 'w')
fp.write(rettext)
fp.close()

print('轉換圖框結束! ')
