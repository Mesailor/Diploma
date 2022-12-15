from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book import forms as frms
from a_book import models
from a_book.create_functions import create_functions
from a_book.edit_functions import edit_functions


def home(request):
    return HttpResponseRedirect('/contents')


def chapter(request, number):
    '''Данная функция предназначена для отображения информации каждого раздела.'''
    htmls = {1: '',
             2: '',
             3: '',
             4: 'a_book/chapter4.html',
             5: 'a_book/chapter5.html',
             6: '',
             7: '',
             8: '',
             9: '',
             10: '',
             11: ''}
    records = models.tables[number].objects.all()
    return render(request, htmls[number], {'records': records, 'number': number})


def create(request, number):
    '''Функция добавления записей в таблицу раздела'''
    record = models.tables[number]()

    if request.method == 'POST':
        create_functions[number](request, record)
        record.save()
        return HttpResponseRedirect('/chapter/' + str(number))
    else:
        chapter_form = frms.forms[number]()
        return render(request, 'a_book/create.html', {'form': chapter_form, 'number': number})


def edit(request, number, id):
    '''Функция редактирования добавленных в таблицу записей'''
    htmls = {4: 'a_book/edit4.html',
             5: 'a_book/edit5.html'}

    try:
        record = models.tables[number].objects.get(id=id)
        if request.method == "POST":
            edit_functions[number](request, record)
            record.save()
            return HttpResponseRedirect("/chapter/" + str(number))
        else:
            return render(request, htmls[number], {'record': record, 'number': number})
    except models.tables[number].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete(request, number, id):
    '''Функция удаления запсей из таблицы'''
    try:
        record = models.tables[number].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect("/chapter/" + str(number))
    except models.tables[number].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")