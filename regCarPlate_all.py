import cv2
import glob

# 取得 realPlate 資料夾中所有 .jpg 檔案路徑
files = glob.glob("realPlate/*.jpg")

# 逐張處理每張圖片
for file in files:
    print('圖片檔案:' + file)
    img = cv2.imread(file)  # 讀取圖片

    # 載入 Haar 分類器（使用訓練好的車牌偵測模型）
    detector = cv2.CascadeClassifier('haar_carplate.xml')

    # 偵測車牌區域
    signs = detector.detectMultiScale(
        img,
        minSize=(76, 20),       # 設定最小偵測尺寸，避免誤偵過小物體
        scaleFactor=1.1,        # 每次圖像縮小的比例（1.1 表示每次縮小 10%）
        minNeighbors=5          # 至少有 5 個重疊區域才被視為偵測成功（可濾除假陽性）
    )

    # 如果有偵測到車牌
    if len(signs) > 0:
        for (x, y, w, h) in signs:
            # 在圖片上畫出紅色的車牌邊框
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            print(signs)  # 印出偵測到的車牌座標資訊
    else:
        print('沒有偵測到車牌!')

    # 顯示圖片（含車牌邊框）
    cv2.imshow('Frame', img)

    # 等待按鍵輸入（暫停在這張圖），按下任意鍵繼續
    key = cv2.waitKey(0)

    # 關閉顯示視窗
    cv2.destroyAllWindows()

    # 如果按下的是 Q（81）或 q（113），則跳出迴圈結束程式
    if key == 113 or key == 81:
        break
