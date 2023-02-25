from django import forms


class FormCh760(forms.Form):
    candidate = forms.CharField(label='Кандидат')
    type_n_number = forms.CharField(label='Тип и регистрационный номер ВС')
    aerodrome = forms.CharField(label='Аэродром взлета/посадки')
    date = forms.CharField(label='Дата проверки')
    time = forms.CharField(label='Время полета')
    sum_time = forms.CharField(label='Общий налет')
    result = forms.CharField(label='Общий результат проверки')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh761(forms.Form):
    preparation = forms.CharField(label='Подготовка к полету')
    knowledge = forms.CharField(label='Знание РЛЭ самолета')
    startup_prep = forms.CharField(label='Операции перед запуском')
    before_takeoff = forms.CharField(label='Запуск двигателя и проверки. Руление, процедуры перед взлетом')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh762(forms.Form):
    standard_maneuvers = forms.CharField(label='Набор высоты, горизонтальный полет, снижение, развороты на заданный курс')
    turns = forms.CharField(label='Виражи, глубокие виражи и развороты на заданный курс')
    stall = forms.CharField(label='Вывод из режима сваливания')
    no_eng_landing = forms.CharField(label='Имитация аварийной посадки вне аэродрома с неработающим двигателем')
    emerg_landing = forms.CharField(label='Имитация вынужденной посадки с подбором площадки')
    emerg_situation = forms.CharField(label='Подготовка кандидата к действиям в аварийной обстановке')
    circle_entering = forms.CharField(label='Вход в круг полетов')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh763(forms.Form):
    takeoff = forms.CharField(label='Взлет')
    eng_failure = forms.CharField(label='Имитация отказа двигателя после взлета или при полете по кругу')
    circle_flight = forms.CharField(label='Полет по кругу')
    circle_low_alt = forms.CharField(label='Полет по кругу на малой высоте')
    app_n_landing = forms.CharField(label='Заход на посадку и посадка')
    short_rw = forms.CharField(label='Заход на посадку и посадка на короткую площадку')
    missed_approach = forms.CharField(label='Уход на второй круг')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh764(forms.Form):
    attestation = forms.CharField(label='Результаты летной проверки(сдал/не сдал)')
    recommendations = forms.CharField(label='РЕКОМЕНДАЦИИ', widget=forms.Textarea)
    examiner = forms.CharField(label='Фамилия')
    license_num = forms.CharField(label='Номер пилотского свидетельства')
    date = forms.CharField(label='Дата')


forms_dict = {0: FormCh760,
              1: FormCh761,
              2: FormCh762,
              3: FormCh763,
              4: FormCh764}
