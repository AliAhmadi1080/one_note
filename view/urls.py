from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_note,name='create'),
    path('view/<str:slug>/',views.view_note,name='view'),
    path('',views.about_page,name='about'),
    path('about/',views.about_page,name='about'),
]
