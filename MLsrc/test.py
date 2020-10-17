
from PIL import Image
import os, glob, sys
import numpy as np
import random, math
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, array_to_img
from keras.layers.normalization import BatchNormalization
from keras import layers, models
from keras import optimizers
import keras
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Dense, Dropout, Activation, Flatten
import matplotlib.pyplot as plt
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.utils import plot_model
from keras.models import model_from_json
from keras.preprocessing import image


# #画像データごとにadd_sample()を呼び出し、X,Yの配列を返す関数
# def make_sample(files):
#     global X, Y
#     X = []
#     Y = []
#     for cat, fname in files:
#         add_sample(cat, fname)
#     return np.array(X), np.array(Y)

# #渡された画像データを読み込んでXに格納し、また、
# #画像データに対応するcategoriesのidxをY格納する関数
# def add_sample(cat, fname):
#     img = Image.open(fname)
#     img = img.convert("RGB")
#     img = img.resize((256, 256))
#     data = np.asarray(img)
#     X.append(data)
#     Y.append(cat)

# # 画像を拡張する関数
# def draw_images(generator, x, dir_name, index):
#     save_name = 'extened-' + str(index)
#     g = generator.flow(x, batch_size=1, save_to_dir=output_dir,
#                        save_prefix=save_name, save_format='jpg')

#     # 1つの入力画像から何枚拡張するかを指定（今回は50枚）
#     for i in range(50):
#         bach = g.next()



if __name__ == '__main__':

    root_dir = ".."
    categories = ["鬼殺し", "十四代", "大吟醸", "獺祭", "アサヒスーパードライ", "アルパカ（赤）", 
            "アルパカ（白）", "こだわり酒場のレモンサワー", "ストロングゼロ", "ビール",
            "プレミアムモルツ", "ベジバル", "ほろよい", "もぎたてストロング", "ラガー", 
            "一番搾り", "角ハイボール", "麹レモンサワー", "赤玉パンチ", "男梅サワー", "氷結", "本搾り", ]

    label_dict = {0:"鬼殺し", 
                    1:"十四代", 
                    2:"大吟醸", 
                    3:"獺祭", 
                    4:"アサヒスーパードライ",
                    5: "アルパカ（赤）",
                    6: "アルパカ（白）", 
                    7:"こだわり酒場のレモンサワー",
                    8: "ストロングゼロ", 
                    9:"ビール",
                    10:"プレミアムモルツ",
                    11: "ベジバル", 
                    12:"ほろよい",
                    13:"もぎたてストロング", 
                    14:"ラガー",
                    15:"一番搾り",
                    16: "角ハイボール",
                    17: "麹レモンサワー",
                    18: "赤玉パンチ",
                    19: "男梅サワー", 
                    20:"氷結",
                    21:"本搾り"}

    # # 画像データ用配列
    # X = []
    # # ラベルデータ用配列
    # Y = []

    # # 全データ格納用配列
    # allfiles = []

    # # カテゴリ配列の各値と、それに対応するidxを認識し、全データをallfilesにまとめる
    # for idx, cat in enumerate(categories):
    #     image_dir = root_dir + "/image_aug/" + cat
    #     print(image_dir)
    #     files = glob.glob(image_dir + "/*.jpg")
    #     for f in files:
    #         allfiles.append((idx, f))

    # # シャッフル後、学習データと検証データに分ける
    # random.shuffle(allfiles)
    # th = math.floor(len(allfiles) * 0.8)
    # train = allfiles[0:th]
    # test = allfiles[th:]
    # X_train, y_train = make_sample(train)
    # X_test, y_test = make_sample(test)
    # xy = (X_train, X_test, y_train, y_test)
    # データを保存する（データの名前を「tea_data.npy」としている）
    # np.save(root_dir + "/saves" + "/alcohol_data.npy", xy)


    nb_classes = len(categories)
    data = np.load(root_dir + "/images" + "/alcohol_data.npy",allow_pickle=True)
    X_train = data[0]
    X_test = data[1]
    y_train = data[3]
    y_test = data[3]


    X_train = X_train.astype("float") / 255
    X_test = X_test.astype("float") / 255

    # kerasで扱えるようにcategoriesをベクトルに変換

    y_train = np_utils.to_categorical(y_train, nb_classes)
    y_test = np_utils.to_categorical(y_test, nb_classes)

    # 保存したモデルの読み込み
    model = model_from_json(open(root_dir + "/MLmodel/" + 'model3.json').read())
    # 保存した重みの読み込み
    model.load_weights(root_dir + "/MLmodel/" + "model3.hdf5")


    score = model.predict(X_test)#ここに画像を入力する(枚数，高さ，幅，チャネル数)，今回は(1,256,256,3)の次元にする
    # print(type(score))
    # print(score.shape)
    alcohol_id = np.argmax(score[0])
    # print(score[0])
    # print(np.argmax(score[0]))
    ans = label_dict[alcohol_id]
    print("このお酒は",label_dict[alcohol_id],"です")
