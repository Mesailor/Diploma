from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book.ch7.GHT06.change_functions import change_funcs
from a_book.ch7.GHT06.models import *
from a_book.ch7.GHT06 import forms


def chapter76(request):
    context = {'records0': TableCh760.objects.all(),
               'records1': TableCh761.objects.all(),
               'records2': TableCh762.objects.all(),
               'records3': TableCh763.objects.all(),
               'records4': TableCh764.objects.all()}
    return render(request, 'a_book/ch7/GHT06/chapter76.html', context)


def create76(request, table_num):
    """Функция добавления записей в таблицы раздела"""
    form = forms.forms_dict[table_num]()
    record = tables[table_num]()
    if request.method == 'POST':
        change_funcs[table_num](request, record)
        record.save()
        return HttpResponseRedirect('/chapter7/GHT06')
    else:
        return render(request, 'a_book/ch7/GHT06/create76.html', {'form': form})


def edit76(request, table_num, id):
    """Функция редактирования записей в таблицах раздела"""
    htmls = {0: 'a_book/ch7/GHT06/edit760.html',
             1: 'a_book/ch7/GHT06/edit761.html',
             2: 'a_book/ch7/GHT06/edit762.html',
             3: 'a_book/ch7/GHT06/edit763.html',
             4: 'a_book/ch7/GHT06/edit764.html'}
    try:
        record = tables[table_num].objects.get(id=id)
        if request.method == "POST":
            change_funcs[table_num](request, record)
            record.save()
            return HttpResponseRedirect('/chapter7/GHT06')
        else:
            return render(request, htmls[table_num], {'record': record})
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete76(request, table_num, id):
    """Функция удаления запсей из таблицы"""
    try:
        record = tables[table_num].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/chapter7/GHT06')
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
