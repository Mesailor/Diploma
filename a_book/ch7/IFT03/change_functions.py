def change_ch730(request, record):
    record.candidate = request.POST.get('candidate')
    record.type_n_number = request.POST.get('type_n_number')
    record.aerodrome = request.POST.get('aerodrome')
    record.date = request.POST.get('date')
    record.time = request.POST.get('time')
    record.sum_time = request.POST.get('sum_time')
    record.result = request.POST.get('result')
    record.examiner = request.POST.get('examiner')


def change_ch731(request, record):
    record.preparation = request.POST.get('preparation')
    record.pref_inspection = request.POST.get('pref_inspection')
    record.deck_check = request.POST.get('deck_check')
    record.pref_proc = request.POST.get('pref_proc')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch732(request, record):
    record.horiz_flight = request.POST.get('horiz_flight')
    record.climb_n_descent = request.POST.get('climb_n_descent')
    record.turns30 = request.POST.get('turns30')
    record.spirals = request.POST.get('spirals')
    record.turns45 = request.POST.get('turns45')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch733(request, record):
    record.stby_horiz = request.POST.get('stby_horiz')
    record.stby_cl_n_des = request.POST.get('stby_cl_n_des')
    record.stby_turns = request.POST.get('stby_turns')
    record.compl_spatial_pos = request.POST.get('compl_spatial_pos')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch734(request, record):
    record.takeoff_n_landing = request.POST.get('takeoff_n_landing')
    record.nav_operating = request.POST.get('nav_operating')
    record.radio = request.POST.get('radio')
    record.eng_operating = request.POST.get('eng_operating')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch735(request, record):
    record.attestation = request.POST.get('attestation')
    record.recommendations = request.POST.get('recommendations')
    record.examiner = request.POST.get('examiner')
    record.license_num = request.POST.get('license_num')
    record.date = request.POST.get('date')


change_funcs = {0: change_ch730,
                1: change_ch731,
                2: change_ch732,
                3: change_ch733,
                4: change_ch734,
                5: change_ch735}
