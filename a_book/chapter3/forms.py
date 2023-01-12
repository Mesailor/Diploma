from django import forms


class FormCh31(forms.Form):
    prev_experience = forms.CharField(
        label='В каких авиационных организациях выполнял полеты и на каких типах ВС летал',
        widget=forms.Textarea)
    head_ltk = forms.CharField(label='Начальник штаба ЛТК')


class FormCh32(forms.Form):
    type = forms.CharField(label='Тип ВС')
    time = forms.CharField(label='Налет на ВС')
    captain_time = forms.CharField(label='В качестве КВС')
    route_time = forms.CharField(label='По маршруту')
    night_time = forms.CharField(label='Ночью')
    instrumental_time = forms.CharField(label='По приборам')


class FormCh33(forms.Form):
    type = forms.CharField(label='Тип ВС')
    trainer_time = forms.CharField(label='Тренировка на летном тренажере(всего)')
    trainer_instrumental = forms.CharField(label='Тренировка на летном тренажере(по приборам)')
    trainer_passed = forms.CharField(label='Тренировка на летном тренажере(в зачет подготовки)')
    time = forms.CharField(label='Полетное время на ВС(всего)')
    instrumental_time = forms.CharField(label='Полетное время на ВС(по приборам)')
    solo_time = forms.CharField(label='Самостоятельный налет(всего)')
    solo_route = forms.CharField(label='Самостоятельный налет(по маршруту)')
    captain_time = forms.CharField(label='Полетное время в качестве КВС(всего)')
    captain_route = forms.CharField(label='Полетное время в качестве КВС(по маршруту)')
    captain_night = forms.CharField(label='Полетное время в качестве КВС(ночью)')
    instructor = forms.CharField(label='Пилот-инструктор')


class FormCh34(forms.Form):
    type = forms.CharField(label='Тип ВС')
    trainer_time = forms.CharField(label='Тренировка на летном тренажере(всего)')
    trainer_instrumental = forms.CharField(label='Тренировка на летном тренажере(по приборам)')
    trainer_passed = forms.CharField(label='Тренировка на летном тренажере(в зачет подготовки)')
    time = forms.CharField(label='Полетное время на ВС(всего)')
    instrumental_time = forms.CharField(label='Полетное время на ВС(по приборам)')
    FO_time = forms.CharField(label='Налет в качестве ВП(всего)')
    FO_passed = forms.CharField(label='Налет в качестве ВП(в зачет подготовки)')
    captain_time = forms.CharField(label='Полетное время в качестве КВС(всего)')
    captain_route = forms.CharField(label='Полетное время в качестве КВС(по маршруту)')
    captain_night = forms.CharField(label='Полетное время в качестве КВС(ночью)')
    instructor = forms.CharField(label='Пилот-инструктор')


class FormCh35(forms.Form):
    type = forms.CharField(label='Тип ВС')
    trainer_time = forms.CharField(label='Тренировка на летном тренажере(всего)')
    trainer_instrumental = forms.CharField(label='Тренировка на летном тренажере(по приборам)')
    trainer_passed = forms.CharField(label='Тренировка на летном тренажере(в зачет подготовки)')
    time = forms.CharField(label='Полетное время на ВС(всего)')
    instrumental_time = forms.CharField(label='Полетное время на ВС(по приборам)')
    captain_time = forms.CharField(label='Полетное время в качестве КВС(всего)')
    captain_route = forms.CharField(label='Полетное время в качестве КВС(по маршруту)')
    captain_night = forms.CharField(label='Полетное время в качестве КВС(ночью)')
    instructor = forms.CharField(label='Пилот-инструктор')


class FormCh36(forms.Form):
    type = forms.CharField(label='Тип ВС')
    trainer_time = forms.CharField(label='Тренировка на летном тренажере(всего)')
    trainer_instrumental = forms.CharField(label='Тренировка на летном тренажере(по приборам)')
    trainer_passed = forms.CharField(label='Тренировка на летном тренажере(в зачет подготовки)')
    time = forms.CharField(label='Полетное время на ВС(всего)')
    instrumental_time = forms.CharField(label='Полетное время на ВС(по приборам)')
    solo_time = forms.CharField(label='Самостоятельный налет(всего)')
    solo_route = forms.CharField(label='Самостоятельный налет(по маршруту)')
    FO_time = forms.CharField(label='Налет в качестве ВП(всего)')
    FO_passed = forms.CharField(label='Налет в качестве ВП(в зачет подготовки)')
    captain_time = forms.CharField(label='Полетное время в качестве КВС(всего)')
    captain_route = forms.CharField(label='Полетное время в качестве КВС(по маршруту)')
    captain_night = forms.CharField(label='Полетное время в качестве КВС(ночью)')
    instructor = forms.CharField(label='Пилот-инструктор')


forms_dict = {1: FormCh31,
              2: FormCh32,
              3: FormCh33,
              4: FormCh34,
              5: FormCh35,
              6: FormCh36}
