from django import forms


class FormCh710(forms.Form):
    candidate = forms.CharField(label='Кандидат')
    type_n_number = forms.CharField(label='Тип и регистрационный номер ВС')
    aerodrome = forms.CharField(label='Аэродром взлета/посадки')
    date = forms.CharField(label='Дата проверки')
    time = forms.CharField(label='Время полета')
    sum_time = forms.CharField(label='Общий налет')
    result = forms.CharField(label='Общий результат проверки')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh711(forms.Form):
    preparation = forms.CharField(label='Подготовка к полету')
    knowledge = forms.CharField(label='Знание РЛЭ самолета')
    startup = forms.CharField(label='Запуск двигателя и проверки')
    taxiing = forms.CharField(label='Руление и процедуры перед взлетом')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh712(forms.Form):
    takeoff = forms.CharField(label='Взлет')
    circle_flight = forms.CharField(label='Полет по кругу')
    app_n_landing = forms.CharField(label='Заход на посадку и посадка')
    complicated_takeoff = forms.CharField(label='Взлет с короткой площадки/с боковым ветром*')
    complicated_landing = forms.CharField(
        label='Посадка с боковым ветром/убранными закрылками/на площадку ограниченных размеров')
    missed_approach = forms.CharField(label='Уход на второй круг')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh713(forms.Form):
    climb_n_descent = forms.CharField(label='Набор высоты и снижение')
    turn45 = forms.CharField(label='Виражи с креном 45°')
    turn60 = forms.CharField(label='Глубокие виражи с креном до 60°')
    stall = forms.CharField(label='Вывод из режима сваливания')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh714(forms.Form):
    eng_failure = forms.CharField(label='Имитация отказа двигателя после взлета/на кругу*')
    no_eng_landing = forms.CharField(label='Имитация вынужденной посадки вне аэродрома с неработающим двигателем')
    emerg_landing = forms.CharField(label='Имитация вынужденной посадки с подбором площадки')
    eng_fire = forms.CharField(label='Имитация пожара двигателя на земле/в полете*')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh715(forms.Form):
    horiz_flight = forms.CharField(label='Прямолинейный горизонтальный полет')
    climb_n_descent = forms.CharField(label='Набор высоты до заданной и снижение на заданную высоту')
    turns = forms.CharField(label='Развороты на заданный курс с креном 20° и 30°')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh716(forms.Form):
    circumspection = forms.CharField(label='Соблюдение правил осмотрительности на земле и в полете')
    weather = forms.CharField(label='Наблюдение за погодными условиями, ведение визуальной ориентировки')
    exploitation = forms.CharField(label='Эксплуатация двигателя, систем и оборудования самолета')
    technology = forms.CharField(label='Выполнение технологии производства полета')
    radio = forms.CharField(label='Ведение радиосвязи и фразеология радиообмена')
    afterflight_proc = forms.CharField(label='Послеполетные процедуры')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh717(forms.Form):
    attestation = forms.CharField(label='Результаты летной проверки(сдал/не сдал)')
    recommendations = forms.CharField(label='РЕКОМЕНДАЦИИ', widget=forms.Textarea)
    examiner = forms.CharField(label='Фамилия')
    license_num = forms.CharField(label='Номер пилотского свидетельства')
    date = forms.CharField(label='Дата')


forms_dict = {0: FormCh710,
              1: FormCh711,
              2: FormCh712,
              3: FormCh713,
              4: FormCh714,
              5: FormCh715,
              6: FormCh716,
              7: FormCh717}
