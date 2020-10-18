from django.shortcuts import render, HttpResponse, redirect
from .models import Sample, Quiz
from .forms import QuizForm
import numpy as np
import operator

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def submit(request):
    return render(request, 'frontend/submit.html')

def quiz(request):
    return render(request, 'frontend/quiz.html')

def photo(request):
    return render(request, 'frontend/photo.html')

def result(request):
    return render(request, 'frontend/result.html')

def new(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/recommend')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = QuizForm()
    return render(request, 'frontend/new.html', params)

def recommend(request):
    target_items_list = ['sampleid', 'sex', 'age', 'beer', 'weakTyuhi', 'mediumTyuhi', 'strongTyuhi', 'wisky', 'sprits', 'wine','fruitsake', 'liqueur', 'umesyu', 'sake', 'shoTyu', #0~11
                         'saladkei', 'yasaisuteliikku', 'otukemono', 'kimuchi', 'rakkyo', 'ume', 'edamame', 'saladchiken', 'winner', 'bacon', 'smoketang', 'namahamu',
                         'karaage', 'tukune', 'kamaboko', 'kanikama', 'tikuwa', 'fish', 'takobutu', 'gohanmono', 'hanbagu', 'gyouza','syuumai','subuta',
                         'tikuzenni','oden','kandume', 'udon', 'soumen','soba','tyukamen','kappumen','karaagekun','kokrokke','tyuukaman','amerikandoggu','yakitori','purin',
                         'taruto','warbimoti','mannjyuu','dorayaki','kukki','rolecake','baumukuuhen','dounatu','masyumaro','chocolategasi','poppukon','soltsnack',
                         'spicysnack','konsomesnack','agegasi','tiitara','mamegasi','osenbay','surume','beefjurky','onsentamago','sakeruchees','smokecheez','tofu',
                         'dryfruits','fruits','vanilaice','chocolate','syabettoice','fruitice']
    target_items_lista = [#0~14がいらなかった
                         'saladkei', 'yasaisuteliikku', 'otukemono', 'kimuchi', 'rakkyo', 'ume', 'edamame', 'saladchiken', 'winner', 'bacon', 'smoketang', 'namahamu',
                         'karaage', 'tukune', 'kamaboko', 'kanikama', 'tikuwa', 'fish', 'takobutu', 'gohanmono', 'hanbagu', 'gyouza','syuumai','subuta',
                         'tikuzenni','oden','kandume', 'udon', 'soumen','soba','tyukamen','kappumen','karaagekun','kokrokke','tyuukaman','amerikandoggu','yakitori','purin',
                         'taruto','warbimoti','mannjyuu','dorayaki','kukki','rolecake','baumukuuhen','dounatu','masyumaro','chocolategasi','poppukon','soltsnack',
                         'spicysnack','konsomesnack','agegasi','tiitara','mamegasi','osenbay','surume','beefjurky','onsentamago','sakeruchees','smokecheez','tofu',
                         'dryfruits','fruits','vanilaice','chocolate','syabettoice','fruitice']
    ##クイズの最新の結果をタプルで取得(ID, sake, feel1, feel2, sex)
    earliest_quiz = list(Quiz.objects.order_by("id").reverse().values_list())
    for i in earliest_quiz:
        quizAnser = i
        break

    #画像とクイズから得られたターゲットデータ
    target_sake = target_items_list[quizAnser[1]]
    first_otsumami = {'saladkei' : quizAnser[2]}
    second_otsumami = {'ume' : quizAnser[3]}
    target_data = [first_otsumami, second_otsumami]
    sample_lists = list(Sample.objects.all().values())


    #選んだ酒の評価が高い人のサンプルデータを取得
    samePersonList = findsamePerson(target_sake, sample_lists)

    #類似度を計算
    similarities = get_similarities(samePersonList, target_data)

    #ランキング付ける
    ranking = predict(samePersonList, similarities, target_items_list)

    params = {
        'title': 'title',
        'massage': similarities,
        'sameperson': quizAnser,
        'data': ranking,
    }
    return render(request, 'frontend/recommend.html', context=params)

def findsamePerson(target_sake, sample_lists):#(str, list[dict])
    #ターゲットの酒の評価が５のサンプルを抽出する
    #評価が高い人のデータ（辞書型）をsamePersonListに入れていく

    samePersonList = []
    for item in sample_lists:
        if item[target_sake] == 1:
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


def predict(samePersonList, similarities, target_items_list):#全samepersonに対して類似度×評価値をして予測評価値を出す
    predict_list = []
    valueList = []#辞書型のsamepersonlistの評価値をリストにしたい

    for a in samePersonList:
        valueList.append(list(a.values()))
    for index, value in similarities:
        valueList[index] = [round(i*value,5) for i in valueList[index]] #round で小数を丸める
        valueList[index] = valueList[index][15:]
    np_samePerson = np.array(valueList)
    np_samePerson = list(np.mean(np_samePerson, axis=0))

    for index, value in enumerate(np_samePerson):
        predict_list.append([target_items_list[index+15], value])
    return sorted(predict_list, key= lambda s: s[1], reverse=True)
