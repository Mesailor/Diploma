from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from a_book import views
from a_book.chapter3 import views as views3
from a_book.ch7.GHT01 import views as views71
from a_book.ch7.XCT02 import views as views72
from a_book.ch7.IFT03 import views as views73
from a_book.ch7.NFT04 import views as views74
from a_book.ch7.XCT05 import views as views75
from a_book.ch7.GHT06 import views as views76
from a_book.ch7.IFT07 import views as views77
from a_book.ch7.IRT08 import views as views78
from a_book.ch7.MET09 import views as views79
from a_book.ch7.MET10 import views as views710
from a_book.ch7.QFT11 import views as views711

urlpatterns = [
    path('', views.home),
    path('chapter/<int:number>', views.chapter),
    path('create/<int:number>', views.create),
    path('edit/<int:number>/<int:id>/', views.edit),
    path('delete/<int:number>/<int:id>/', views.delete),
    path('admin/', admin.site.urls),
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
    path('chapter7/XCT05', views75.chapter75),
    path('chapter7/XCT05/create/<int:table_num>', views75.create75),
    path('chapter7/XCT05/edit/<int:table_num>/<int:id>', views75.edit75),
    path('chapter7/XCT05/delete/<int:table_num>/<int:id>', views75.delete75),
    path('chapter7/GHT06', views76.chapter76),
    path('chapter7/GHT06/create/<int:table_num>', views76.create76),
    path('chapter7/GHT06/edit/<int:table_num>/<int:id>', views76.edit76),
    path('chapter7/GHT06/delete/<int:table_num>/<int:id>', views76.delete76),
    path('chapter7/IFT07', views77.chapter77),
    path('chapter7/IFT07/create/<int:table_num>', views77.create77),
    path('chapter7/IFT07/edit/<int:table_num>/<int:id>', views77.edit77),
    path('chapter7/IFT07/delete/<int:table_num>/<int:id>', views77.delete77),
    path('chapter7/IRT08', views78.chapter78),
    path('chapter7/IRT08/create/<int:table_num>', views78.create78),
    path('chapter7/IRT08/edit/<int:table_num>/<int:id>', views78.edit78),
    path('chapter7/IRT08/delete/<int:table_num>/<int:id>', views78.delete78),
    path('chapter7/MET09', views79.chapter79),
    path('chapter7/MET09/create/<int:table_num>', views79.create79),
    path('chapter7/MET09/edit/<int:table_num>/<int:id>', views79.edit79),
    path('chapter7/MET09/delete/<int:table_num>/<int:id>', views79.delete79),
    path('chapter7/MET10', views710.chapter710),
    path('chapter7/MET10/create/<int:table_num>', views710.create710),
    path('chapter7/MET10/edit/<int:table_num>/<int:id>', views710.edit710),
    path('chapter7/MET10/delete/<int:table_num>/<int:id>', views710.delete710),
    path('chapter7/QFT11', views711.chapter711),
    path('chapter7/QFT11/create/<int:table_num>', views711.create711),
    path('chapter7/QFT11/edit/<int:table_num>/<int:id>', views711.edit711),
    path('chapter7/QFT11/delete/<int:table_num>/<int:id>', views711.delete711),
    path('chapter3', views3.chapter3),
    path('chapter3/create/<int:table_num>', views3.create3),
    path('chapter3/edit/<int:table_num>/<int:id>', views3.edit3),
    path('chapter3/delete/<int:table_num>/<int:id>', views3.delete3),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
