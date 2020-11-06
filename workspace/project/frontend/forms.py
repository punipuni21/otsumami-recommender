from django import forms
from .models import Quiz
from django import forms
from django.contrib.admin import widgets
import os
import random


ns = random.sample(range(15,83), 9)

def decide_coice(count, CHOICE_dict):
    CHOICEs = {
        (ns[count*3], CHOICE_dict[ns[count*3]]),
        (ns[count*3+1], CHOICE_dict[ns[count*3+1]]),
        (ns[count*3+2], CHOICE_dict[ns[count*3+2]])
    }
    return CHOICEs

CHOICESAKE = {
    (1,'1'),
    (2,'2'),
    (3,'3'),
}
CHOICE_dict = {
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
CHOICE = {
    (15,'サラダ系'),
    (16,'野菜スティック'),
    (17,'お漬物'),
    (18, 'キムチ'),
    (19, 'らっきょ'),
    (20, '梅'),
    (21, '枝豆'),
    (22, 'サラダチキン'),
    (23, 'ウィンナー'),
    (24, 'ベーコン'),
    (25, 'スモークタン'),
    (26, '生ハム'),
    (27, 'から揚げ'),
    (28, 'つくね'),
    (29, 'かまぼこ'),
    (30, 'かにかま'),
    (31, 'ちくわ'),
    (32, '魚'),
    (33, 'たこぶつ'),
    (34, 'ご飯もの'),
    (35, 'ハンバーグ'),
    (36, '餃子'),
    (37, 'シュウマイ'),
    (38, '酢豚'),
    (39, '筑前煮'),
    (40, 'おでん'),
    (41, '缶詰'),
    (42, 'おうどん'),
    (43, 'おそうめん'),
    (44, 'おそば'),
    (45, '中華麺'),
    (46, 'カップ麺'),
    (47, 'からあげくん'),
    (48, 'コロッケ'),
    (49, '中華饅'),
    (50, 'アメリカンドッグ'),
    (51, '焼き鳥'),
    (52, 'プリン'),
    (53, 'タルト'),
    (54, 'わらび餅'),
    (55, '饅頭'),
    (56, 'どら焼き'),
    (57, 'クッキー'),
    (58, 'ロールケーキ'),
    (59, 'バームクーヘン'),
    (60, 'ドーナツ'),
    (61, 'マシュマロ'),
    (62, 'チョコレート菓子'),
    (63, 'ポップコーンン'),
    (64, '塩味のスナック'),
    (65, '辛いスナック'),
    (66, 'コンソメスナック'),
    (67, '揚げ菓子'),
    (68, 'チー鱈'),
    (69, '豆菓子'),
    (70, 'おせんべい'),
    (71, 'スルメ'),
    (72, 'ビーフジャーキー'),
    (73, '温泉卵'),
    (74, '割けるチーズ'),
    (75, 'スモークチーズ'),
    (76, 'お豆腐'),
    (77, 'ドライフルーツ'),
    (78, 'フルーツ'),
    (79, 'ヴァニライス'),
    (80, 'チョコレート'),
    (81, 'シャーベットアイス'),
    (82, 'フルーツのアイス'),
}
target_items_lista = [#0~14がいらなかった
                        'saladkei', 'yasaisuteliikku', 'otukemono', 'kimuchi', 'rakkyo', 'ume', 'edamame', 'saladchiken', 'winner', 'bacon', 'smoketang', 'namahamu',
                        'karaage', 'tukune', 'kamaboko', 'kanikama', 'tikuwa', 'fish', 'takobutu', 'gohanmono', 'hanbagu', 'gyouza','syuumai','subuta',
                        'tikuzenni','oden','kandume', 'udon', 'soumen','soba','tyukamen','kappumen','karaagekun','kokrokke','tyuukaman','amerikandoggu','yakitori','purin',
                        'taruto','warbimoti','mannjyuu','dorayaki','kukki','rolecake','baumukuuhen','dounatu','masyumaro','chocolategasi','poppukon','soltsnack',
                        'spicysnack','konsomesnack','agegasi','tiitara','mamegasi','osenbay','surume','beefjurky','onsentamago','sakeruchees','smokecheez','tofu',
                        'dryfruits','fruits','vanilaice','chocoice','syabettoice','fruitice']

class RadioForm(forms.Form):
    select = forms.ChoiceField(label='酒', widget=forms.RadioSelect, choices= CHOICESAKE, initial=2)
    select2 = forms.ChoiceField(label='属性2', widget=forms.RadioSelect, choices= decide_coice(0, CHOICE_dict), initial=15)
    select3 = forms.ChoiceField(label='属性3', widget=forms.RadioSelect, choices= decide_coice(1, CHOICE_dict), initial=15)
    select4 = forms.ChoiceField(label='属性4', widget=forms.RadioSelect, choices= decide_coice(2,CHOICE_dict), initial=15)



class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('kindSake', 'firstfeeling', 'secondfeeling', 'thirdfeeling')
        labels = {
            'kindSake':'お酒は何aaa？',
            'firstfeeling': '今の気分１',
            'secondfeeling': '今の気分２',
            'thirdfeeling':'今の気分３',
        }

