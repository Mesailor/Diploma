from django import forms


class FormCh730(forms.Form):
    candidate = forms.CharField(label='Кандидат')
    type_n_number = forms.CharField(label='Тип и регистрационный номер ВС')
    aerodrome = forms.CharField(label='Аэродром взлета/посадки')
    date = forms.CharField(label='Дата проверки')
    time = forms.CharField(label='Время полета')
    sum_time = forms.CharField(label='Общий налет')
    result = forms.CharField(label='Общий результат проверки')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh731(forms.Form):
    preparation = forms.CharField(label='Подготовка к полету')
    pref_inspection = forms.CharField(label='Предполетный осмотр')
    deck_check = forms.CharField(label='Проверки пилотажно-навигационного оборудования')
    pref_proc = forms.CharField(label='Предполетные процедуры')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh732(forms.Form):
    horiz_flight = forms.CharField(label='Прямолинейный горизонтальный полет')
    climb_n_descent = forms.CharField(label='Набор высоты и снижение')
    turns30 = forms.CharField(label='Виражи и развороты на заданный курс с креном до 30°')
    spirals = forms.CharField(label='Развороты с набором высоты и снижением на заданный курс')
    turns45 = forms.CharField(label='Виражи и развороты на заданный курс с креном 45°')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh733(forms.Form):
    stby_horiz = forms.CharField(label='Прямолинейный горизонтальный полет')
    stby_cl_n_des = forms.CharField(label='Набор высоты и снижение')
    stby_turns = forms.CharField(label='Развороты для выхода на заданный курс')
    compl_spatial_pos = forms.CharField(label='Вывод самолета из сложного пространственного положения')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh734(forms.Form):
    takeoff_n_landing = forms.CharField(label='Взлет и посадка')
    nav_operating = forms.CharField(label='Эксплуатация средств навигации')
    radio = forms.CharField(label='Ведение радиообмена')
    eng_operating = forms.CharField(label='Эксплуатация самолета и двигателя')
    attestation = forms.CharField(label='Аттестация по разделу')
    examiner = forms.CharField(label='Экзаменатор')


class FormCh735(forms.Form):
    attestation = forms.CharField(label='Результаты летной проверки(сдал/не сдал)')
    recommendations = forms.CharField(label='РЕКОМЕНДАЦИИ', widget=forms.Textarea)
    signature = forms.ImageField(label='Подпись экзаменатора')
    examiner = forms.CharField(label='Фамилия')
    license_num = forms.CharField(label='Номер пилотского свидетельства')
    date = forms.CharField(label='Дата')


forms_dict = {0: FormCh730,
              1: FormCh731,
              2: FormCh732,
              3: FormCh733,
              4: FormCh734,
              5: FormCh735}
