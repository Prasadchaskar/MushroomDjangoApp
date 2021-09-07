from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('predict',views.Preedict,name='predict'),
    path('desc',views.Description,name='desc')
]