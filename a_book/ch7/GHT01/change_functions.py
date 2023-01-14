def change_ch710(request, record):
    record.candidate = request.POST.get('candidate')
    record.type_n_number = request.POST.get('type_n_number')
    record.aerodrome = request.POST.get('aerodrome')
    record.date = request.POST.get('date')
    record.time = request.POST.get('time')
    record.sum_time = request.POST.get('sum_time')
    record.result = request.POST.get('result')
    record.examiner = request.POST.get('examiner')


def change_ch711(request, record):
    record.preparation = request.POST.get('preparation')
    record.knowledge = request.POST.get('knowledge')
    record.startup = request.POST.get('startup')
    record.taxiing = request.POST.get('taxiing')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch712(request, record):
    record.takeoff = request.POST.get('takeoff')
    record.circle_flight = request.POST.get('circle_flight')
    record.app_n_landing = request.POST.get('app_n_landing')
    record.complicated_takeoff = request.POST.get('complicated_takeoff')
    record.complicated_landing = request.POST.get('complicated_landing')
    record.missed_approach = request.POST.get('missed_approach')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch713(request, record):
    record.climb_n_descent = request.POST.get('climb_n_descent')
    record.turn45 = request.POST.get('turn45')
    record.turn60 = request.POST.get('turn60')
    record.stall = request.POST.get('stall')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch714(request, record):
    record.eng_failure = request.POST.get('eng_failure')
    record.no_eng_landing = request.POST.get('no_eng_landing')
    record.emerg_landing = request.POST.get('emerg_landing')
    record.eng_fire = request.POST.get('eng_fire')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch715(request, record):
    record.horiz_flight = request.POST.get('horiz_flight')
    record.climb_n_descent = request.POST.get('climb_n_descent')
    record.turns = request.POST.get('turns')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch716(request, record):
    record.circumspection = request.POST.get('circumspection')
    record.weather = request.POST.get('weather')
    record.exploitation = request.POST.get('exploitation')
    record.technology = request.POST.get('technology')
    record.radio = request.POST.get('radio')
    record.afterflight_proc = request.POST.get('afterflight_proc')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch717(request, record):
    record.attestation = request.POST.get('attestation')
    record.recommendations = request.POST.get('recommendations')
    record.signature = request.POST.get('signature')
    record.examiner = request.POST.get('examiner')
    record.license_num = request.POST.get('license_num')
    record.date = request.POST.get('date')


change_funcs = {0: change_ch710,
                1: change_ch711,
                2: change_ch712,
                3: change_ch713,
                4: change_ch714,
                5: change_ch715,
                6: change_ch716,
                7: change_ch717}
