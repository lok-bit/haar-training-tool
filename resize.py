import os
import shutil
import glob
import time
from PIL import Image
import PIL

def emptydir (dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        time.sleep(2)
    os.mkdir(dirname)

def dirResize (src, dst):
    # 取得資料夾中所有副檔名為 .JPG 的圖片檔案路徑
    myfiles= glob.glob(src + '/*.JPG')
    # 清空/建立資料夾，用來存放轉換後的圖片
    emptydir(dst)
    print(src+'資料夾 :')
    print('開始轉換圖形尺寸!')
    for i, f in enumerate(myfiles):
        # 讀取原始圖片
        img = Image.open(f)
        # 調整大小為 300x225，使用高品質縮放
        img_new = img.resize((300, 225), PIL.Image.LANCZOS)  
        # 建立儲存檔名，格式為 resizejpg001.jpg、resizejpg002.jpg ...
        outname = 'resizejpg' + str('{:0>3d}').format(i + 1) + '.jpg'  
        img_new.save(dst + '/' + outname)
    print('轉換圖形尺寸完成!\n')

dirResize('carPlate_sr', 'carPlate')
dirResize('realPlate_sr', 'realPlate')