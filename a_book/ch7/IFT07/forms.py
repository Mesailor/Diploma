from django import forms


class FormCh770(forms.Form):
    candidate = forms.CharField(label='Кандидат')
    type_n_number = forms.CharField(label='Тип и регистрационный номер ВС')
    aerodrome = forms.CharField(label='Аэродром взлета/посадки')
    date = forms.CharField(label='Дата проверки')
    time = forms.CharField(label='Время полета')
    sum_time = forms.CharField(label='Общий налет')
    result = forms.CharField(label='Общий результат проверки')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh771(forms.Form):
    preparation = forms.CharField(label='Подготовка к полету')
    pref_inspection = forms.CharField(label='Предполетный осмотр')
    deck_check = forms.CharField(label='Проверки пилотажно-навигационного оборудования')
    pref_proc = forms.CharField(label='Предполетные процедуры')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh772(forms.Form):
    turns30 = forms.CharField(label='Развороты с креном до 30° с выходом на заданный курс')
    spirals = forms.CharField(label='Развороты на заданный курс с набором высоты и снижением')
    turns45 = forms.CharField(label='Виражи и развороты с креном 45°')
    maneuvering = forms.CharField(label='Маневрирование при изменении скорости и конфигурации')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh773(forms.Form):
    climb_n_descent = forms.CharField(label='Набор высоты и снижение')
    stby_spirals = forms.CharField(label='Развороты с набором высоты и снижением для выхода на заданный курс')
    stby_maneuvering = forms.CharField(label='Маневрирование при изменении скорости и конфигурации')
    compl_spatial_pos = forms.CharField(label='Вывод самолета из сложного пространственного положения')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh774(forms.Form):
    takeoff_n_land = forms.CharField(label='Взлет и посадка')
    nav_operating = forms.CharField(label='Эксплуатация средств навигации')
    radio = forms.CharField(label='Ведение  радиообмена')
    eng_operating = forms.CharField(label='Эксплуатация самолета и двигателя')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh775(forms.Form):
    attestation = forms.CharField(label='Результаты летной проверки(сдал/не сдал)')
    recommendations = forms.CharField(label='РЕКОМЕНДАЦИИ', widget=forms.Textarea)
    examiner = forms.CharField(label='Фамилия')
    license_num = forms.CharField(label='Номер пилотского свидетельства')
    date = forms.CharField(label='Дата')


forms_dict = {0: FormCh770,
              1: FormCh771,
              2: FormCh772,
              3: FormCh773,
              4: FormCh774,
              5: FormCh775}
