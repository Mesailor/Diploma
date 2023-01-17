def change_ch760(request, record):
    record.candidate = request.POST.get('candidate')
    record.type_n_number = request.POST.get('type_n_number')
    record.aerodrome = request.POST.get('aerodrome')
    record.date = request.POST.get('date')
    record.time = request.POST.get('time')
    record.sum_time = request.POST.get('sum_time')
    record.result = request.POST.get('result')
    record.examiner = request.POST.get('examiner')


def change_ch761(request, record):
    record.preparation = request.POST.get('preparation')
    record.knowledge = request.POST.get('knowledge')
    record.startup_prep = request.POST.get('startup_prep')
    record.before_takeoff = request.POST.get('before_takeoff')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch762(request, record):
    record.standard_maneuvers = request.POST.get('standard_maneuvers')
    record.turns = request.POST.get('turns')
    record.stall = request.POST.get('stall')
    record.no_eng_landing = request.POST.get('no_eng_landing')
    record.emerg_landing = request.POST.get('emerg_landing')
    record.emerg_situation = request.POST.get('emerg_situation')
    record.circle_entering = request.POST.get('circle_entering')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch763(request, record):
    record.takeoff = request.POST.get('takeoff')
    record.eng_failure = request.POST.get('eng_failure')
    record.circle_flight = request.POST.get('circle_flight')
    record.circle_low_alt = request.POST.get('circle_low_alt')
    record.app_n_landing = request.POST.get('app_n_landing')
    record.short_rw = request.POST.get('short_rw')
    record.missed_approach = request.POST.get('missed_approach')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch764(request, record):
    record.attestation = request.POST.get('attestation')
    record.recommendations = request.POST.get('recommendations')
    record.signature = request.POST.get('signature')
    record.examiner = request.POST.get('examiner')
    record.license_num = request.POST.get('license_num')
    record.date = request.POST.get('date')


change_funcs = {0: change_ch760,
                1: change_ch761,
                2: change_ch762,
                3: change_ch763,
                4: change_ch764}
