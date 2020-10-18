from django.shortcuts import render
from django.http import HttpResponse

from pathlib import Path
import PIL.Image
from tkinter import *

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
from .models import Image


# Create your views here.
def showimage(request):
  images = Image.objects.all()
  context = {'images':images}
  return render(request, 'MLapp/image.html', context)

def estimate(request):
  root_dir = "."
  #images = Image.objects.all().
  image = list(Image.objects.order_by("id").reverse().values_list())
  for i in image:
      quizAnser = i
      break
  image_path = 'media/' + quizAnser[1]
  #image_path = 'media/images/IMG_9762.JPG'
  categories = ["鬼殺し", "十四代", "大吟醸", "獺祭", "アサヒスーパードライ", "アルパカ（赤）", 
            "アルパカ（白）", "こだわり酒場のレモンサワー", "ストロングゼロ", "ビール",
            "プレミアムモルツ", "ベジバル", "ほろよい", "もぎたてストロング", "ラガー", 
            "一番搾り", "角ハイボール", "麹レモンサワー", "赤玉パンチ", "男梅サワー", "氷結", "本搾り", ]

  alcohol_name_dict = {0:"鬼殺し", 
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
  alcohol_kind_dict = {
    0:"日本酒",
    1:"日本酒",
    2:"日本酒",
    3:"日本酒",
    4:"ビール",
    5:"ワイン",
    6:"ワイン",
    7:"果実酒",
    8:"ストロング系",
    9:"ビール",
    10:"ビール",
    11:"果実酒",
    12:"果実酒",
    13:"ストロング系",
    14:"果実酒",
    15:"ビール",
    16:"ハイボール",
    17:"果実酒",
    18:"果実酒",
    19:"果実酒",
    20:"氷結",
    21:"ビール",
  }

  #クラス数
  nb_classes = len(categories)
  # 保存したモデルの読み込み
  model = model_from_json(open('MLapp/MLmodel/model.json').read())
  # 保存した重みの読み込み
  model.load_weights('MLapp/MLmodel/model.hdf5')

  image = PIL.Image.open(image_path)
  image = image.resize((256,256))
  image_array = np.asarray(image)/255
  image_array = image_array.reshape(-1,256,256,3)

  pred = model.predict(image_array)
  alcohol_id = np.argmax(pred[0])
  alcohol_name = alcohol_name_dict[alcohol_id]#これがお酒の名前
  alcohol_kind = alcohol_kind_dict[alcohol_id]#これがお酒の種類

  
  return render(request, 'MLapp/estimate.html', {'alcohol_name': alcohol_name,
    'alcohol_kind': alcohol_kind})

