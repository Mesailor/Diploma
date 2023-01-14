from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book.ch7.XCT02.change_functions import change_funcs
from a_book.ch7.XCT02.models import *
from a_book.ch7.XCT02 import forms


def chapter72(request):
    context = {'records0': TableCh720.objects.all(),
               'records1': TableCh721.objects.all(),
               'records2': TableCh722.objects.all(),
               'records3': TableCh723.objects.all(),
               'records4': TableCh724.objects.all(),
               'records5': TableCh725.objects.all()}
    return render(request, 'a_book/ch7/XCT02/chapter72.html', context)


def create72(request, table_num):
    """Функция добавления записей в таблицы раздела"""
    form = forms.forms_dict[table_num]()
    record = tables[table_num]()
    if request.method == 'POST':
        change_funcs[table_num](request, record)
        record.save()
        return HttpResponseRedirect('/chapter7/XCT02')
    else:
        return render(request, 'a_book/ch7/XCT02/create72.html', {'form': form})


def edit72(request, table_num, id):
    """Функция редактирования записей в таблицах раздела"""
    htmls = {0: 'a_book/ch7/XCT02/edit720.html',
             1: 'a_book/ch7/XCT02/edit721.html',
             2: 'a_book/ch7/XCT02/edit722.html',
             3: 'a_book/ch7/XCT02/edit723.html',
             4: 'a_book/ch7/XCT02/edit724.html',
             5: 'a_book/ch7/XCT02/edit725.html'}
    try:
        record = tables[table_num].objects.get(id=id)
        if request.method == "POST":
            change_funcs[table_num](request, record)
            record.save()
            return HttpResponseRedirect('/chapter7/XCT02')
        else:
            return render(request, htmls[table_num], {'record': record})
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete72(request, table_num, id):
    """Функция удаления запсей из таблицы"""
    try:
        record = tables[table_num].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/chapter7/XCT02')
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
