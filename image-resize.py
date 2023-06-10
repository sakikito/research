import cv2
import os

# Pythonで実行中のファイルの場所（パス）を取得する
BASE_DIR = os.path.dirname(__file__)

def get_write_dir_path():

    # パスを結合する(outputフォルダを作成する)
    write_dir_path = os.path.join(BASE_DIR, "write_image")

    # outputディレクトリが存在しない場合
    if not os.path.exists(write_dir_path):

        # Pythonでディレクトリ（フォルダ）を作成するmkdir
        os.makedirs(write_dir_path)

    return write_dir_path

# 保存先を作成する
get_write_dir_path()

# 画像数(30) + 1
image_num = 31

for i in range(1,image_num):

    # 読み込む画像を選択
    img = cv2.imread("read_image\img ({}).jpg".format(i))

    # サイズ設定｜cv2では(幅、高さ）の順で数値を設定
    size = (600,400)

    # リサイズ
    img_resize = cv2.resize(img,size)

    cv2.imwrite("resize{}.jpg".format(i), img_resize)
