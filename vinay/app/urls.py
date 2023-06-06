from django.urls import path
from . import views
from .views import submit_poem

urlpatterns = [
     path('', views.app, name='app'),
     path('submit/', views.submit_poem, name='submit'),
    path('poem/', views.second, name='second'),
    path('experiment', views.experiment, name='experiment'),

]