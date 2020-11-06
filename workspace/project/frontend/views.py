from django.shortcuts import render, HttpResponse, redirect
from .models import Sample, Quiz
from .forms import QuizForm, RadioForm
from django.urls import reverse
import numpy as np
import operator
from urllib.parse import urlencode
import itertools
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


def oldview(request):
    form = RadioForm(request.POST)
    return redirect('/submit')

def newview(request):
    form = RadioForm(request.POST)
    return render(request,'frontend/oldview.html',{"form" : form})



def new(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        #form = QuizForm(request.POST)
        form = RadioForm(request.POST)
        if form.is_valid():
            """
            redirect_url = '/newview'
            form = urlencode(QuizForm(request.POST))
            url = f'{redirect_url}?{form}'
            return redirect(url)
            """
            
            key = (int(form.data['select']), int(form.data['select2']), int(form.data['select3']), int(form.data['select4']))
            return recommend(request, key[0], key[1], key[2], key[3])
            

        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = RadioForm()
    return render(request, 'frontend/new.html', params)

def recommend(request, one, two ,three, four):
    target_items_list = ['sampleid', 'sex', 'age', 'beer', 'weakTyuhi', 'mediumTyuhi', 'strongTyuhi', 'wisky', 'sprits', 'wine','fruitsake', 'liqueur', 'umesyu', 'sake', 'shoTyu', #0~11
                         'saladkei', 'yasaisuteliikku', 'otukemono', 'kimuchi', 'rakkyo', 'ume', 'edamame', 'saladchiken', 'winner', 'bacon', 'smoketang', 'namahamu',
                         'karaage', 'tukune', 'kamaboko', 'kanikama', 'tikuwa', 'fish', 'takobutu', 'gohanmono', 'hanbagu', 'gyouza','syuumai','subuta',
                         'tikuzenni','oden','kandume', 'udon', 'soumen','soba','tyukamen','kappumen','karaagekun','kokrokke','tyuukaman','amerikandoggu','yakitori','purin',
                         'taruto','warbimoti','mannjyuu','dorayaki','kukki','rolecake','baumukuuhen','dounatu','masyumaro','chocolategasi','poppukon','soltsnack',
                         'spicysnack','konsomesnack','agegasi','tiitara','mamegasi','osenbay','surume','beefjurky','onsentamago','sakeruchees','smokecheez','tofu',
                         'dryfruits','fruits','vanilaice','chocoice','syabettoice','fruitice']
    target_items_lista = [#0~14がいらなかった
                         'saladkei', 'yasaisuteliikku', 'otukemono', 'kimuchi', 'rakkyo', 'ume', 'edamame', 'saladchiken', 'winner', 'bacon', 'smoketang', 'namahamu',
                         'karaage', 'tukune', 'kamaboko', 'kanikama', 'tikuwa', 'fish', 'takobutu', 'gohanmono', 'hanbagu', 'gyouza','syuumai','subuta',
                         'tikuzenni','oden','kandume', 'udon', 'soumen','soba','tyukamen','kappumen','karaagekun','kokrokke','tyuukaman','amerikandoggu','yakitori','purin',
                         'taruto','warbimoti','mannjyuu','dorayaki','kukki','rolecake','baumukuuhen','dounatu','masyumaro','chocolategasi','poppukon','soltsnack',
                         'spicysnack','konsomesnack','agegasi','tiitara','mamegasi','osenbay','surume','beefjurky','onsentamago','sakeruchees','smokecheez','tofu',
                         'dryfruits','fruits','vanilaice','chocoice','syabettoice','fruitice']
    CHOICE_dict = {
        3:'ビール',
        4:'ほろよい',
        5:'やや強チューハイ',
        6:'ストロングチューハイ',
        7:'ウヰスキー',
        8:'スピリッツ',
        9:'ワイン',
        10:'果実酒',
        11:'リキュール系',
        12:'梅酒',
        13:'日本酒',
        14:'焼酎',
        15:'サラダ系',
        16:'野菜スティック',
        17:'お漬物',
        18: 'キムチ',
        19: 'らっきょ',
        20:'梅',
        21:'枝豆',
        22: 'サラダチキン',
        23: 'ウィンナー',
        24: 'ベーコン',
        25: 'スモークタン',
        26: '生ハム',
        27: 'から揚げ',
        28: 'つくね',
        29 :'かまぼこ',
        30: 'かにかま',
        31: 'ちくわ',
        32: '魚',
        33 :'たこぶつ',
        34: 'ご飯もの',
        35: 'ハンバーグ',
        36: '餃子',
        37:'シュウマイ',
        38: '酢豚',
        39: '筑前煮',
        40: 'おでん',
        41: '缶詰',
        42: 'おうどん',
        43: 'おそうめん',
        44: 'おそば',
        45: '中華麺',
        46: 'カップ麺',
        47: 'からあげくん',
        48: 'コロッケ',
        49: '中華饅',
        50: 'アメリカンドッグ',
        51: '焼き鳥',
        52: 'プリン',
        53: 'タルト',
        54: 'わらび餅',
        55: '饅頭',
        56: 'どら焼き',
        57: 'クッキー',
        58: 'ロールケーキ',
        59: 'バームクーヘン',
        60: 'ドーナツ',
        61: 'マシュマロ',
        62: 'チョコレート菓子',
        63:'ポップコーンン',
        64: '塩味のスナック',
        65: '辛いスナック',
        66: 'コンソメスナック',
        67:'揚げ菓子',
        68: 'チー鱈',
        69: '豆菓子',
        70: 'おせんべい',
        71: 'スルメ',
        72: 'ビーフジャーキー',
        73: '温泉卵',
        74: '割けるチーズ',
        75: 'スモークチーズ',
        76: 'お豆腐',
        77: 'ドライフルーツ',
        78: 'フルーツ',
        79: 'ヴァニライス',
        80: 'チョコレート',
        81: 'シャーベットアイス',
        82: 'フルーツのアイス',
    }
    """
    ##クイズの最新の結果をタプルで取得(ID, sake, feel1, feel2, sex)
    earliest_quiz = list(Quiz.objects.order_by("id").reverse().values_list())
    Quiz.objects.all().delete()
    
    for i in earliest_quiz:
        quizAnser = i
        break
    """
    quizAnser = [CHOICE_dict[one+3], CHOICE_dict[two], CHOICE_dict[three], CHOICE_dict[four]]

    #画像とクイズから得られたターゲットデータ
    target_sake = target_items_list[one+3]
    first_otsumami = {target_items_list[two] : two}
    second_otsumami = {target_items_list[three] : three}
    target_data = [first_otsumami, second_otsumami]
    sample_lists = list(Sample.objects.all().values())


    #選んだ酒の評価が高い人のサンプルデータを取得
    samePersonList = findsamePerson(target_sake, sample_lists)

    #類似度を計算
    similarities = get_similarities(samePersonList, target_data)

    #ランキング付ける
    ranking = predict(samePersonList, similarities, target_items_list, CHOICE_dict)

    params = {
        'title': 'title',
        'massage': similarities,
        '酒の種類':quizAnser[0],
        'おつまみ１':quizAnser[1],
        'おつまみ２':quizAnser[2],
        'おつまみ３':quizAnser[3],
        '1位':ranking[0][0],
        'quizAnser': quizAnser,
        'data': ranking,
    }
    return render(request, 'frontend/recommend.html', context=params)

def findsamePerson(target_sake, sample_lists):#(str, list[dict])
    #ターゲットの酒の評価が５のサンプルを抽出する
    #評価が高い人のデータ（辞書型）をsamePersonListに入れていく

    samePersonList = []
    for item in sample_lists:
        if item[target_sake] >= 3:
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


def predict(samePersonList, similarities, target_items_list, CHOICE_dict):#全samepersonに対して類似度×評価値をして予測評価値を出す
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
        if index == 6:
            break
        predict_list.append([CHOICE_dict[index+15], value])
    return sorted(predict_list, key= lambda s: s[1], reverse=True)
