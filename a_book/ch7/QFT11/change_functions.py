def change_ch7110(request, record):
    record.candidate = request.POST.get('candidate')
    record.type_n_number = request.POST.get('type_n_number')
    record.aerodrome = request.POST.get('aerodrome')
    record.date = request.POST.get('date')
    record.time = request.POST.get('time')
    record.sum_time = request.POST.get('sum_time')
    record.result = request.POST.get('result')
    record.examiner = request.POST.get('examiner')


def change_ch7111(request, record):
    record.preparation = request.POST.get('preparation')
    record.inspection = request.POST.get('inspection')
    record.startup = request.POST.get('startup')
    record.airway_entering = request.POST.get('airway_entering')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch7112(request, record):
    record.takeoff = request.POST.get('takeoff')
    record.landing = request.POST.get('landing')
    record.eng_failure = request.POST.get('eng_failure')
    record.one_eng_landing = request.POST.get('one_eng_landing')
    record.airway_entering = request.POST.get('airway_entering')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch7113(request, record):
    record.airway_entrance = request.POST.get('airway_entrance')
    record.airway_navigation = request.POST.get('airway_navigation')
    record.hold_area = request.POST.get('hold_area')
    record.precision_app = request.POST.get('precision_app')
    record.nonprecision_app = request.POST.get('nonprecision_app')
    record.missed_approach = request.POST.get('missed_approach')
    record.low_alt_circle = request.POST.get('low_alt_circle')
    record.airway_entering = request.POST.get('airway_entering')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch7114(request, record):
    record.radio = request.POST.get('radio')
    record.observation = request.POST.get('observation')
    record.visual_maneuvering = request.POST.get('visual_maneuvering')
    record.team_work = request.POST.get('team_work')
    record.missed_approach = request.POST.get('missed_approach')
    record.emergency = request.POST.get('emergency')
    record.airway_entering = request.POST.get('airway_entering')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch7115(request, record):
    record.attestation = request.POST.get('attestation')
    record.dateGHT06 = request.POST.get('dateGHT06')
    record.dateIRT08 = request.POST.get('dateIRT08')
    record.dateMET09 = request.POST.get('dateMET09')
    record.dateMET10 = request.POST.get('dateMET10')
    record.recommendations = request.POST.get('recommendations')
    record.examiner = request.POST.get('examiner')
    record.license_num = request.POST.get('license_num')
    record.date = request.POST.get('date')


change_funcs = {0: change_ch7110,
                1: change_ch7111,
                2: change_ch7112,
                3: change_ch7113,
                4: change_ch7114,
                5: change_ch7115}
