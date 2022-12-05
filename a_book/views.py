from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .forms import Chapter4
from .models import Table_Ch4


def home(request):
    return HttpResponseRedirect('/chapter')

def chapter(request):
    '''Данная функция предназначена для отображения информации каждого раздела. Сейчас в ней содержится
    отображение только одного созданного раздела.'''
    records = Table_Ch4.objects.all()
    return render(request, 'a_book/chapter4.html', {'records': records})

def create(request):
    '''Функция добавления записей в таблицу раздела'''
    if request.method == 'POST':
        record = Table_Ch4()
        record.date = request.POST.get('date')
        record.exercise = request.POST.get('exercise')
        record.time = request.POST.get('time')
        record.grade = request.POST.get('grade')
        record.examiner = request.POST.get('examiner')
        record.save()
        return HttpResponseRedirect('/chapter')
    else:
        chapter_form = Chapter4()
        return render(request, 'a_book/create.html', {'form': chapter_form})

def edit(request, id):
    '''Функция редактирования добавленных в таблицу записей'''
    try:
        record = Table_Ch4.objects.get(id=id)

        if request.method == "POST":
            record.date = request.POST.get('date')
            record.exercise = request.POST.get('exercise')
            record.time = request.POST.get('time')
            record.grade = request.POST.get('grade')
            record.examiner = request.POST.get('examiner')
            record.save()
            return HttpResponseRedirect("/chapter")
        else:
            return render(request, "a_book/edit.html", {'record': record})
    except Table_Ch4.DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')

def delete(request, id):
    '''Функция удаления запсей из таблицы'''
    try:
        record = Table_Ch4.objects.get(id=id)
        record.delete()
        return HttpResponseRedirect("/chapter")
    except Table_Ch4.DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")