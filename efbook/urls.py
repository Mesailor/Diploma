from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from a_book import views
from a_book.chapter3 import views as views3
from a_book.ch7.GHT01 import views as views71
from a_book.ch7.XCT02 import views as views72
from a_book.ch7.IFT03 import views as views73
from a_book.ch7.NFT04 import views as views74

urlpatterns = [
    path('', views.home),
    path('chapter7', TemplateView.as_view(template_name='a_book/ch7/chapter7.html')),
    path('chapter7/GHT01', views71.chapter71),
    path('chapter7/GHT01/create/<int:table_num>', views71.create71),
    path('chapter7/GHT01/edit/<int:table_num>/<int:id>', views71.edit71),
    path('chapter7/GHT01/delete/<int:table_num>/<int:id>', views71.delete71),
    path('chapter7/XCT02', views72.chapter72),
    path('chapter7/XCT02/create/<int:table_num>', views72.create72),
    path('chapter7/XCT02/edit/<int:table_num>/<int:id>', views72.edit72),
    path('chapter7/XCT02/delete/<int:table_num>/<int:id>', views72.delete72),
    path('chapter7/IFT03', views73.chapter73),
    path('chapter7/IFT03/create/<int:table_num>', views73.create73),
    path('chapter7/IFT03/edit/<int:table_num>/<int:id>', views73.edit73),
    path('chapter7/IFT03/delete/<int:table_num>/<int:id>', views73.delete73),
    path('chapter7/NFT04', views74.chapter74),
    path('chapter7/NFT04/create/<int:table_num>', views74.create74),
    path('chapter7/NFT04/edit/<int:table_num>/<int:id>', views74.edit74),
    path('chapter7/NFT04/delete/<int:table_num>/<int:id>', views74.delete74),
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
