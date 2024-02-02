
from django.urls import path,include
from . import views
urlpatterns = [
    path('view/', views.viewUser, name='view-user-details'),
    path('write/', views.Write, name='write-data'),
    path('switchboard/', views.Board, name='switchboard-page')
]