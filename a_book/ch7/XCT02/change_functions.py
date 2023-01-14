def change_ch720(request, record):
    record.candidate = request.POST.get('candidate')
    record.type_n_number = request.POST.get('type_n_number')
    record.aerodrome = request.POST.get('aerodrome')
    record.date = request.POST.get('date')
    record.time = request.POST.get('time')
    record.sum_time = request.POST.get('sum_time')
    record.result = request.POST.get('result')
    record.examiner = request.POST.get('examiner')


def change_ch721(request, record):
    record.research = request.POST.get('research')
    record.planning = request.POST.get('planning')
    record.flight_plan = request.POST.get('flight_plan')
    record.operating_proc = request.POST.get('operating_proc')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch722(request, record):
    record.docs_check = request.POST.get('docs_check')
    record.aircraft_inspection = request.POST.get('aircraft_inspection')
    record.startup = request.POST.get('startup')
    record.takeoff = request.POST.get('takeoff')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch723(request, record):
    record.VFR = request.POST.get('VFR')
    record.radio = request.POST.get('radio')
    record.circumspection = request.POST.get('circumspection')
    record.maintaining = request.POST.get('maintaining')
    record.route_changes = request.POST.get('route_changes')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch724(request, record):
    record.approach_prep = request.POST.get('approach_prep')
    record.app_n_landing = request.POST.get('app_n_landing')
    record.afterflight_proc = request.POST.get('afterflight_proc')
    record.paperwork = request.POST.get('paperwork')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch725(request, record):
    record.attestation = request.POST.get('attestation')
    record.dateGHT01 = request.POST.get('dateGHT01')
    record.recommendations = request.POST.get('recommendations')
    record.signature = request.POST.get('signature')
    record.examiner = request.POST.get('examiner')
    record.license_num = request.POST.get('license_num')
    record.date = request.POST.get('date')


change_funcs = {0: change_ch720,
                1: change_ch721,
                2: change_ch722,
                3: change_ch723,
                4: change_ch724,
                5: change_ch725}