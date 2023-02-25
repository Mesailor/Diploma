from django import forms


class FormCh740(forms.Form):
    candidate = forms.CharField(label='Кандидат')
    type_n_number = forms.CharField(label='Тип и регистрационный номер ВС')
    aerodrome = forms.CharField(label='Аэродром взлета/посадки')
    date = forms.CharField(label='Дата проверки')
    time = forms.CharField(label='Время полета')
    sum_time = forms.CharField(label='Общий налет')
    result = forms.CharField(label='Общий результат проверки')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh741(forms.Form):
    preparation = forms.CharField(label='Подготовка к полету')
    inspection = forms.CharField(label='Осмотры и проверки')
    startup = forms.CharField(label='Запуск двигателя, проверки и руление перед взлетом')
    takeoff = forms.CharField(label='Взлет в ночное время, набор высоты')
    circle_flight = forms.CharField(label='Полет по кругу в ночное время')
    landing = forms.CharField(label='Посадка в ночное время')
    approach = forms.CharField(label='Заход на посадку без использования системы визуальной индикации глиссады')
    missed_approach = forms.CharField(label='Уход на второй круг')
    radio_failure = forms.CharField(label='Знание действий при отказе радио и электрооборудования')
    eng_failure = forms.CharField(label='Знание действий при отказе двигателя')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh742(forms.Form):
    attestation = forms.CharField(label='Результаты летной проверки(сдал/не сдал)')
    recommendations = forms.CharField(label='РЕКОМЕНДАЦИИ', widget=forms.Textarea)
    examiner = forms.CharField(label='Фамилия')
    license_num = forms.CharField(label='Номер пилотского свидетельства')
    date = forms.CharField(label='Дата')


forms_dict = {0: FormCh740,
              1: FormCh741,
              2: FormCh742}
