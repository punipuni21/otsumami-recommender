from django import forms

from .models import Quiz

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('kindSake', 'sex', 'firstfeeling', 'secondfeeling')
        labels = {
            'kindSake':'お酒は何？',
            'sex':'性別',
            'firstfeeling': '今の気分１',
            'secondfeeling': '今の気分２',
        }
        help_texts = {
            'kindSake':'お酒は何？',
            'sex':'性別',
            'firstfeeling': '今の気分１',
            'secondfeeling': '今の気分２',
        }
