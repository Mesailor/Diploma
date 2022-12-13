from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from a_book import views

urlpatterns = [
    path('', views.home),
    path('chapter/<int:number>', views.chapter),
    path('create/<int:number>', views.create),
    path('edit/<int:number>/<int:id>/', views.edit),
    path('delete/<int:number>/<int:id>/', views.delete),
    path('contents/', TemplateView.as_view(template_name='a_book/contents.html')),
    path('admin/', admin.site.urls),
]
