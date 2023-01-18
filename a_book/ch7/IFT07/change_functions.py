def change_ch770(request, record):
    record.candidate = request.POST.get('candidate')
    record.type_n_number = request.POST.get('type_n_number')
    record.aerodrome = request.POST.get('aerodrome')
    record.date = request.POST.get('date')
    record.time = request.POST.get('time')
    record.sum_time = request.POST.get('sum_time')
    record.result = request.POST.get('result')
    record.examiner = request.POST.get('examiner')


def change_ch771(request, record):
    record.preparation = request.POST.get('preparation')
    record.pref_inspection = request.POST.get('pref_inspection')
    record.deck_check = request.POST.get('deck_check')
    record.pref_proc = request.POST.get('pref_proc')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch772(request, record):
    record.turns30 = request.POST.get('turns30')
    record.spirals = request.POST.get('spirals')
    record.turns45 = request.POST.get('turns45')
    record.maneuvering = request.POST.get('maneuvering')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch773(request, record):
    record.climb_n_descent = request.POST.get('climb_n_descent')
    record.stby_spirals = request.POST.get('stby_spirals')
    record.stby_maneuvering = request.POST.get('stby_maneuvering')
    record.compl_spatial_pos = request.POST.get('compl_spatial_pos')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch774(request, record):
    record.takeoff_n_land = request.POST.get('takeoff_n_land')
    record.nav_operating = request.POST.get('nav_operating')
    record.radio = request.POST.get('radio')
    record.eng_operating = request.POST.get('eng_operating')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch775(request, record):
    record.attestation = request.POST.get('attestation')
    record.recommendations = request.POST.get('recommendations')
    record.signature = request.POST.get('signature')
    record.examiner = request.POST.get('examiner')
    record.license_num = request.POST.get('license_num')
    record.date = request.POST.get('date')


change_funcs = {0: change_ch770,
                1: change_ch771,
                2: change_ch772,
                3: change_ch773,
                4: change_ch774,
                5: change_ch775}
