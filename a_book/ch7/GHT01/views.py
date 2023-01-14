from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book.ch7.GHT01.change_functions import change_funcs
from a_book.ch7.GHT01.models import *
from a_book.ch7.GHT01 import forms


def chapter71(request):
    context = {'records0': TableCh710.objects.all(),
               'records1': TableCh711.objects.all(),
               'records2': TableCh712.objects.all(),
               'records3': TableCh713.objects.all(),
               'records4': TableCh714.objects.all(),
               'records5': TableCh715.objects.all(),
               'records6': TableCh716.objects.all(),
               'records7': TableCh717.objects.all()}
    return render(request, 'a_book/ch7/GHT01/chapter71.html', context)


def create71(request, table_num):
    """Функция добавления записей в таблицы раздела"""
    form = forms.forms_dict[table_num]()
    record = tables[table_num]()
    if request.method == 'POST':
        change_funcs[table_num](request, record)
        record.save()
        return HttpResponseRedirect('/chapter7/GHT01')
    else:
        return render(request, 'a_book/ch7/GHT01/create71.html', {'form': form})


def edit71(request, table_num, id):
    """Функция редактирования записей в таблицах раздела"""
    htmls = {0: 'a_book/ch7/GHT01/edit710.html',
             1: 'a_book/ch7/GHT01/edit711.html',
             2: 'a_book/ch7/GHT01/edit712.html',
             3: 'a_book/ch7/GHT01/edit713.html',
             4: 'a_book/ch7/GHT01/edit714.html',
             5: 'a_book/ch7/GHT01/edit715.html',
             6: 'a_book/ch7/GHT01/edit716.html',
             7: 'a_book/ch7/GHT01/edit717.html'}
    try:
        record = tables[table_num].objects.get(id=id)
        if request.method == "POST":
            change_funcs[table_num](request, record)
            record.save()
            return HttpResponseRedirect('/chapter7/GHT01')
        else:
            return render(request, htmls[table_num], {'record': record})
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete71(request, table_num, id):
    """Функция удаления запсей из таблицы"""
    try:
        record = tables[table_num].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/chapter7/GHT01')
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")