from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book.ch7.QFT11.change_functions import change_funcs
from a_book.ch7.QFT11.models import *
from a_book.ch7.QFT11 import forms


def chapter711(request):
    context = {'records0': TableCh7110.objects.all(),
               'records1': TableCh7111.objects.all(),
               'records2': TableCh7112.objects.all(),
               'records3': TableCh7113.objects.all(),
               'records4': TableCh7114.objects.all(),
               'records5': TableCh7115.objects.all()}
    return render(request, 'a_book/ch7/QFT11/chapter711.html', context)


def create711(request, table_num):
    """Функция добавления записей в таблицы раздела"""
    form = forms.forms_dict[table_num]()
    record = tables[table_num]()
    if request.method == 'POST':
        change_funcs[table_num](request, record)
        record.save()
        return HttpResponseRedirect('/chapter7/QFT11')
    else:
        return render(request, 'a_book/ch7/QFT11/create711.html', {'form': form})


def edit711(request, table_num, id):
    """Функция редактирования записей в таблицах раздела"""
    htmls = {0: 'a_book/ch7/QFT11/edit7110.html',
             1: 'a_book/ch7/QFT11/edit7111.html',
             2: 'a_book/ch7/QFT11/edit7112.html',
             3: 'a_book/ch7/QFT11/edit7113.html',
             4: 'a_book/ch7/QFT11/edit7114.html',
             5: 'a_book/ch7/QFT11/edit7115.html'}
    try:
        record = tables[table_num].objects.get(id=id)
        if request.method == "POST":
            change_funcs[table_num](request, record)
            record.save()
            return HttpResponseRedirect('/chapter7/QFT11')
        else:
            return render(request, htmls[table_num], {'record': record})
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete711(request, table_num, id):
    """Функция удаления запсей из таблицы"""
    try:
        record = tables[table_num].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/chapter7/QFT11')
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
