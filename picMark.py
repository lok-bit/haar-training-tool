import shutil, os
import time
from PIL import Image, ImageDraw

# 定義清空資料夾的函式，如果資料夾已存在就刪除後重新建立
def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)  # 刪除整個資料夾
        time.sleep(2)           # 等待 2 秒，避免系統還沒完全釋放資源
    os.mkdir(dirname)           # 建立新資料夾

# 開啟 info.txt，這個檔案記錄了每張正樣本圖的座標標註資訊
fp = open('Haar-Training_carPlate/training/positive/info.txt', 'r')

# 讀取第一行內容（每行對應一張圖片的標註）
line = fp.readline()
# 清空並建立儲存標註圖的資料夾
emptydir('picMark')
print('開始繪製圖框!')
# 持續讀取每一行直到結束
while line:
    data = line.split(' ')  # 以空白分割每一段資料
    img = Image.open('Haar-Training_carPlate/training/positive/' + data[0])  # 讀取圖片
    draw = ImageDraw.Draw(img)  # 建立繪圖物件
    n = data[1]  # 圖片中有幾個物件
    # 依據標註資訊繪製紅框
    for i in range(int(n)):
        x = int(data[2 + i*4])      # 左上角 x 座標
        y = int(data[3 + i*4])      # 左上角 y 座標
        w = int(data[4 + i*4])      # 寬度
        h = int(data[5 + i*4])      # 高度
        draw.rectangle((x, y, x + w, y + h), outline='red')  # 畫出紅框
    # 取出圖片檔名（去除資料夾路徑）
    filename = (data[0].split('/'))[-1]
    # 儲存繪製紅框後的圖片到 picMark 資料夾
    img.save('picMark/' + filename)
    # 讀取下一行
    line = fp.readline()

fp.close()
print('繪製圖框結束! ')

