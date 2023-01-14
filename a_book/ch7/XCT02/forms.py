from django import forms


class FormCh720(forms.Form):
    candidate = forms.CharField(label='Кандидат')
    type_n_number = forms.CharField(label='Тип и регистрационный номер ВС')
    aerodrome = forms.CharField(label='Аэродром взлета/посадки')
    date = forms.CharField(label='Дата проверки')
    time = forms.CharField(label='Время полета')
    sum_time = forms.CharField(label='Общий налет')
    result = forms.CharField(label='Общий результат проверки')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh721(forms.Form):
    research = forms.CharField(label='Изучение района полетов и метеоусловий')
    planning = forms.CharField(label='Планирование маршрута и подготовка карты')
    flight_plan = forms.CharField(label='Подготовка рабочего плана полета')
    operating_proc = forms.CharField(label='Знание эксплуатационных процедур')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh722(forms.Form):
    docs_check = forms.CharField(label='Проверка документации и оборудования на борту ВС')
    aircraft_inspection = forms.CharField(label='Принятие и осмотр ВС')
    startup = forms.CharField(label='Запуск двигателя, руление, подготовка к взлету')
    takeoff = forms.CharField(label='Взлет, набор высоты')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh723(forms.Form):
    VFR = forms.CharField(label='Правила визуальной навигации')
    radio = forms.CharField(label='Ведение рабочего плана полета, радиообмена')
    circumspection = forms.CharField(label='Осмотрительность и наблюдение')
    maintaining = forms.CharField(label='Выдерживание параметров полета')
    route_changes = forms.CharField(label='Действия при изменении маршрута')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh724(forms.Form):
    approach_prep = forms.CharField(label='Подготовка к заходу на посадку')
    app_n_landing = forms.CharField(label='Заход на посадку и посадка')
    afterflight_proc = forms.CharField(label='Послеполетные процедуры')
    paperwork = forms.CharField(label='Оформление документации')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh725(forms.Form):
    attestation = forms.CharField(label='Результаты летной проверки(сдал/не сдал)')
    dateGHT01 = forms.CharField(label='Дата успешного прохождения проверки GHT.01')
    recommendations = forms.CharField(label='РЕКОМЕНДАЦИИ', widget=forms.Textarea)
    signature = forms.ImageField(label='Подпись экзаменатора')
    examiner = forms.CharField(label='Фамилия')
    license_num = forms.CharField(label='Номер пилотского свидетельства')
    date = forms.CharField(label='Дата')


forms_dict = {0: FormCh720,
              1: FormCh721,
              2: FormCh722,
              3: FormCh723,
              4: FormCh724,
              5: FormCh725}
