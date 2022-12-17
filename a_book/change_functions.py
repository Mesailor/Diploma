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


change_funcs = {4: change_ch4,
                5: change_ch5}