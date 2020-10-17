from django.shortcuts import render, HttpResponse
from .models import Sample
import numpy as np
import operator

# Create your views here.

def recommend(request):
    return render(request, 'recommend.html')

def recommnd(request):
    #画像とクイズから得られたターゲットデータ
    target_sake = 'beer'
    first_otsumami = {'saladkei' : 1}
    second_otsumami = {'ume' : 2}
    third_otsumami = {'edamame' : 4}
    target_data = [first_otsumami, second_otsumami, third_otsumami]
    sample_lists = list(Sample.objects.all().values())


    #選んだ酒の評価が高い人のサンプルデータを取得
    samePersonList = findsamePerson(target_sake, sample_lists)

    #類似度を計算
    similarities = get_similarities(samePersonList, target_data)

    #ランキング付ける
    ranking = predict(samePersonList, similarities)

    target_samples = Sample.objects.all() #target_sakeの評価が５のサンプルデータの辞書型リスト
    params = {
        'title': 'title',
        'massage': similarities,
        'sameperson': ranking,
        'data': samePersonList,
    }
    return render(request, 'recmomend/recommend.html', context=params)

def findsamePerson(target_sake, sample_lists):#(str, list[dict])
    #ターゲットの酒の評価が５のサンプルを抽出する
    #評価が高い人のデータ（辞書型）をsamePersonListに入れていく

    samePersonList = []
    for item in sample_lists:
        if item[target_sake] == 5:
            samePersonList.append(item)
        else:
            pass
    return samePersonList

def get_similarities(samePersonList, target_data):# ( list[dict], list[dict] )
    similarities = []
    for j, sampleDict in enumerate(samePersonList):#sampleDictに評価が辞書型で入ってる
        distanceList = []
        for targetItem in target_data: #ターゲット辞書から、指定したおつまみの名前と評価値を取り出す
            for key in targetItem.keys():
                for targetValue in targetItem.values():
                    distance = targetValue - sampleDict[key]
                    distanceList.append(pow(distance, 2))
        similarities.append([j, 1/(1+np.sqrt(sum(distanceList)))])

    return sorted(similarities, key=lambda s: s[1], reverse=True)
    #return similarities


def predict(samePersonList, similarities):#全samepersonに対して類似度×評価値をして予測評価値を出す
    predict_list = []
    valueList = []#辞書型のsamepersonlistの評価値をリストにしたい
    for a in samePersonList:
        valueList.append(list(a.values()))
    for index, value in similarities:
        valueList[index] = [round(i*value,5) for i in valueList[index]] #round で小数を丸める

    np_samePerson = np.array(valueList)
    np_samePerson = list(np.mean(np_samePerson, axis=0))

    for index, value in enumerate(np_samePerson):
        predict_list.append([index, value])
    return sorted(predict_list, key= lambda s: s[1], reverse=True)


