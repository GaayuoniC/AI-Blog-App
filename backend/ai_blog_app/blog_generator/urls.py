from django.urls import path
from . import views #Both these imports are created in the urls file in the blog gen


urlpatterns=[
    path('',views.index, name='index')#This is the root view
]