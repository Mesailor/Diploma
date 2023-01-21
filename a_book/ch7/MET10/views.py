from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book.ch7.MET10.change_functions import change_funcs
from a_book.ch7.MET10.models import *
from a_book.ch7.MET10 import forms


def chapter710(request):
    context = {'records0': TableCh7100.objects.all(),
               'records1': TableCh7101.objects.all(),
               'records2': TableCh7102.objects.all()}
    return render(request, 'a_book/ch7/MET10/chapter710.html', context)


def create710(request, table_num):
    """Функция добавления записей в таблицы раздела"""
    form = forms.forms_dict[table_num]()
    record = tables[table_num]()
    if request.method == 'POST':
        change_funcs[table_num](request, record)
        record.save()
        return HttpResponseRedirect('/chapter7/MET10')
    else:
        return render(request, 'a_book/ch7/MET10/create710.html', {'form': form})


def edit710(request, table_num, id):
    """Функция редактирования записей в таблицах раздела"""
    htmls = {0: 'a_book/ch7/MET10/edit7100.html',
             1: 'a_book/ch7/MET10/edit7101.html',
             2: 'a_book/ch7/MET10/edit7102.html'}
    try:
        record = tables[table_num].objects.get(id=id)
        if request.method == "POST":
            change_funcs[table_num](request, record)
            record.save()
            return HttpResponseRedirect('/chapter7/MET10')
        else:
            return render(request, htmls[table_num], {'record': record})
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete710(request, table_num, id):
    """Функция удаления запсей из таблицы"""
    try:
        record = tables[table_num].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/chapter7/MET10')
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
