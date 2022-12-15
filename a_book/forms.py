from django import forms


class FormCh4(forms.Form):
    date = forms.CharField(label='Дата')
    exercise = forms.CharField(label='Упражнение, краткое содержание занятия', widget=forms.Textarea)
    time = forms.CharField(label='Время')
    grade = forms.IntegerField(label='Оценка', min_value=2, max_value=5)
    examiner = forms.CharField(label='Должность, фамилия и инициалы лица проводившего Н.П.')


class FormCh5(forms.Form):
    date = forms.CharField(label='Дата', max_length=11)
    type = forms.CharField(label='Тип тренажера', max_length=10)
    exercise = forms.CharField(label='Упражнение, краткое содержание тренировки', max_length=120, widget=forms.Textarea)
    time_hours = forms.IntegerField(label='Время(час)', max_value=6)
    time_mins = forms.IntegerField(label='Время(мин)', max_value=60)
    instrumental_time_hours = forms.IntegerField(label='Из них по приборам(час)', max_value=6)
    instrumental_time_mins = forms.IntegerField(label='Из них по приборам(мин)', max_value=60)
    grade = forms.IntegerField(label='Оценка', min_value=2, max_value=5)
    examiner = forms.CharField(label='Пилот-инструктор', max_length=50)


forms = {4: FormCh4,
         5: FormCh5}
