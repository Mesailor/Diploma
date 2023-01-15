from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book.ch7.IFT03.change_functions import change_funcs
from a_book.ch7.IFT03.models import *
from a_book.ch7.IFT03 import forms


def chapter73(request):
    context = {'records0': TableCh730.objects.all(),
               'records1': TableCh731.objects.all(),
               'records2': TableCh732.objects.all(),
               'records3': TableCh733.objects.all(),
               'records4': TableCh734.objects.all(),
               'records5': TableCh735.objects.all()}
    return render(request, 'a_book/ch7/IFT03/chapter73.html', context)


def create73(request, table_num):
    """Функция добавления записей в таблицы раздела"""
    form = forms.forms_dict[table_num]()
    record = tables[table_num]()
    if request.method == 'POST':
        change_funcs[table_num](request, record)
        record.save()
        return HttpResponseRedirect('/chapter7/IFT03')
    else:
        return render(request, 'a_book/ch7/IFT03/create73.html', {'form': form})


def edit73(request, table_num, id):
    """Функция редактирования записей в таблицах раздела"""
    htmls = {0: 'a_book/ch7/IFT03/edit730.html',
             1: 'a_book/ch7/IFT03/edit731.html',
             2: 'a_book/ch7/IFT03/edit732.html',
             3: 'a_book/ch7/IFT03/edit733.html',
             4: 'a_book/ch7/IFT03/edit734.html',
             5: 'a_book/ch7/IFT03/edit735.html'}
    try:
        record = tables[table_num].objects.get(id=id)
        if request.method == "POST":
            change_funcs[table_num](request, record)
            record.save()
            return HttpResponseRedirect('/chapter7/IFT03')
        else:
            return render(request, htmls[table_num], {'record': record})
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete73(request, table_num, id):
    """Функция удаления запсей из таблицы"""
    try:
        record = tables[table_num].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/chapter7/IFT03')
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
