import PIL
from PIL import Image
import glob
import shutil, os
import time

# 定義一個清空資料夾的函式：如果資料夾存在就刪掉重建
def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)   # 刪除整個資料夾
        time.sleep(2)            # 暫停 2 秒，確保刪除完成
    os.mkdir(dirname)            # 建立新的資料夾

# 取得 carNegative_sr 資料夾中所有副檔名為 .JPG 的圖片檔案路徑
myfiles = glob.glob("carNegative_sr/*.JPG")

# 清空/建立 carNegative 資料夾，用來存放轉換後的圖片
emptydir('carNegative')

print('開始轉換尺寸及灰階! ')

# 逐張處理圖片
for i, f in enumerate(myfiles):
    img = Image.open(f)                         # 讀取原始圖片
    img_new = img.resize((500, 375), PIL.Image.LANCZOS)  # 調整大小為 500x375，使用高品質縮放
    img_new = img_new.convert('L')              # 轉換為灰階模式（L = 8-bit 灰階）

    # 建立儲存檔名，格式為 negGray001.jpg、negGray002.jpg ...
    outname = "negGray" + '{:0>3d}'.format(i + 1) + '.jpg'

    # 儲存轉換後的圖片到 carNegative 資料夾中
    img_new.save('carNegative/' + outname)

    # i = i + 1 → 其實不需要這行，因為 enumerate 已經處理了 i 的遞增

print('轉換尺寸及灰階結束! ')
