def change_ch7100(request, record):
    record.candidate = request.POST.get('candidate')
    record.type_n_number = request.POST.get('type_n_number')
    record.aerodrome = request.POST.get('aerodrome')
    record.date = request.POST.get('date')
    record.time = request.POST.get('time')
    record.sum_time = request.POST.get('sum_time')
    record.result = request.POST.get('result')
    record.examiner = request.POST.get('examiner')


def change_ch7101(request, record):
    record.preparation = request.POST.get('preparation')
    record.takeoff = request.POST.get('takeoff')
    record.circle_flight = request.POST.get('circle_flight')
    record.eng_failure = request.POST.get('eng_failure')
    record.one_eng_landing = request.POST.get('one_eng_landing')
    record.missed_approach = request.POST.get('missed_approach')
    record.one_eng_mis_apr = request.POST.get('one_eng_mis_apr')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch7102(request, record):
    record.attestation = request.POST.get('attestation')
    record.dateMET09 = request.POST.get('dateMET09')
    record.recommendations = request.POST.get('recommendations')
    record.signature = request.POST.get('signature')
    record.examiner = request.POST.get('examiner')
    record.license_num = request.POST.get('license_num')
    record.date = request.POST.get('date')


change_funcs = {0: change_ch7100,
                1: change_ch7101,
                2: change_ch7102}
