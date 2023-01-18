from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book.ch7.IFT07.change_functions import change_funcs
from a_book.ch7.IFT07.models import *
from a_book.ch7.IFT07 import forms


def chapter77(request):
    context = {'records0': TableCh770.objects.all(),
               'records1': TableCh771.objects.all(),
               'records2': TableCh772.objects.all(),
               'records3': TableCh773.objects.all(),
               'records4': TableCh774.objects.all(),
               'records5': TableCh775.objects.all()}
    return render(request, 'a_book/ch7/IFT07/chapter77.html', context)


def create77(request, table_num):
    """Функция добавления записей в таблицы раздела"""
    form = forms.forms_dict[table_num]()
    record = tables[table_num]()
    if request.method == 'POST':
        change_funcs[table_num](request, record)
        record.save()
        return HttpResponseRedirect('/chapter7/IFT07')
    else:
        return render(request, 'a_book/ch7/IFT07/create77.html', {'form': form})


def edit77(request, table_num, id):
    """Функция редактирования записей в таблицах раздела"""
    htmls = {0: 'a_book/ch7/IFT07/edit770.html',
             1: 'a_book/ch7/IFT07/edit771.html',
             2: 'a_book/ch7/IFT07/edit772.html',
             3: 'a_book/ch7/IFT07/edit773.html',
             4: 'a_book/ch7/IFT07/edit774.html',
             5: 'a_book/ch7/IFT07/edit775.html'}
    try:
        record = tables[table_num].objects.get(id=id)
        if request.method == "POST":
            change_funcs[table_num](request, record)
            record.save()
            return HttpResponseRedirect('/chapter7/IFT07')
        else:
            return render(request, htmls[table_num], {'record': record})
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete77(request, table_num, id):
    """Функция удаления запсей из таблицы"""
    try:
        record = tables[table_num].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/chapter7/IFT07')
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
