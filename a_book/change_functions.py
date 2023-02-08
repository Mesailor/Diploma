def change_ch1(request, record):
    record.student = request.POST.get('student')
    record.group = request.POST.get('group')
    record.date = request.POST.get('date')
    record.instructor1 = request.POST.get('instructor1')
    record.instructor2 = request.POST.get('instructor2')
    record.instructor3 = request.POST.get('instructor3')


def change_ch2(request, record):
    record.student = request.POST.get('student')


def change_ch4(request, record):
    record.date = request.POST.get('date')
    record.exercise = request.POST.get('exercise')
    record.time = request.POST.get('time')
    record.grade = request.POST.get('grade')
    record.examiner = request.POST.get('examiner')


def change_ch5(request, record):
    record.date = request.POST.get('date')
    record.type = request.POST.get('type')
    record.exercise = request.POST.get('exercise')
    record.time_hours = request.POST.get('time_hours')
    record.time_mins = request.POST.get('time_mins')
    record.instrumental_time_hours = request.POST.get('instrumental_time_hours')
    record.instrumental_time_mins = request.POST.get('instrumental_time_mins')
    record.grade = request.POST.get('grade')
    record.examiner = request.POST.get('examiner')


def change_ch6(request, record):
    record.date = request.POST.get('date')
    record.type = request.POST.get('type')
    record.exercise = request.POST.get('exercise')
    record.quantity_approach = request.POST.get('quantity_approach')
    record.quantity_landing = request.POST.get('quantity_landing')
    record.time_hours = request.POST.get('time_hours')
    record.time_mins = request.POST.get('time_mins')
    record.instrumental_time_hours = request.POST.get('instrumental_time_hours')
    record.instrumental_time_mins = request.POST.get('instrumental_time_mins')
    record.extra_time_hours = request.POST.get('extra_time_hours')
    record.extra_time_mins = request.POST.get('extra_time_mins')
    record.captain_hours = request.POST.get('captain_hours')
    record.captain_mins = request.POST.get('captain_mins')
    record.captain_route_hours = request.POST.get('captain_route_hours')
    record.captain_route_mins = request.POST.get('captain_route_mins')
    record.captain_night_hours = request.POST.get('captain_night_hours')
    record.captain_night_mins = request.POST.get('captain_night_mins')
    record.grade = request.POST.get('grade')
    record.examiner = request.POST.get('examiner')


def change_ch8(request, record):
    record.date = request.POST.get('date')
    record.type = request.POST.get('type')
    record.times_of_day = request.POST.get('times_of_day')
    record.flight_permit = request.POST.get('flight_permit')
    record.meteo_height = request.POST.get('meteo_height')
    record.meteo_vis = request.POST.get('meteo_vis')
    record.meteo_wind = request.POST.get('meteo_wind')
    record.examiner = request.POST.get('examiner')


def change_ch9(request, record):
    record.characteristic = request.POST.get('characteristic')


def change_ch10(request, record):
    record.date = request.POST.get('date')
    record.remarks = request.POST.get('remarks')
    record.examiner = request.POST.get('examiner')
    record.deletion_mark = request.POST.get('deletion_mark')


change_funcs = {1: change_ch1,
                2: change_ch2,
                4: change_ch4,
                5: change_ch5,
                6: change_ch6,
                8: change_ch8,
                9: change_ch9,
                10: change_ch10}
