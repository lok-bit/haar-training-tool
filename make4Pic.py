from PIL import Image

# 設定圖片與標註檔案的資料夾路徑
path = 'Haar-Training_carPlate/training/positive/'

# 開啟原始的 info.txt，讀取標註資訊
fp = open(path + 'info.txt', 'r')
line = fp.readline()

count = 73      # 設定新的圖片編號起始值（通常接續之前的編號）
rettext = ''    # 用來儲存新的標註內容
print('開始產生新圖片! ')

# 一行一行讀取標註檔，每行代表一張圖片與其標註框
while line:
    data = line.split(' ')
    img = Image.open(path + data[0])  # 讀取原始圖

    # 擷取標註框位置與大小
    x = int(data[2])
    y = int(data[3])
    w = int(data[4])
    h = int(data[5])

    # 設定邊緣裁切大小（裁切時保留邊邊）
    reduceW = 30
    reduceH = int(reduceW * 0.75)  # 高度的裁切比例配合寬度

    # 計算縮放倍率（把較小的裁切區域放大成 300x225）
    multi = float(300 / (300 - reduceW))

    # 計算車牌在新圖片中應有的寬高（經縮放後）
    neww = int(w * multi)
    newh = int(h * multi)

    # === 以下為四種不同裁切條件的擴增方式 ===

    # 左上裁切 → 避開車牌的左與上，讓車牌偏右下角
    if (x - reduceW) > 5 and (y - reduceH) > 5:
        count += 1
        newimg = img.crop((reduceW, reduceH, 300, 225))  # 裁切區域
        newimg = newimg.resize((300, 225), Image.LANCZOS)  # 縮放
        newimg.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count), 'bmp')

        # 計算新圖中車牌框的位置
        newx = int((x - reduceW) * multi - reduceW * (multi - 1) / 2)
        newy = int((y - reduceH) * multi - reduceH * (multi - 1) / 2)

        # 組合標註資訊並加到結果中
        rettext += 'rawdata/bmpraw{:>3d}.bmp 1 {} {} {} {}\n'.format(
            count, newx, newy, neww, newh
        )

    # 右上裁切 → 去掉右邊與上邊的圖，讓車牌偏左下角
    if (x + w) < (300 - reduceW - 5) and y > (reduceH + 5):
        count += 1
        newimg = img.crop((0, reduceH, (300 - reduceW), 225))
        newimg = newimg.resize((300, 225), Image.LANCZOS)
        newimg.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count), 'bmp')

        newx = int(x * multi)
        newy = int((y - reduceH) * multi - reduceH * (multi - 1) / 2)

        rettext += 'rawdata/bmpraw{:0>3d}.bmp 1 {} {} {} {}\n'.format(
            count, newx, newy, neww, newh
        )

    # 左下裁切 → 去掉左邊與下邊，車牌偏右上
    if (x - reduceW) > 5 and (y + h) < (225 - reduceH - 5):
        count += 1
        newimg = img.crop((reduceW, 0, 300, 225 - reduceH))
        newimg = newimg.resize((300, 225), Image.LANCZOS)
        newimg.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count), 'bmp')

        newx = int((x - reduceW) * multi - reduceW * (multi - 1) / 2)
        newy = int(y * multi)

        rettext += 'rawdata/bmpraw{:>3d}.bmp 1 {} {} {} {}\n'.format(
            count, newx, newy, neww, newh
        )

    # 右下裁切 → 去掉右與下邊，車牌偏左上
    if (x + w) < (300 - reduceW - 5) and (y + h) < (225 - reduceH - 5):
        count += 1
        newimg = img.crop((0, 0, (300 - reduceW), 225 - reduceH))
        newimg = newimg.resize((300, 225), Image.LANCZOS)
        newimg.save(path + 'rawdata/bmpraw{:0>3d}.bmp'.format(count), 'bmp')

        newx = int(x * multi)
        newy = int(y * multi)

        rettext += 'rawdata/bmpraw{:0>3d}.bmp 1 {} {} {} {}\n'.format(
            count, newx, newy, neww, newh
        )

    # 讀取下一行標註
    line = fp.readline()

fp.close()

# 將擴增後的標註資訊寫入 Info.txt（用 append 模式加在後面）
fpmake = open(path + 'Info.txt', 'a')
fpmake.write(rettext)
fpmake.close()

print('產生新圖片結束! ')
