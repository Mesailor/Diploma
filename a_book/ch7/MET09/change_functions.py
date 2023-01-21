def change_ch790(request, record):
    record.candidate = request.POST.get('candidate')
    record.type_n_number = request.POST.get('type_n_number')
    record.aerodrome = request.POST.get('aerodrome')
    record.date = request.POST.get('date')
    record.time = request.POST.get('time')
    record.sum_time = request.POST.get('sum_time')
    record.result = request.POST.get('result')
    record.examiner = request.POST.get('examiner')


def change_ch791(request, record):
    record.preparation = request.POST.get('preparation')
    record.knowledge = request.POST.get('knowledge')
    record.startup = request.POST.get('startup')
    record.taxiing = request.POST.get('taxiing')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch792(request, record):
    record.standard_maneuvering = request.POST.get('standard_maneuvering')
    record.stall_flight_conf = request.POST.get('stall_flight_conf')
    record.stall_land_conf = request.POST.get('stall_land_conf')
    record.eng_fire = request.POST.get('eng_fire')
    record.one_eng_flight = request.POST.get('one_eng_flight')
    record.circle_entrance = request.POST.get('circle_entrance')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch793(request, record):
    record.takeoff = request.POST.get('takeoff')
    record.aborted_takeoff = request.POST.get('aborted_takeoff')
    record.eng_failure = request.POST.get('eng_failure')
    record.circle_flight = request.POST.get('circle_flight')
    record.app_n_landing = request.POST.get('app_n_landing')
    record.complicated_takeoff = request.POST.get('complicated_takeoff')
    record.complicated_landing = request.POST.get('complicated_landing')
    record.one_eng_landing = request.POST.get('one_eng_landing')
    record.missed_approach = request.POST.get('missed_approach')
    record.one_eng_mis_apr = request.POST.get('one_eng_mis_apr')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch794(request, record):
    record.attestation = request.POST.get('attestation')
    record.recommendations = request.POST.get('recommendations')
    record.signature = request.POST.get('signature')
    record.examiner = request.POST.get('examiner')
    record.license_num = request.POST.get('license_num')
    record.date = request.POST.get('date')


change_funcs = {0: change_ch790,
                1: change_ch791,
                2: change_ch792,
                3: change_ch793,
                4: change_ch794}
