from django import forms


class Chapter4(forms.Form):
    date = forms.CharField(label='Дата')
    exercise = forms.CharField(label='Упражнение, краткое содержание занятия', widget=forms.Textarea)
    time = forms.CharField(label='Время')
    grade = forms.IntegerField(label='Оценка', min_value=2, max_value=5)
    examiner = forms.CharField(label='Должность, фамилия и инициалы лица проводившего Н.П.')
