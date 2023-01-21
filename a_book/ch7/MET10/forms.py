from django import forms


class FormCh7100(forms.Form):
    candidate = forms.CharField(label='Кандидат')
    type_n_number = forms.CharField(label='Тип и регистрационный номер ВС')
    aerodrome = forms.CharField(label='Аэродром взлета/посадки')
    date = forms.CharField(label='Дата проверки')
    time = forms.CharField(label='Время полета')
    sum_time = forms.CharField(label='Общий налет')
    result = forms.CharField(label='Общий результат проверки')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh7101(forms.Form):
    preparation = forms.CharField(label='Подготовка к полету, запуск двигателя и руление')
    takeoff = forms.CharField(label='Взлет и набор высоты')
    circle_flight = forms.CharField(label='Полет по кругу, заход на посадку и посадка')
    eng_failure = forms.CharField(label='Имитация отказа двигателя в полете')
    one_eng_landing = forms.CharField(label='Посадка с одним неработающим двигателем')
    missed_approach = forms.CharField(label='Уход на второй круг при обоих работающих двигателях')
    one_eng_mis_apr = forms.CharField(
        label='Уход на второй круг при заходе на посадку с имитацией отказа одного двигателя')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh7102(forms.Form):
    attestation = forms.CharField(label='Результаты летной проверки(сдал/не сдал)')
    dateMET09 = forms.CharField(label='Дата успешного прохождения летной проверки MET.09')
    recommendations = forms.CharField(label='РЕКОМЕНДАЦИИ', widget=forms.Textarea)
    signature = forms.ImageField(label='Подпись экзаменатора')
    examiner = forms.CharField(label='Фамилия')
    license_num = forms.CharField(label='Номер пилотского свидетельства')
    date = forms.CharField(label='Дата')


forms_dict = {0: FormCh7100,
              1: FormCh7101,
              2: FormCh7102}
