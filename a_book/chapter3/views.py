from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book.chapter3.change_functions import change_funcs
from a_book.chapter3.models import *
from a_book.chapter3 import forms


def chapter3(request):
    context = {'records1': TableCh31.objects.all(),
               'records2': TableCh32.objects.all(),
               'records3': TableCh33.objects.all(),
               'records4': TableCh34.objects.all(),
               'records5': TableCh35.objects.all(),
               'records6': TableCh36.objects.all()}
    return render(request, 'a_book/chapter3/chapter3.html', context)


def create3(request, table_num):
    """Функция добавления записей в таблицы раздела "Общие данные о летной подготовке" """
    form = forms.forms_dict[table_num]()
    record = tables[table_num]()
    if request.method == 'POST':
        change_funcs[table_num](request, record)
        record.save()
        return HttpResponseRedirect('/chapter3')
    else:
        return render(request, 'a_book/chapter3/create3.html', {'form': form})


def edit3(request, table_num, id):
    htmls = {1: 'a_book/chapter3/edit31.html',
             2: 'a_book/chapter3/edit32.html',
             3: 'a_book/chapter3/edit33.html',
             4: 'a_book/chapter3/edit34.html',
             5: 'a_book/chapter3/edit35.html',
             6: 'a_book/chapter3/edit36.html'}
    try:
        record = tables[table_num].objects.get(id=id)
        if request.method == "POST":
            change_funcs[table_num](request, record)
            record.save()
            return HttpResponseRedirect('/chapter3')
        else:
            return render(request, htmls[table_num], {'record': record})
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete3(request, table_num, id):
    """Функция удаления запсей из таблицы"""
    try:
        record = tables[table_num].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/chapter3')
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
