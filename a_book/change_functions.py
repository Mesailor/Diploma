def change_ch1(request, record):
    record.student = request.POST.get('student')
    record.group = request.POST.get('group')
    record.date = request.POST.get('date')
    record.instructor1 = request.POST.get('instructor1')
    record.instructor2 = request.POST.get('instructor2')
    record.instructor3 = request.POST.get('instructor3')
    record.instructor4 = request.POST.get('instructor4')


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


change_funcs = {1: change_ch1,
                4: change_ch4,
                5: change_ch5}
