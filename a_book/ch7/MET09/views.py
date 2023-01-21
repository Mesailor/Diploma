from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book.ch7.MET09.change_functions import change_funcs
from a_book.ch7.MET09.models import *
from a_book.ch7.MET09 import forms


def chapter79(request):
    context = {'records0': TableCh790.objects.all(),
               'records1': TableCh791.objects.all(),
               'records2': TableCh792.objects.all(),
               'records3': TableCh793.objects.all(),
               'records4': TableCh794.objects.all()}
    return render(request, 'a_book/ch7/MET09/chapter79.html', context)


def create79(request, table_num):
    """Функция добавления записей в таблицы раздела"""
    form = forms.forms_dict[table_num]()
    record = tables[table_num]()
    if request.method == 'POST':
        change_funcs[table_num](request, record)
        record.save()
        return HttpResponseRedirect('/chapter7/MET09')
    else:
        return render(request, 'a_book/ch7/MET09/create79.html', {'form': form})


def edit79(request, table_num, id):
    """Функция редактирования записей в таблицах раздела"""
    htmls = {0: 'a_book/ch7/MET09/edit790.html',
             1: 'a_book/ch7/MET09/edit791.html',
             2: 'a_book/ch7/MET09/edit792.html',
             3: 'a_book/ch7/MET09/edit793.html',
             4: 'a_book/ch7/MET09/edit794.html'}
    try:
        record = tables[table_num].objects.get(id=id)
        if request.method == "POST":
            change_funcs[table_num](request, record)
            record.save()
            return HttpResponseRedirect('/chapter7/MET09')
        else:
            return render(request, htmls[table_num], {'record': record})
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete79(request, table_num, id):
    """Функция удаления запсей из таблицы"""
    try:
        record = tables[table_num].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/chapter7/MET09')
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
