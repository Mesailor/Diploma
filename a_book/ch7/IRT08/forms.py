from django import forms


class FormCh780(forms.Form):
    candidate = forms.CharField(label='Кандидат')
    type_n_number = forms.CharField(label='Тип и регистрационный номер ВС')
    aerodrome = forms.CharField(label='Аэродром взлета/посадки')
    date = forms.CharField(label='Дата проверки')
    time = forms.CharField(label='Время полета')
    sum_time = forms.CharField(label='Общий налет')
    result = forms.CharField(label='Общий результат проверки')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh781(forms.Form):
    planning = forms.CharField(label='Планирование полета')
    inspection = forms.CharField(label='Осмотр и проверка самолета')
    startup = forms.CharField(label='Запуск двигателя и руление')
    ATC_clearance = forms.CharField(label='Диспетчерское разрешение')
    takeoff = forms.CharField(label='Взлет и первоначальный набор высоты')
    airway_entering = forms.CharField(label='Выход на воздушную трассу')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh782(forms.Form):
    maintaining_track = forms.CharField(label='Выдерживание линии заданного пути')
    flightplan = forms.CharField(label='Ведение рабочего плана полета')
    reports = forms.CharField(label='Доклады о месте воздушного судна')
    instrumental_flight = forms.CharField(label='Полет по приборам')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh783(forms.Form):
    hold_area_entering = forms.CharField(label='Вход в зону ожидания')
    accuracy_hold_area = forms.CharField(label='Выдерживание схемы полета в зоне ожидания')
    maintaining_alt = forms.CharField(label='Выдерживание высоты')
    wind_correction = forms.CharField(label='Учет ветра')
    hold_area_leaving = forms.CharField(label='Выход из зоны ожидания')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh784(forms.Form):
    initial_stage = forms.CharField(label='Полет на начальном этапе')
    landing_course = forms.CharField(label='Выход на посадочный курс')
    ILS_established = forms.CharField(label='Захват курсового маяка и глиссады')
    decision_alt = forms.CharField(label='Снижение до высоты принятия решения')
    missed_approach = forms.CharField(label='Уход на второй круг или переход на визуальное пилотирование')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh785(forms.Form):
    initial_stage = forms.CharField(label='Полет на начальном этапе')
    landing_course = forms.CharField(label='Выход на посадочный курс')
    final_stage = forms.CharField(label='Полет по радиосредству на конечном этапе')
    decision_alt = forms.CharField(label='Снижение до минимальной высоты снижения')
    missed_approach = forms.CharField(label='Уход на второй круг или переход на визуальное пилотирование')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh786(forms.Form):
    observation = forms.CharField(label='Контроль и наблюдение в полете')
    flight_info = forms.CharField(label='Применение навигационного оборудования, использование справочников АНИ')
    radio = forms.CharField(label='Ведение радиообмена')
    IFR_knowledge = forms.CharField(label='Знание правил полета по приборам')
    briefing = forms.CharField(label='Инструктаж и организация работы в экипаже')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh787(forms.Form):
    attestation = forms.CharField(label='Результаты летной проверки(сдал/не сдал)')
    dateIFT07 = forms.CharField(label='Дата успешного прохождения проверки IFT.07')
    recommendations = forms.CharField(label='РЕКОМЕНДАЦИИ', widget=forms.Textarea)
    signature = forms.ImageField(label='Подпись экзаменатора')
    examiner = forms.CharField(label='Фамилия')
    license_num = forms.CharField(label='Номер пилотского свидетельства')
    date = forms.CharField(label='Дата')


forms_dict = {0: FormCh780,
              1: FormCh781,
              2: FormCh782,
              3: FormCh783,
              4: FormCh784,
              5: FormCh785,
              6: FormCh786,
              7: FormCh787}
