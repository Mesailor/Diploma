from django import forms


class FormCh750(forms.Form):
    candidate = forms.CharField(label='Кандидат')
    type_n_number = forms.CharField(label='Тип и регистрационный номер ВС')
    aerodrome = forms.CharField(label='Аэродром взлета/посадки')
    date = forms.CharField(label='Дата проверки')
    time = forms.CharField(label='Время полета')
    sum_time = forms.CharField(label='Общий налет')
    result = forms.CharField(label='Общий результат проверки')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh751(forms.Form):
    research = forms.CharField(label='Изучение района полета и метеоусловий')
    route_choice = forms.CharField(label='Выбор маршрута полета')
    flightplan_prep = forms.CharField(label='Подготовка карты и рабочего плана полета')
    calculation = forms.CharField(label='Проведение необходимых расчетов')
    docs_check = forms.CharField(label='Проверка документации и оборудования на борту ВС')
    inspection = forms.CharField(label='Осмотр ВС, запуск и руление')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh752(forms.Form):
    briefing = forms.CharField(label='Инструктаж пассажиров')
    takeoff = forms.CharField(label='Взлет, набор высоты')
    route_entering = forms.CharField(label='Выход на маршрут полета, действия на начальном этапе крейсерского полета')
    radio = forms.CharField(label='Ведение радиообмена')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh753(forms.Form):
    VFR = forms.CharField(label='Правила визуальной навигации')
    deck_operating = forms.CharField(label='Использование пилотажно-навигационного комплекса')
    nav_proc = forms.CharField(label='Общие навигационные процедуры')
    flightplan_operating = forms.CharField(label='Ведение рабочего плана полетов')
    route_changes = forms.CharField(label='Действия при изменении маршрута')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh754(forms.Form):
    app_n_landing = forms.CharField(label='Заход на посадку и посадка')
    info_using = forms.CharField(label='Получение и использование информации для полета')
    postflight_proc = forms.CharField(label='Послеполетные процедуры и заправка топливом')
    paperwork = forms.CharField(label='Оформление документации')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh755(forms.Form):
    accuracy = forms.CharField(label='Точность выдерживания режима полета')
    circumspection = forms.CharField(label='Ведение осмотрительности, наблюдение и контроль')
    commercial = forms.CharField(label='Коммерческий подход к полету')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh756(forms.Form):
    attestation = forms.CharField(label='Результаты летной проверки(сдал/не сдал)')
    recommendations = forms.CharField(label='РЕКОМЕНДАЦИИ', widget=forms.Textarea)
    examiner = forms.CharField(label='Фамилия')
    license_num = forms.CharField(label='Номер пилотского свидетельства')
    date = forms.CharField(label='Дата')


forms_dict = {0: FormCh750,
              1: FormCh751,
              2: FormCh752,
              3: FormCh753,
              4: FormCh754,
              5: FormCh755,
              6: FormCh756}
