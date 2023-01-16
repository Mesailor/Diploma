from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book.ch7.XCT05.change_functions import change_funcs
from a_book.ch7.XCT05.models import *
from a_book.ch7.XCT05 import forms


def chapter75(request):
    context = {'records0': TableCh750.objects.all(),
               'records1': TableCh751.objects.all(),
               'records2': TableCh752.objects.all(),
               'records3': TableCh753.objects.all(),
               'records4': TableCh754.objects.all(),
               'records5': TableCh755.objects.all(),
               'records6': TableCh756.objects.all()}
    return render(request, 'a_book/ch7/XCT05/chapter75.html', context)


def create75(request, table_num):
    """Функция добавления записей в таблицы раздела"""
    form = forms.forms_dict[table_num]()
    record = tables[table_num]()
    if request.method == 'POST':
        change_funcs[table_num](request, record)
        record.save()
        return HttpResponseRedirect('/chapter7/XCT05')
    else:
        return render(request, 'a_book/ch7/XCT05/create75.html', {'form': form})


def edit75(request, table_num, id):
    """Функция редактирования записей в таблицах раздела"""
    htmls = {0: 'a_book/ch7/XCT05/edit750.html',
             1: 'a_book/ch7/XCT05/edit751.html',
             2: 'a_book/ch7/XCT05/edit752.html',
             3: 'a_book/ch7/XCT05/edit753.html',
             4: 'a_book/ch7/XCT05/edit754.html',
             5: 'a_book/ch7/XCT05/edit755.html',
             6: 'a_book/ch7/XCT05/edit756.html'}
    try:
        record = tables[table_num].objects.get(id=id)
        if request.method == "POST":
            change_funcs[table_num](request, record)
            record.save()
            return HttpResponseRedirect('/chapter7/XCT05')
        else:
            return render(request, htmls[table_num], {'record': record})
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete75(request, table_num, id):
    """Функция удаления запсей из таблицы"""
    try:
        record = tables[table_num].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/chapter7/XCT05')
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
