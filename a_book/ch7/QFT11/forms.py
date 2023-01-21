from django import forms


class FormCh7110(forms.Form):
    candidate = forms.CharField(label='Кандидат')
    type_n_number = forms.CharField(label='Тип и регистрационный номер ВС')
    aerodrome = forms.CharField(label='Аэродром взлета/посадки')
    date = forms.CharField(label='Дата проверки')
    time = forms.CharField(label='Время полета')
    sum_time = forms.CharField(label='Общий налет')
    result = forms.CharField(label='Общий результат проверки')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh7111(forms.Form):
    preparation = forms.CharField(label='Подготовка к полету')
    inspection = forms.CharField(label='Осмотр и проверки')
    startup = forms.CharField(label='Запуск двигателей и руление')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh7112(forms.Form):
    takeoff = forms.CharField(label='Обычный взлет')
    landing = forms.CharField(label='Полет по кругу и посадка')
    eng_failure = forms.CharField(label='Имитация отказа двигателя в полете')
    one_eng_landing = forms.CharField(label='Посадка с имитацией отказа одного двигателя')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh7113(forms.Form):
    airway_entrance = forms.CharField(label='Выход на воздушную трассу')
    airway_navigation = forms.CharField(label='Навигация по воздушным трассам')
    hold_area = forms.CharField(label='Полет в зоне ожидания')
    precision_app = forms.CharField(label='Точный заход на посадку')
    nonprecision_app = forms.CharField(label='Неточный заход на посадку')
    missed_approach = forms.CharField(label='Уход на второй круг')
    low_alt_circle = forms.CharField(label='Полет по кругу на малой высоте')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh7114(forms.Form):
    radio = forms.CharField(label='Радиообмен')
    observation = forms.CharField(label='Контроль параметров и наблюдение в полете')
    visual_maneuvering = forms.CharField(label='Визуальное маневрирование')
    team_work = forms.CharField(label='Организация работы экипажа')
    missed_approach = forms.CharField(label='Уход на второй круг')
    emergency = forms.CharField(label='Действия в аварийной ситуации')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh7115(forms.Form):
    attestation = forms.CharField(label='Результаты летной проверки(сдал/не сдал)')
    dateGHT06 = forms.CharField(label='Дата успешного прохождения проверки GHT.06')
    dateIRT08 = forms.CharField(label='Дата успешного прохождения проверки IRT.08')
    dateMET09 = forms.CharField(label='Дата успешного прохождения проверки MET.09')
    dateMET10 = forms.CharField(label='Дата успешного прохождения проверки MET.10')
    recommendations = forms.CharField(label='РЕКОМЕНДАЦИИ', widget=forms.Textarea)
    signature = forms.ImageField(label='Подпись экзаменатора')
    examiner = forms.CharField(label='Фамилия')
    license_num = forms.CharField(label='Номер пилотского свидетельства')
    date = forms.CharField(label='Дата')


forms_dict = {0: FormCh7110,
              1: FormCh7111,
              2: FormCh7112,
              3: FormCh7113,
              4: FormCh7114,
              5: FormCh7115}
