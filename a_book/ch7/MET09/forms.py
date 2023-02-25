from django import forms


class FormCh790(forms.Form):
    candidate = forms.CharField(label='Кандидат')
    type_n_number = forms.CharField(label='Тип и регистрационный номер ВС')
    aerodrome = forms.CharField(label='Аэродром взлета/посадки')
    date = forms.CharField(label='Дата проверки')
    time = forms.CharField(label='Время полета')
    sum_time = forms.CharField(label='Общий налет')
    result = forms.CharField(label='Общий результат проверки')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh791(forms.Form):
    preparation = forms.CharField(label='Подготовка к полету')
    knowledge = forms.CharField(label='Знание РЛЭ самолета')
    startup = forms.CharField(label='Операции перед запуском')
    taxiing = forms.CharField(label='Запуск двигателя и проверки. Руление и процедуры перед взлетом')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh792(forms.Form):
    standard_maneuvering = forms.CharField(
        label='Набор высоты, горизонтальный полет, снижение, развороты на заданный курс')
    stall_flight_conf = forms.CharField(label='Вывод из режима сваливания в полетной конфигурации')
    stall_land_conf = forms.CharField(label='Вывод из режима сваливания в посадочной конфигурации')
    eng_fire = forms.CharField(label='Имитация пожара одного двигателя в воздухе')
    one_eng_flight = forms.CharField(label='Пилотирование с несимметричной тягой')
    circle_entrance = forms.CharField(label='Вход в круг полетов')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh793(forms.Form):
    takeoff = forms.CharField(label='Взлет')
    aborted_takeoff = forms.CharField(label='Прерванный взлет')
    eng_failure = forms.CharField(label='Имитация отказа двигателя после взлета')
    circle_flight = forms.CharField(label='Полет по кругу')
    app_n_landing = forms.CharField(label='Заход на посадку и посадка')
    complicated_takeoff = forms.CharField(label='Взлет с короткой площадки/с боковым ветром*')
    complicated_landing = forms.CharField(
        label='Посадка при боковом ветре/с убранными закрылками/на площадку ограниченных размеров*')
    one_eng_landing = forms.CharField(label='Посадка с одним неработающим двигателем')
    missed_approach = forms.CharField(label='Уход на второй круг с обоими работающими двигателями')
    one_eng_mis_apr = forms.CharField(label='Уход на второй круг с одним неработающим двигателем')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh794(forms.Form):
    attestation = forms.CharField(label='Результаты летной проверки(сдал/не сдал)')
    recommendations = forms.CharField(label='РЕКОМЕНДАЦИИ', widget=forms.Textarea)
    examiner = forms.CharField(label='Фамилия')
    license_num = forms.CharField(label='Номер пилотского свидетельства')
    date = forms.CharField(label='Дата')


forms_dict = {0: FormCh790,
              1: FormCh791,
              2: FormCh792,
              3: FormCh793,
              4: FormCh794}
