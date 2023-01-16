def change_ch740(request, record):
    record.candidate = request.POST.get('candidate')
    record.type_n_number = request.POST.get('type_n_number')
    record.aerodrome = request.POST.get('aerodrome')
    record.date = request.POST.get('date')
    record.time = request.POST.get('time')
    record.sum_time = request.POST.get('sum_time')
    record.result = request.POST.get('result')
    record.examiner = request.POST.get('examiner')


def change_ch741(request, record):
    record.preparation = request.POST.get('preparation')
    record.inspection = request.POST.get('inspection')
    record.startup = request.POST.get('startup')
    record.takeoff = request.POST.get('takeoff')
    record.circle_flight = request.POST.get('circle_flight')
    record.landing = request.POST.get('landing')
    record.approach = request.POST.get('approach')
    record.missed_approach = request.POST.get('missed_approach')
    record.radio_failure = request.POST.get('radio_failure')
    record.eng_failure = request.POST.get('eng_failure')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch742(request, record):
    record.attestation = request.POST.get('attestation')
    record.recommendations = request.POST.get('recommendations')
    record.signature = request.POST.get('signature')
    record.examiner = request.POST.get('examiner')
    record.license_num = request.POST.get('license_num')
    record.date = request.POST.get('date')


change_funcs = {0: change_ch740,
                1: change_ch741,
                2: change_ch742}
