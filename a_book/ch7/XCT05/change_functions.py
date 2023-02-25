def change_ch750(request, record):
    record.candidate = request.POST.get('candidate')
    record.type_n_number = request.POST.get('type_n_number')
    record.aerodrome = request.POST.get('aerodrome')
    record.date = request.POST.get('date')
    record.time = request.POST.get('time')
    record.sum_time = request.POST.get('sum_time')
    record.result = request.POST.get('result')
    record.examiner = request.POST.get('examiner')


def change_ch751(request, record):
    record.research = request.POST.get('research')
    record.route_choice = request.POST.get('route_choice')
    record.flightplan_prep = request.POST.get('flightplan_prep')
    record.calculation = request.POST.get('calculation')
    record.docs_check = request.POST.get('docs_check')
    record.inspection = request.POST.get('inspection')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch752(request, record):
    record.briefing = request.POST.get('briefing')
    record.takeoff = request.POST.get('takeoff')
    record.route_entering = request.POST.get('route_entering')
    record.radio = request.POST.get('radio')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch753(request, record):
    record.VFR = request.POST.get('VFR')
    record.deck_operating = request.POST.get('deck_operating')
    record.nav_proc = request.POST.get('nav_proc')
    record.flightplan_operating = request.POST.get('flightplan_operating')
    record.route_changes = request.POST.get('route_changes')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch754(request, record):
    record.app_n_landing = request.POST.get('app_n_landing')
    record.info_using = request.POST.get('info_using')
    record.postflight_proc = request.POST.get('postflight_proc')
    record.paperwork = request.POST.get('paperwork')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch755(request, record):
    record.accuracy = request.POST.get('accuracy')
    record.circumspection = request.POST.get('circumspection')
    record.commercial = request.POST.get('commercial')
    record.attestation = request.POST.get('attestation')
    record.examiner = request.POST.get('examiner')


def change_ch756(request, record):
    record.attestation = request.POST.get('attestation')
    record.recommendations = request.POST.get('recommendations')
    record.examiner = request.POST.get('examiner')
    record.license_num = request.POST.get('license_num')
    record.date = request.POST.get('date')


change_funcs = {0: change_ch750,
                1: change_ch751,
                2: change_ch752,
                3: change_ch753,
                4: change_ch754,
                5: change_ch755,
                6: change_ch756}
