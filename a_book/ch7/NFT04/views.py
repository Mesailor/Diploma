from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from a_book.ch7.NFT04.change_functions import change_funcs
from a_book.ch7.NFT04.models import *
from a_book.ch7.NFT04 import forms


def chapter74(request):
    context = {'records0': TableCh740.objects.all(),
               'records1': TableCh741.objects.all(),
               'records2': TableCh742.objects.all()}
    return render(request, 'a_book/ch7/NFT04/chapter74.html', context)


def create74(request, table_num):
    """Функция добавления записей в таблицы раздела"""
    form = forms.forms_dict[table_num]()
    record = tables[table_num]()
    if request.method == 'POST':
        change_funcs[table_num](request, record)
        record.save()
        return HttpResponseRedirect('/chapter7/NFT04')
    else:
        return render(request, 'a_book/ch7/NFT04/create74.html', {'form': form})


def edit74(request, table_num, id):
    """Функция редактирования записей в таблицах раздела"""
    htmls = {0: 'a_book/ch7/NFT04/edit740.html',
             1: 'a_book/ch7/NFT04/edit741.html',
             2: 'a_book/ch7/NFT04/edit742.html'}
    try:
        record = tables[table_num].objects.get(id=id)
        if request.method == "POST":
            change_funcs[table_num](request, record)
            record.save()
            return HttpResponseRedirect('/chapter7/NFT04')
        else:
            return render(request, htmls[table_num], {'record': record})
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound('Запись не найдена')


def delete74(request, table_num, id):
    """Функция удаления запсей из таблицы"""
    try:
        record = tables[table_num].objects.get(id=id)
        record.delete()
        return HttpResponseRedirect('/chapter7/NFT04')
    except tables[table_num].DoesNotExist:
        return HttpResponseNotFound("<h2>Запись не найдена</h2>")
