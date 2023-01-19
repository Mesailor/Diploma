from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book.ch7.IRT08.change_functions import change_funcs
from a_book.ch7.IRT08.models import *
from a_book.ch7.IRT08 import forms


def chapter78(request):
    context = {'records0': TableCh780.objects.all(),
               'records1': TableCh781.objects.all(),
               'records2': TableCh782.objects.all(),
               'records3': TableCh783.objects.all(),
               'records4': TableCh784.objects.all(),
               'records5': TableCh785.objects.all(),
               'records6': TableCh786.objects.all(),
               'records7': TableCh787.objects.all()}
    return render(request, 'a_book/ch7/IRT08/chapter78.html', context)


def create78(request, table_num):
    """Функция добавления записей в таблицы раздела"""
    form = forms.forms_dict[table_num]()
    record = tables[table_num]()
    if request.method == 'POST':
        change_funcs[table_num](request, record)
        record.save()
        return HttpResponseRedirect('/chapter7/IRT08')
    else:
        return render(request, 'a_book/ch7/IRT08/create78.html', {'form': form})


def edit78(request, table_num, id):
    """Функция редактирования записей в таблицах раздела"""
    htmls = {0: 'a_book/ch7/IRT08/edit780.html',
             1: 'a_book/ch7/IRT08/edit781.html',
             2: 'a_book/ch7/IRT08/edit782.html',
             3: 'a_book/ch7/IRT08/edit783.html',
             4: 'a_book/ch7/IRT08/edit784.html',
             5: 'a_book/ch7/IRT08/edit785.html',
             6: 'a_book/ch7/IRT08/edit786.html',
             7: 'a_book/ch7/IRT08/edit787.html'}
    try:
        record = tables[table_num].objects.get(id=id)
        if request.method == "POST":
            change_funcs[table_num](request, record)
            record.save()
            return HttpResponseRedirect('/chapter7/IRT08')
        else:
            return render(request, htmls[table_num], {'record': record})
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete78(request, table_num, id):
    """Функция удаления запсей из таблицы"""
    try:
        record = tables[table_num].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/chapter7/IRT08')
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
