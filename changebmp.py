from PIL import Image
import glob
import os

# 取得 carPlate 資料夾中所有 .JPG 副檔名的圖片路徑
myfiles = glob.glob("carPlate/*.JPG")

print('開始轉換圖形格式! ')

# 逐張處理每一張 .JPG 圖片
for f in myfiles:
    namespilt = f.split("\\")  # 將檔案路徑以 \ 分割，取得檔名
    img = Image.open(f)        # 開啟圖片
    # 修改檔名：將 "resizejpg" 改成 "bmpraw"，副檔名改成 .bmp
    outname = namespilt[1].replace('resizejpg', 'bmpraw')
    outname = outname.replace('.jpg', '.bmp')
    # 將圖片以 BMP 格式儲存到同一個資料夾
    img.save('carPlate/' + outname, 'bmp')
    # 刪除原本的 .JPG 圖片
    os.remove(f)

print('轉換圖形格式結束! ')
