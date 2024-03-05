from django.urls import path 
from App import views
urlpatterns = [
     path('',views.index,name='index'),
    path('hp/',views.http,name='http'),
    path('web/',views.cat,name='https'),
    path('md/',views.md,name='md'),
    path('dj/',views.dj,name='dj'),
    path('tm/',views.tm,name='tm'),
   
    #path('Fifth',views.Fifth,name='Fifth')
]