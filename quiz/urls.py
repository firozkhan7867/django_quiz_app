from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name="index"),
    path('create/', views.create,name="create"),
    path('create_1/', views.create_1,name="create_1"),
    path('view/<int:pk>', views.view,name="view"),
    path('view_all/', views.view_all,name="view_all"),
    path('take/<int:pk>', views.take,name="take"),
    path('history/', views.history,name="history"),
]