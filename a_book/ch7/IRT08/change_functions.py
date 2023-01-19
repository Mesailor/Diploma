def change_ch780(request, record):
    record.candidate = request.POST.get('candidate')
    record.type_n_number = request.POST.get('type_n_number')
    record.aerodrome = request.POST.get('aerodrome')
    record.date = request.POST.get('date')
    record.time = request.POST.get('time')
    record.sum_time = request.POST.get('sum_time')
    record.result = request.POST.get('result')
    record.examiner = request.POST.get('examiner')


def change_ch781(request, record):
    record.planning = request.POST.get('planning')
    record.inspection = request.POST.get('inspection')
    record.startup = request.POST.get('startup')
    record.ATC_clearance = request.POST.get('ATC_clearance')
    record.takeoff = request.POST.get('takeoff')
    record.airway_entering = request.POST.get('airway_entering')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch782(request, record):
    record.maintaining_track = request.POST.get('maintaining_track')
    record.flightplan = request.POST.get('flightplan')
    record.reports = request.POST.get('reports')
    record.instrumental_flight = request.POST.get('instrumental_flight')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch783(request, record):
    record.hold_area_entering = request.POST.get('hold_area_entering')
    record.accuracy_hold_area = request.POST.get('accuracy_hold_area')
    record.maintaining_alt = request.POST.get('maintaining_alt')
    record.wind_correction = request.POST.get('wind_correction')
    record.hold_area_leaving = request.POST.get('hold_area_leaving')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch784(request, record):
    record.initial_stage = request.POST.get('initial_stage')
    record.landing_course = request.POST.get('landing_course')
    record.ILS_established = request.POST.get('ILS_established')
    record.decision_alt = request.POST.get('decision_alt')
    record.missed_approach = request.POST.get('missed_approach')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch785(request, record):
    record.initial_stage = request.POST.get('initial_stage')
    record.landing_course = request.POST.get('landing_course')
    record.final_stage = request.POST.get('final_stage')
    record.decision_alt = request.POST.get('decision_alt')
    record.missed_approach = request.POST.get('missed_approach')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch786(request, record):
    record.observation = request.POST.get('observation')
    record.flight_info = request.POST.get('flight_info')
    record.radio = request.POST.get('radio')
    record.IFR_knowledge = request.POST.get('IFR_knowledge')
    record.briefing = request.POST.get('briefing')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch787(request, record):
    record.attestation = request.POST.get('attestation')
    record.dateIFT07 = request.POST.get('dateIFT07')
    record.recommendations = request.POST.get('recommendations')
    record.signature = request.POST.get('signature')
    record.examiner = request.POST.get('examiner')
    record.license_num = request.POST.get('license_num')
    record.date = request.POST.get('date')


change_funcs = {0: change_ch780,
                1: change_ch781,
                2: change_ch782,
                3: change_ch783,
                4: change_ch784,
                5: change_ch785,
                6: change_ch786,
                7: change_ch787}
