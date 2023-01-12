def change_ch31(request, record):
    record.prev_experience = request.POST.get('prev_experience')
    record.head_ltk = request.POST.get('head_ltk')


def change_ch32(request, record):
    record.type = request.POST.get('type')
    record.time = request.POST.get('time')
    record.captain_time = request.POST.get('captain_time')
    record.route_time = request.POST.get('route_time')
    record.night_time = request.POST.get('night_time')
    record.instrumental_time = request.POST.get('instrumental_time')


def change_ch33(request, record):
    record.type = request.POST.get('type')
    record.trainer_time = request.POST.get('trainer_time')
    record.trainer_instrumental = request.POST.get('trainer_instrumental')
    record.trainer_passed = request.POST.get('trainer_passed')
    record.time = request.POST.get('time')
    record.instrumental_time = request.POST.get('instrumental_time')
    record.solo_time = request.POST.get('solo_time')
    record.solo_route = request.POST.get('solo_route')
    record.captain_time = request.POST.get('captain_time')
    record.captain_route = request.POST.get('captain_route')
    record.captain_night = request.POST.get('captain_night')
    record.instructor = request.POST.get('instructor')


def change_ch34(request, record):
    record.type = request.POST.get('type')
    record.trainer_time = request.POST.get('trainer_time')
    record.trainer_instrumental = request.POST.get('trainer_instrumental')
    record.trainer_passed = request.POST.get('trainer_passed')
    record.time = request.POST.get('time')
    record.instrumental_time = request.POST.get('instrumental_time')
    record.FO_time = request.POST.get('FO_time')
    record.FO_passed = request.POST.get('FO_passed')
    record.captain_time = request.POST.get('captain_time')
    record.captain_route = request.POST.get('captain_route')
    record.captain_night = request.POST.get('captain_night')
    record.instructor = request.POST.get('instructor')


def change_ch35(request, record):
    record.type = request.POST.get('type')
    record.trainer_time = request.POST.get('trainer_time')
    record.trainer_instrumental = request.POST.get('trainer_instrumental')
    record.trainer_passed = request.POST.get('trainer_passed')
    record.time = request.POST.get('time')
    record.instrumental_time = request.POST.get('instrumental_time')
    record.captain_time = request.POST.get('captain_time')
    record.captain_route = request.POST.get('captain_route')
    record.captain_night = request.POST.get('captain_night')
    record.instructor = request.POST.get('instructor')


def change_ch36(request, record):
    record.type = request.POST.get('type')
    record.trainer_time = request.POST.get('trainer_time')
    record.trainer_instrumental = request.POST.get('trainer_instrumental')
    record.trainer_passed = request.POST.get('trainer_passed')
    record.time = request.POST.get('time')
    record.instrumental_time = request.POST.get('instrumental_time')
    record.solo_time = request.POST.get('solo_time')
    record.solo_route = request.POST.get('solo_route')
    record.FO_time = request.POST.get('FO_time')
    record.FO_passed = request.POST.get('FO_passed')
    record.captain_time = request.POST.get('captain_time')
    record.captain_route = request.POST.get('captain_route')
    record.captain_night = request.POST.get('captain_night')
    record.instructor = request.POST.get('instructor')


change_funcs = {1: change_ch31,
                2: change_ch32,
                3: change_ch33,
                4: change_ch34,
                5: change_ch35,
                6: change_ch36}
