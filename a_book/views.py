from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book import forms as frms
from a_book import models


def home(request):
    return HttpResponseRedirect('/contents')

def chapter(request, number):
    '''Данная функция предназначена для отображения информации каждого раздела.'''
    htmls = {4: 'a_book/chapter4.html',
             5: 'a_book/chapter5.html'}
    tables = {4: models.Table_Ch4,
              5: models.Table_Ch5}
    records = tables[number].objects.all()
    return render(request, htmls[number], {'records': records, 'number': number})

def create(request, number):
    '''Функция добавления записей в таблицу раздела'''
    tables = {4: models.Table_Ch4(),
              5: models.Table_Ch5()}
    forms = {4: frms.Form_Ch4(),
             5: frms.Form_Ch5()}
    record = tables[number]
    def create_ch4():
        record.date = request.POST.get('date')
        record.exercise = request.POST.get('exercise')
        record.time = request.POST.get('time')
        record.grade = request.POST.get('grade')
        record.examiner = request.POST.get('examiner')
    def create_ch5():
        record.date = request.POST.get('date')
        record.type = request.POST.get('type')
        record.exercise = request.POST.get('exercise')
        record.time_hours = request.POST.get('time_hours')
        record.time_mins = request.POST.get('time_mins')
        record.instrumental_time_hours = request.POST.get('instrumental_time_hours')
        record.instrumental_time_mins = request.POST.get('instrumental_time_mins')
        record.grade = request.POST.get('grade')
        record.examiner = request.POST.get('examiner')
    create_functions = {4: create_ch4(),
                        5: create_ch5()}
    if request.method == 'POST':
        create_functions[number]
        record.save()
        return HttpResponseRedirect('/chapter/' + str(number))
    else:
        chapter_form = forms[number]
        return render(request, 'a_book/create.html', {'form': chapter_form, 'number': number})

def edit(request, number, id):
    '''Функция редактирования добавленных в таблицу записей'''
    htmls = {4: 'a_book/edit4.html',
             5: 'a_book/edit5.html'}
    tables = {4: models.Table_Ch4,
              5: models.Table_Ch5}

    try:
        record = tables[number].objects.get(id=id)

        def edit_ch4(record):
            record.date = request.POST.get('date')
            record.exercise = request.POST.get('exercise')
            record.time = request.POST.get('time')
            record.grade = request.POST.get('grade')
            record.examiner = request.POST.get('examiner')

        def edit_ch5(record):
            record.date = request.POST.get('date')
            record.type = request.POST.get('type')
            record.exercise = request.POST.get('exercise')
            record.time_hours = request.POST.get('time_hours')
            record.time_mins = request.POST.get('time_mins')
            record.instrumental_time_hours = request.POST.get('instrumental_time_hours')
            record.instrumental_time_mins = request.POST.get('instrumental_time_mins')
            record.grade = request.POST.get('grade')
            record.examiner = request.POST.get('examiner')

        edit_functions = {4: edit_ch4,
                          5: edit_ch5}
        if request.method == "POST":
            edit_functions[number](record)
            record.save()
            return HttpResponseRedirect("/chapter/" + str(number))
        else:
            return render(request, htmls[number], {'record': record, 'number': number})
    except models.Table_Ch4.DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')

def delete(request, number, id):
    '''Функция удаления запсей из таблицы'''
    tables = {4: models.Table_Ch4,
              5: models.Table_Ch5}
    try:
        record = tables[number].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect("/chapter/" + str(number))
    except tables[number].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")