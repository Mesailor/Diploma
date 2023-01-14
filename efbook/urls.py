from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from a_book import views
from a_book.chapter3 import views as views3
from a_book.ch7.GHT01 import views as views71

urlpatterns = [
    path('', views.home),
    path('chapter7', TemplateView.as_view(template_name='a_book/ch7/chapter7.html')),
    path('chapter7/GHT01', views71.chapter71),
    path('chapter7/GHT01/create/<int:table_num>', views71.create71),
    path('chapter7/GHT01/edit/<int:table_num>/<int:id>', views71.edit71),
    path('chapter7/GHT01/delete/<int:table_num>/<int:id>', views71.delete71),
    path('chapter3', views3.chapter3),
    path('chapter3/create/<int:table_num>', views3.create3),
    path('chapter3/edit/<int:table_num>/<int:id>', views3.edit3),
    path('chapter3/delete/<int:table_num>/<int:id>', views3.delete3),
    path('chapter/<int:number>', views.chapter),
    path('create/<int:number>', views.create),
    path('edit/<int:number>/<int:id>/', views.edit),
    path('delete/<int:number>/<int:id>/', views.delete),
    path('contents/', TemplateView.as_view(template_name='a_book/contents.html')),
    path('admin/', admin.site.urls),
]
