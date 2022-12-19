from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book import models
from a_book.change_functions import change_funcs

htmls = {1: 'a_book/chapter1.html',
         2: 'a_book/chapter2.html',
         3: '',
         4: 'a_book/chapter4.html',
         5: 'a_book/chapter5.html',
         6: '',
         7: '',
         8: 'a_book/chapter8.html',
         9: 'a_book/chapter9.html',
         10: 'a_book/chapter10.html',
         11: ''}


def home(request):
    return HttpResponseRedirect('/contents')


def chapter(request, number):
    '''Данная функция предназначена для отображения информации каждого раздела.'''
    records = models.tables[number].objects.all()
    return render(request, htmls[number], {'records': records, 'number': number})


def create(request, number):
    '''Функция добавления записей в таблицу раздела'''
    record = models.tables[number]()
    records = models.tables[number].objects.all()
    if request.method == 'POST':
        change_funcs[number](request, record)
        record.save()
        return HttpResponseRedirect('/chapter/' + str(number))
    else:
        return render(request, htmls[number], {'records': records, 'number': number, 'creating': True})


def edit(request, number, id):
    '''Функция редактирования добавленных в таблицу записей'''
    records = models.tables[number].objects.all()
    try:
        record = models.tables[number].objects.get(id=id)
        if request.method == "POST":
            change_funcs[number](request, record)
            record.save()
            return HttpResponseRedirect("/chapter/" + str(number))
        else:
            return render(request, htmls[number], {'records': records, 'number': number, 'id': id, 'editing': True})
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