from . import views
from django.urls import path
app_name='MovieApp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_mov,name='add_mov'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
